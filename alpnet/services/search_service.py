from alpnet.config.settings import Settings
from alpnet.db.vector_store import VectorStore
from alpnet.models.api import SearchResponse, SearchResult
from alpnet.services.embedding_service import EmbeddingService


class SearchService:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.embeddings = EmbeddingService(settings)
        self.vectors = VectorStore(settings)

    async def semantic_search(self, query: str, top_k: int = 8) -> SearchResponse:
        query_embedding = await self.embeddings.embed_query(query)
        raw = self.vectors.query(query_embedding=query_embedding, top_k=top_k)

        ids = raw.get("ids", [[]])[0]
        documents = raw.get("documents", [[]])[0]
        metadatas = raw.get("metadatas", [[]])[0]
        distances = raw.get("distances", [[]])[0]

        results: list[SearchResult] = []
        for item_id, document, metadata, distance in zip(ids, documents, metadatas, distances):
            score = 1.0 / (1.0 + float(distance))
            results.append(
                SearchResult(
                    id=item_id,
                    title=metadata.get("title", item_id) if metadata else item_id,
                    content=document,
                    score=score,
                    source_file=metadata.get("source_file") if metadata else None,
                    metadata=metadata or {},
                )
            )
        return SearchResponse(query=query, results=results)
