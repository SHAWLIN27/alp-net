"""
Ingest Pipeline — orchestrates the full data ingestion workflow.

Flow:
1. Scan vault for .md files → FileScanner
2. Parse each file → MarkdownFileParser
3. Chunk content for embeddings → ContentChunker
4. Build knowledge graph (nodes + edges) → GraphBuilder
5. Save graph to JSON → GraphStore
6. Generate embeddings → EmbeddingService
7. Index chunks in ChromaDB → VectorStore
"""
import asyncio
import hashlib
import time
from pathlib import Path

from alpnet.config.settings import Settings, get_settings
from alpnet.db.graph_store import GraphStore
from alpnet.db.vector_store import VectorStore
from alpnet.services.embedding_service import EmbeddingService
from alpnet.ingest.parser import MarkdownFileParser, ParsedFile
from alpnet.ingest.chunker import ContentChunker, Chunk
from alpnet.ingest.graph_builder import GraphBuilder


class IngestPipeline:
    """Orchestrates full vault ingestion."""

    def __init__(self, settings: Settings | None = None):
        self.settings = settings or get_settings()
        self.graph_store = GraphStore(self.settings.graph_path)
        self.vector_store = VectorStore(self.settings)
        self.embedding_service = EmbeddingService(self.settings)

    def run(self, full: bool = False) -> dict:
        """Run the full ingestion pipeline. Returns stats dict."""
        start_time = time.monotonic()
        vault_root = self.settings.vault_path.resolve()
        stats: dict = {}

        print("=" * 60)
        print("ALP_Net Ingest Pipeline")
        print("=" * 60)
        print(f"  Vault: {vault_root}")
        print(f"  Mode: {'full' if full else 'incremental'}")
        print()

        # ── Step 1: Scan & Parse ──
        print("📂 Step 1/5: Scanning & parsing markdown files...")
        parsed_files = MarkdownFileParser.scan_vault(vault_root)
        stats["files_scanned"] = len(parsed_files)
        hubs = sum(1 for pf in parsed_files if pf.node_type == "topic_hub")
        leaves = sum(1 for pf in parsed_files if pf.node_type == "leaf_concept")
        print(f"   ✅ Parsed {len(parsed_files)} files ({hubs} hubs, {leaves} leaves)")
        print()

        # ── Step 2: Chunk ──
        print("✂️  Step 2/5: Chunking content for embedding...")
        all_chunks: list[Chunk] = []
        for pf in parsed_files:
            chunks = ContentChunker.chunk_file(pf, str(vault_root))
            all_chunks.extend(chunks)
        stats["chunks_created"] = len(all_chunks)
        # Stats by type
        type_counts: dict[str, int] = {}
        for c in all_chunks:
            type_counts[c.chunk_type] = type_counts.get(c.chunk_type, 0) + 1
        for ct, count in sorted(type_counts.items()):
            print(f"   {ct}: {count} chunks")
        print(f"   ✅ Total: {len(all_chunks)} chunks")
        print()

        # ── Step 3: Build Graph ──
        print("🕸️  Step 3/5: Building knowledge graph...")
        builder = GraphBuilder(parsed_files)
        graph_data = builder.build()
        stats["nodes"] = len(graph_data.nodes)
        stats["edges"] = len(graph_data.edges)

        # Persist to GraphStore
        self.graph_store.load()
        for node in graph_data.nodes:
            self.graph_store.upsert_node(node)
        for edge in graph_data.edges:
            self.graph_store.upsert_edge(edge)
        self.graph_store.save()

        edge_types: dict[str, int] = {}
        for e in graph_data.edges:
            edge_types[e.edge_type.value] = edge_types.get(e.edge_type.value, 0) + 1
        print(f"   Nodes: {stats['nodes']}")
        print(f"   Edges: {stats['edges']}")
        for et, count in sorted(edge_types.items()):
            print(f"     {et}: {count}")
        print(f"   ✅ Graph saved to {self.settings.graph_path}")
        print()

        # ── Step 4: Generate Embeddings ──
        print("🧮 Step 4/5: Generating embeddings...")
        stats["embeddings_generated"] = asyncio.run(
            self._embed_chunks(all_chunks)
        )
        print(f"   ✅ {stats['embeddings_generated']} embeddings generated")
        print()

        # ── Step 5: Index in ChromaDB ──
        print("🔍 Step 5/5: Indexing in ChromaDB...")
        indexed = self._index_chunks(all_chunks)
        stats["chunks_indexed"] = indexed
        print(f"   ✅ {indexed} chunks indexed in ChromaDB")
        print()

        elapsed = time.monotonic() - start_time
        stats["elapsed_seconds"] = round(elapsed, 1)

        print("=" * 60)
        print("✅ Ingestion complete!")
        print(f"   Files: {stats['files_scanned']}")
        print(f"   Chunks: {stats['chunks_created']}")
        print(f"   Graph Nodes: {stats['nodes']}")
        print(f"   Graph Edges: {stats['edges']}")
        print(f"   Embeddings: {stats['embeddings_generated']}")
        print(f"   ChromaDB: {stats['chunks_indexed']}")
        print(f"   Time: {stats['elapsed_seconds']}s")
        print("=" * 60)

        return stats

    async def _embed_chunks(self, chunks: list[Chunk]) -> int:
        """Generate embeddings for all chunks in batches."""
        batch_size = self.settings.embedding_batch_size
        texts = [c.content for c in chunks]
        total = 0

        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            embeddings = await self.embedding_service.embed_texts(batch)
            # Store embeddings back on chunks
            for j, emb in enumerate(embeddings):
                idx = i + j
                if idx < len(chunks):
                    chunks[idx].metadata["_embedding"] = emb
            total += len(embeddings)
            if i > 0 and i % (batch_size * 5) == 0:
                print(f"   ... {total}/{len(texts)}")

        return total

    def _index_chunks(self, chunks: list[Chunk]) -> int:
        """Index all chunks with their embeddings into ChromaDB."""
        if not chunks:
            return 0

        chunk_ids = [c.chunk_id for c in chunks]
        documents = [c.content for c in chunks]
        embeddings = [c.metadata.pop("_embedding", []) for c in chunks]
        metadatas = [c.metadata for c in chunks]

        # Filter out chunks without embeddings
        valid_indices = [i for i, emb in enumerate(embeddings) if emb]
        if not valid_indices:
            return 0

        self.vector_store.upsert_chunks(
            ids=[chunk_ids[i] for i in valid_indices],
            documents=[documents[i] for i in valid_indices],
            embeddings=[embeddings[i] for i in valid_indices],
            metadatas=[metadatas[i] for i in valid_indices],
        )
        return len(valid_indices)
