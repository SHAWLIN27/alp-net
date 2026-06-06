from fastapi import APIRouter, Depends, HTTPException, Query

from alpnet.api.dependencies import get_graph_service
from alpnet.models.api import GraphResponse
from alpnet.models.nodes import KnowledgeNode
from alpnet.services.graph_service import GraphService

router = APIRouter(prefix="/graph", tags=["graph"])


@router.get("/topics", response_model=GraphResponse)
def get_topics(graph: GraphService = Depends(get_graph_service)) -> GraphResponse:
    return graph.topic_tree()


@router.get("/concepts/{concept_id}", response_model=KnowledgeNode)
def get_concept(concept_id: str, graph: GraphService = Depends(get_graph_service)) -> KnowledgeNode:
    node = graph.get_node(concept_id)
    if node is None:
        raise HTTPException(status_code=404, detail="Concept not found")
    return node


@router.get("/concepts/{concept_id}/neighborhood", response_model=GraphResponse)
def get_neighborhood(
    concept_id: str,
    depth: int = Query(default=1, ge=1, le=4),
    graph: GraphService = Depends(get_graph_service),
) -> GraphResponse:
    return graph.get_neighborhood(concept_id, depth=depth)


@router.get("/path", response_model=GraphResponse)
def get_path(
    source: str = Query(alias="from"),
    target: str = Query(alias="to"),
    graph: GraphService = Depends(get_graph_service),
) -> GraphResponse:
    return graph.shortest_path(source, target)
