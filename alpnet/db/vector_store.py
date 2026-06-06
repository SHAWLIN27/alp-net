from typing import Any

import chromadb

from alpnet.config.settings import Settings


class VectorStore:
    def __init__(self, settings: Settings):
        self.settings = settings
        # Try HTTP client first, fall back to embedded
        try:
            self.client = chromadb.HttpClient(
                host=settings.chroma_host, port=settings.chroma_port
            )
            self.client.heartbeat()
        except Exception:
            # Fall back to local persistent storage
            persist_dir = str(settings.data_dir / "chromadb")
            self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection(name="alpnet_chunks")

    def upsert_chunks(
        self,
        ids: list[str],
        documents: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict[str, Any]],
    ) -> None:
        self.collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def query(
        self,
        query_embedding: list[float],
        top_k: int = 8,
        where: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where,
        )

    def count(self) -> int:
        return self.collection.count()
