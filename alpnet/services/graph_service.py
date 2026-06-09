from collections import deque

import networkx as nx

from alpnet.config.settings import Settings
from alpnet.db.graph_store import GraphStore
from alpnet.models.api import GraphResponse
from alpnet.models.nodes import KnowledgeEdge, KnowledgeNode


class GraphService:
    def __init__(self, settings: Settings):
        self.store = GraphStore(settings.graph_path)
        self.graph = self.store.load()

    def reload(self) -> None:
        self.graph = self.store.load()

    def stats(self) -> dict[str, int]:
        return {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges(),
        }

    def all_nodes(self) -> list[KnowledgeNode]:
        return [KnowledgeNode(**data) for _, data in self.graph.nodes(data=True)]

    def get_node(self, node_id: str) -> KnowledgeNode | None:
        if node_id not in self.graph:
            return None
        return KnowledgeNode(**self.graph.nodes[node_id])

    def get_neighborhood(self, node_id: str, depth: int = 1) -> GraphResponse:
        if node_id not in self.graph:
            return GraphResponse()

        visited = {node_id}
        queue: deque[tuple[str, int]] = deque([(node_id, 0)])

        while queue:
            current, distance = queue.popleft()
            if distance >= depth:
                continue
            neighbors = set(self.graph.successors(current)) | set(self.graph.predecessors(current))
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return self._subgraph_response(self.graph.subgraph(visited))

    def shortest_path(self, source: str, target: str) -> GraphResponse:
        if source not in self.graph or target not in self.graph:
            return GraphResponse()
        try:
            path = nx.shortest_path(self.graph.to_undirected(), source=source, target=target)
        except nx.NetworkXNoPath:
            return GraphResponse()
        return self._subgraph_response(self.graph.subgraph(path))

    def _subgraph_response(self, graph: nx.MultiDiGraph, exclude_content: bool = False) -> GraphResponse:
        nodes: list[KnowledgeNode] = []
        for _, data in graph.nodes(data=True):
            node_data = dict(data)
            if exclude_content:
                node_data.pop("content_md", None)
            nodes.append(KnowledgeNode(**node_data))
        edges: list[KnowledgeEdge] = []
        for source, target, data in graph.edges(data=True):
            edges.append(KnowledgeEdge(**data))
        return GraphResponse(nodes=nodes, edges=edges)

    def topic_tree(self) -> GraphResponse:
        topic_nodes = [
            node_id
            for node_id, data in self.graph.nodes(data=True)
            if data.get("node_type") == "Topic"
        ]
        expanded = set(topic_nodes)
        for topic_id in topic_nodes:
            expanded.update(self.graph.predecessors(topic_id))
        return self._subgraph_response(self.graph.subgraph(expanded), exclude_content=True)
