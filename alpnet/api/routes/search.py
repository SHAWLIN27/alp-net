from fastapi import APIRouter, Depends, Request

from alpnet.api.dependencies import get_search_service
from alpnet.models.api import SearchResponse
from alpnet.services.search_service import SearchService

router = APIRouter(prefix="/search", tags=["search"])


@router.post("/semantic", response_model=SearchResponse)
async def semantic_search(
    req: Request,
    search: SearchService = Depends(get_search_service),
) -> SearchResponse:
    body = await req.json()
    return await search.semantic_search(body.get("query", ""), top_k=body.get("top_k", 8))


@router.post("/hybrid", response_model=SearchResponse)
async def hybrid_search(
    req: Request,
    search: SearchService = Depends(get_search_service),
) -> SearchResponse:
    body = await req.json()
    return await search.semantic_search(body.get("query", ""), top_k=body.get("top_k", 8))
