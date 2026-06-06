from pydantic_settings import BaseSettings
from pathlib import Path
from functools import lru_cache


class Settings(BaseSettings):
    # DeepSeek API
    deepseek_api_key: str = "your-deepseek-api-key-here"
    deepseek_base_url: str = "https://api.deepseek.com"
    deepseek_model: str = "deepseek-chat"
    deepseek_embedding_model: str = "deepseek-embedding"

    # ChromaDB
    chroma_host: str = "localhost"
    chroma_port: int = 8001

    # Application paths
    vault_path: Path = Path("./vault")
    data_dir: Path = Path("./data")
    graph_file: str = "knowledge_graph.json"

    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True

    # Ingestion
    embedding_batch_size: int = 20
    chunk_size: int = 1000

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

    @property
    def graph_path(self) -> Path:
        return self.data_dir / self.graph_file


@lru_cache()
def get_settings() -> Settings:
    return Settings()
