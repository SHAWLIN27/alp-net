from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from alpnet.api.routes import admin, chat, graph, search
from alpnet.config.settings import get_settings
from alpnet.models.api import HealthResponse

settings = get_settings()

app = FastAPI(
    title="ALP_Net API",
    description="A-Level Physics Knowledge Graph RAG System",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin.router, prefix="/api/v1")
app.include_router(graph.router, prefix="/api/v1")
app.include_router(search.router, prefix="/api/v1")
app.include_router(chat.router, prefix="/api/v1")


@app.get("/", response_model=HealthResponse)
def root() -> HealthResponse:
    return HealthResponse(status="ok")
