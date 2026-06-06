from fastapi import APIRouter, Depends

from alpnet.api.dependencies import get_graph_service
from alpnet.config.settings import Settings, get_settings
from alpnet.models.api import HealthResponse
from alpnet.services.graph_service import GraphService

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get("/stats")
def stats(
    settings: Settings = Depends(get_settings),
    graph: GraphService = Depends(get_graph_service),
) -> dict:
    return {
        "graph": graph.stats(),
        "vault_path": str(settings.vault_path),
        "graph_path": str(settings.graph_path),
    }


@router.post("/ingest")
def ingest() -> dict[str, str]:
    return {"status": "not_implemented", "message": "Ingestion pipeline will be implemented in Phase 3."}
