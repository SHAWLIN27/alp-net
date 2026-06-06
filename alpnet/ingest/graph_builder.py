"""
Graph Builder — converts ParsedFile objects into KnowledgeNode + KnowledgeEdge objects
and persists them to the GraphStore.
"""
import uuid

from alpnet.ingest.parser import ParsedFile
from alpnet.ingest.resolver import WikilinkResolver
from alpnet.models.nodes import (
    KnowledgeNode, KnowledgeEdge, GraphData,
    NodeType, EdgeType, Difficulty,
)


class GraphBuilder:
    """Builds the knowledge graph from parsed vault files."""

    def __init__(self, parsed_files: list[ParsedFile]):
        self.parsed = parsed_files

    def build(self) -> GraphData:
        """Build complete GraphData with nodes and edges."""
        nodes = self._build_nodes()
        edges = self._build_edges()
        return GraphData(nodes=nodes, edges=edges)

    def _build_nodes(self) -> list[KnowledgeNode]:
        """Convert each ParsedFile into a KnowledgeNode."""
        nodes = []
        for pf in self.parsed:
            node_type = self._map_node_type(pf.node_type)
            difficulty = self._map_difficulty(pf.difficulty)

            # Normalize syllabus field — some generated YAML has malformed values
            safe_syllabus = []
            for s in pf.syllabus:
                if isinstance(s, dict):
                    safe_syllabus.append(str(s))
                elif isinstance(s, str):
                    safe_syllabus.append(s)
                else:
                    safe_syllabus.append(str(s))

            node = KnowledgeNode(
                id=pf.node_id,
                name=pf.name,
                node_type=node_type,
                definition=self._extract_definition(pf),
                content_md=pf.content_md,
                domain=pf.domain,
                difficulty=difficulty,
                tags=pf.tags,
                syllabus=safe_syllabus,
                cie_ref=pf.metadata.get("cie_ref"),
                edexcel_ref=pf.metadata.get("edexcel_ref"),
                source_file=str(pf.file_path),
                metadata={
                    "node_type_detail": pf.node_type,
                    "level": pf.level,
                    "topic_folder": pf.topic_folder or "",
                    "name_cn": pf.name_cn,
                    "section_count": len(pf.sections),
                    "wikilink_count": len(pf.wikilinks),
                },
            )
            nodes.append(node)

        return nodes

    def _build_edges(self) -> list[KnowledgeEdge]:
        """Resolve wikilinks into edges."""
        resolver = WikilinkResolver(self.parsed)
        return resolver.resolve()

    @staticmethod
    def _map_node_type(nt: str) -> NodeType:
        mapping = {
            "topic_hub": NodeType.topic,
            "leaf_concept": NodeType.concept,
            "subdomain_index": NodeType.topic,
        }
        return mapping.get(nt, NodeType.concept)

    @staticmethod
    def _map_difficulty(d: str) -> Difficulty:
        mapping = {
            "foundation": Difficulty.foundation,
            "intermediate": Difficulty.intermediate,
            "advanced": Difficulty.advanced,
        }
        return mapping.get(d, Difficulty.foundation)

    @staticmethod
    def _extract_definition(pf: ParsedFile) -> str:
        """Extract a short definition from Section 3 (Core Definitions) if available."""
        section3 = pf.sections.get(3, "")
        if not section3:
            section1 = pf.sections.get(1, "")
            # Take first meaningful sentence from overview
            lines = section1.split("\n")
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#") and len(line) > 30:
                    return line[:300]
            return ""
        # Take first definition row
        return section3[:300]
