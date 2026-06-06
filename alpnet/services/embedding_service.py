import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer

from alpnet.config.settings import Settings


class EmbeddingService:
    """Generates embeddings using HashingVectorizer (stateless, offline, no download).
    For production, swap to sentence-transformers or API-based embeddings.
    """

    EMBEDDING_DIM = 384  # match all-MiniLM-L6-v2 for compatibility

    def __init__(self, settings: Settings):
        self.settings = settings
        # HashingVectorizer is stateless — same hash function for all batches
        self._vectorizer = HashingVectorizer(
            n_features=self.EMBEDDING_DIM,
            stop_words="english",
            alternate_sign=False,
            norm="l2",
        )

    def _encode_batch(self, texts: list[str]) -> np.ndarray:
        """Encode batch to fixed-dim dense vectors via feature hashing."""
        sparse = self._vectorizer.transform(texts)
        return sparse.toarray().astype(np.float32)

    async def embed_texts(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for a batch of texts."""
        if not texts:
            return []
        import asyncio
        result = await asyncio.to_thread(self._encode_batch, texts)
        return result.tolist()

    async def embed_query(self, query: str) -> list[float]:
        """Generate embedding for a single query."""
        results = await self.embed_texts([query])
        return results[0]
