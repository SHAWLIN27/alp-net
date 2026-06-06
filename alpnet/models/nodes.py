from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Difficulty(str, Enum):
    foundation = "foundation"
    intermediate = "intermediate"
    advanced = "advanced"


class NodeType(str, Enum):
    topic = "Topic"
    concept = "Concept"
    formula = "Formula"
    example = "Example"
    experiment = "Experiment"
    application = "Application"
    misconception = "Misconception"


class EdgeType(str, Enum):
    belongs_to = "BELONGS_TO"
    prerequisite_of = "PREREQUISITE_OF"
    derives_from = "DERIVES_FROM"
    applies_to = "APPLIES_TO"
    has_formula = "HAS_FORMULA"
    has_example = "HAS_EXAMPLE"
    has_experiment = "HAS_EXPERIMENT"
    related_to = "RELATED_TO"
    subtopic_of = "SUBTOPIC_OF"
    has_misconception = "HAS_MISCONCEPTION"
    requires_math = "REQUIRES_MATH"
    contrasts_with = "CONTRASTS_WITH"


class KnowledgeNode(BaseModel):
    id: str
    name: str
    node_type: NodeType = NodeType.concept
    definition: str = ""
    content_md: str = ""
    domain: str = ""
    difficulty: Difficulty = Difficulty.foundation
    tags: list[str] = Field(default_factory=list)
    syllabus: list[str] = Field(default_factory=list)
    cie_ref: str | None = None
    edexcel_ref: str | None = None
    source_file: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class KnowledgeEdge(BaseModel):
    source: str
    target: str
    edge_type: EdgeType
    label: str | None = None
    weight: float = 1.0
    metadata: dict[str, Any] = Field(default_factory=dict)


class GraphData(BaseModel):
    nodes: list[KnowledgeNode] = Field(default_factory=list)
    edges: list[KnowledgeEdge] = Field(default_factory=list)
