import json
from pathlib import Path

import networkx as nx
from networkx.readwrite import json_graph

from alpnet.models.nodes import KnowledgeEdge, KnowledgeNode


class GraphStore:
    def __init__(self, graph_path: Path):
        self.graph_path = graph_path
        self.graph = nx.MultiDiGraph()

    def load(self) -> nx.MultiDiGraph:
        if not self.graph_path.exists():
            self.graph = nx.MultiDiGraph()
            return self.graph

        with self.graph_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        self.graph = json_graph.node_link_graph(data, directed=True, multigraph=True)
        # Ensure all nodes have their id in attributes for Pydantic deserialization
        for node_id in list(self.graph.nodes()):
            self.graph.nodes[node_id]["id"] = node_id
        # Ensure all edges have source/target in attributes
        for u, v, key in list(self.graph.edges(keys=True)):
            self.graph.edges[u, v, key]["source"] = u
            self.graph.edges[u, v, key]["target"] = v
        return self.graph

    def save(self) -> None:
        self.graph_path.parent.mkdir(parents=True, exist_ok=True)
        data = json_graph.node_link_data(self.graph)
        with self.graph_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def upsert_node(self, node: KnowledgeNode) -> None:
        data = node.model_dump()
        data["id"] = node.id  # ensure id is in attributes for deserialization
        self.graph.add_node(node.id, **data)

    def upsert_edge(self, edge: KnowledgeEdge) -> None:
        self.graph.add_edge(
            edge.source,
            edge.target,
            key=edge.edge_type.value,
            **edge.model_dump(),
        )

    def stats(self) -> dict[str, int]:
        return {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges(),
        }
