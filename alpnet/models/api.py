from pydantic import BaseModel, Field

from alpnet.models.nodes import KnowledgeEdge, KnowledgeNode


class HealthResponse(BaseModel):
    status: str
    service: str = "ALP_Net API"


class GraphResponse(BaseModel):
    nodes: list[KnowledgeNode] = Field(default_factory=list)
    edges: list[KnowledgeEdge] = Field(default_factory=list)


class SearchRequest(BaseModel):
    model_config = {"extra": "allow"}
    query: str
    top_k: int = 8
    filters: dict[str, str | list[str]] = Field(default_factory=dict)


class SearchResult(BaseModel):
    id: str
    title: str
    content: str
    score: float
    source_file: str | None = None
    metadata: dict = Field(default_factory=dict)


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult] = Field(default_factory=list)


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None
    top_k: int = 8
    syllabus_filter: list[str] = Field(default_factory=list)
    difficulty: str | None = None


class SourceCitation(BaseModel):
    id: str
    title: str
    source_file: str | None = None
    score: float | None = None


class ChatResponse(BaseModel):
    answer: str
    conversation_id: str
    sources: list[SourceCitation] = Field(default_factory=list)
    graph_context: GraphResponse = Field(default_factory=GraphResponse)
