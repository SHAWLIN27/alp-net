"""
Wikilink Resolver — resolves [[wikilinks]] from parsed files into KnowledgeEdge objects.

Strategy:
- Build a lookup table: display_name → node_id (from all ParsedFiles)
- For each wikilink in each file, find the best-matching target node
- Determine edge type based on relationship context:
  - leaf → its own hub → SUBTOPIC_OF
  - link to a prerequisite topic → PREREQUISITE_OF
  - link to a related topic → RELATED_TO
"""
import re
from collections import defaultdict

from alpnet.ingest.parser import ParsedFile
from alpnet.models.nodes import KnowledgeEdge, EdgeType


class WikilinkResolver:
    """Resolves [[wikilinks]] to KnowledgeEdge objects."""

    def __init__(self, parsed_files: list[ParsedFile]):
        self.parsed = parsed_files
        # Build lookup: all possible display names → node_id
        self.name_to_id: dict[str, str] = {}
        self._build_lookup()

    def _build_lookup(self) -> None:
        """Build a comprehensive name → node_id lookup from all parsed files."""
        for pf in self.parsed:
            # Primary: by node_id (normalized)
            self.name_to_id[pf.node_id.lower()] = pf.node_id
            # By display name
            self.name_to_id[pf.name.lower()] = pf.node_id
            # By file stem (without extension)
            stem = pf.file_path.stem.lower()
            self.name_to_id[stem] = pf.node_id
            # By name without spaces
            no_space = pf.name.replace(" ", "").lower()
            self.name_to_id[no_space] = pf.node_id
            # By Chinese name if present
            if pf.name_cn:
                self.name_to_id[pf.name_cn.strip().lower()] = pf.node_id
            # By topic folder
            if pf.topic_folder:
                self.name_to_id[pf.topic_folder.lower()] = pf.node_id

        # Also add common abbreviations and variants
        extra_aliases = {
            "newton's laws of motion": "newtons-laws-of-motion",
            "newtons laws": "newtons-laws-of-motion",
            "newton's laws": "newtons-laws-of-motion",
            "free body diagrams": "free-body-diagrams",
            "freebody diagrams": "free-body-diagrams",
            "suvat": "equations-of-motion-(suvat)",
            "equations of motion": "equations-of-motion-(suvat)",
            "shm": "simple-harmonic-motion",
            "ke": "kinetic-energy-(ke)",
            "gpe": "gravitational-potential-energy-(gpe)",
            "terminal velocity": "terminal-velocity",
            "projectile motion": "projectile-motion",
        }
        for alias, target in extra_aliases.items():
            if alias not in self.name_to_id and target in self.name_to_id:
                self.name_to_id[alias] = self.name_to_id[target]

    def resolve(self) -> list[KnowledgeEdge]:
        """Resolve all wikilinks from all files into KnowledgeEdge objects."""
        edges: list[KnowledgeEdge] = []
        seen_edges = set()

        for pf in self.parsed:
            source_id = pf.node_id

            for wl in pf.wikilinks:
                target_id = self._find_target(wl["target"])
                if not target_id or target_id == source_id:
                    continue  # self-link or unresolvable

                edge_type = self._determine_edge_type(pf, target_id)

                edge_key = (source_id, target_id, edge_type.value)
                if edge_key in seen_edges:
                    continue
                seen_edges.add(edge_key)

                edges.append(KnowledgeEdge(
                    source=source_id,
                    target=target_id,
                    edge_type=edge_type,
                    label=wl.get("alias", wl["target"]),
                    weight=1.0,
                    metadata={
                        "wikilink_target": wl["target"],
                        "section": wl.get("section", 0),
                    },
                ))

        # Also create BELONGS_TO edges: leaf_concept → topic_hub (by folder structure)
        for pf in self.parsed:
            if pf.node_type == "leaf_concept" and pf.topic_folder:
                hub_id = self._find_target(pf.topic_folder)
                if hub_id:
                    edge_key = (pf.node_id, hub_id, "SUBTOPIC_OF")
                    if edge_key not in seen_edges:
                        edges.append(KnowledgeEdge(
                            source=pf.node_id,
                            target=hub_id,
                            edge_type=EdgeType.subtopic_of,
                            label=f"Sub-topic of {pf.topic_folder}",
                            weight=1.0,
                        ))

        return edges

    def _find_target(self, target: str) -> str | None:
        """Find the node_id for a wikilink target string."""
        target_clean = target.strip()
        # Exact match
        if target_clean.lower() in self.name_to_id:
            return self.name_to_id[target_clean.lower()]
        # Try without special chars
        normalized = re.sub(r'[^\w\s-]', '', target_clean).strip().lower()
        if normalized in self.name_to_id:
            return self.name_to_id[normalized]
        # Try without spaces
        no_space = target_clean.replace(" ", "").lower()
        if no_space in self.name_to_id:
            return self.name_to_id[no_space]
        # Fuzzy: check if any key contains this target
        for key, nid in self.name_to_id.items():
            if target_clean.lower() in key or key in target_clean.lower():
                return nid
        return None

    @staticmethod
    def _determine_edge_type(source: ParsedFile, target_id: str) -> EdgeType:
        """Determine the edge type based on the relationship between nodes."""
        # Check if target is a prerequisite of source
        for prereq in source.metadata.get("prerequisites", []):
            prereq_norm = prereq.replace(" ", "").lower()
            if prereq_norm in target_id.lower() or target_id.lower() in prereq_norm:
                return EdgeType.prerequisite_of

        # Check if target is a related topic
        for related in source.metadata.get("related_topics", []):
            related_norm = related.replace(" ", "").lower()
            if related_norm in target_id.lower() or target_id.lower() in related_norm:
                return EdgeType.related_to

        # Default: related_to
        return EdgeType.related_to
