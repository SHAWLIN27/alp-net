"""Constants for node types, edge types, and visual encoding."""

# Node type constants
NODE_TYPE_TOPIC = "Topic"
NODE_TYPE_CONCEPT = "Concept"
NODE_TYPE_FORMULA = "Formula"
NODE_TYPE_EXAMPLE = "Example"
NODE_TYPE_EXPERIMENT = "Experiment"
NODE_TYPE_APPLICATION = "Application"
NODE_TYPE_MISCONCEPTION = "Misconception"

NODE_TYPES = [
    NODE_TYPE_TOPIC,
    NODE_TYPE_CONCEPT,
    NODE_TYPE_FORMULA,
    NODE_TYPE_EXAMPLE,
    NODE_TYPE_EXPERIMENT,
    NODE_TYPE_APPLICATION,
    NODE_TYPE_MISCONCEPTION,
]

# Edge / relationship type constants
EDGE_BELONGS_TO = "BELONGS_TO"
EDGE_PREREQUISITE_OF = "PREREQUISITE_OF"
EDGE_DERIVES_FROM = "DERIVES_FROM"
EDGE_APPLIES_TO = "APPLIES_TO"
EDGE_HAS_FORMULA = "HAS_FORMULA"
EDGE_HAS_EXAMPLE = "HAS_EXAMPLE"
EDGE_HAS_EXPERIMENT = "HAS_EXPERIMENT"
EDGE_RELATED_TO = "RELATED_TO"
EDGE_SUBTOPIC_OF = "SUBTOPIC_OF"
EDGE_HAS_MISCONCEPTION = "HAS_MISCONCEPTION"
EDGE_REQUIRES_MATH = "REQUIRES_MATH"
EDGE_CONTRASTS_WITH = "CONTRASTS_WITH"

EDGE_TYPES = [
    EDGE_BELONGS_TO,
    EDGE_PREREQUISITE_OF,
    EDGE_DERIVES_FROM,
    EDGE_APPLIES_TO,
    EDGE_HAS_FORMULA,
    EDGE_HAS_EXAMPLE,
    EDGE_HAS_EXPERIMENT,
    EDGE_RELATED_TO,
    EDGE_SUBTOPIC_OF,
    EDGE_HAS_MISCONCEPTION,
    EDGE_REQUIRES_MATH,
    EDGE_CONTRASTS_WITH,
]

# Physics domain -> color mapping (for frontend visualization)
DOMAIN_COLORS = {
    "mechanics": "#4A90D9",
    "waves": "#50B86C",
    "electricity": "#F5A623",
    "fields": "#9B59B6",
    "thermal": "#E74C3C",
    "nuclear": "#E67E22",
    "quantum": "#1ABC9C",
    "materials": "#E91E90",
    "astrophysics": "#34495E",
    "medical": "#C0392B",
    "math": "#7F8C8D",
    "practical": "#95A5A6",
}

# Edge type -> visual style
EDGE_STYLES = {
    EDGE_PREREQUISITE_OF: {"color": "#E74C3C", "style": "solid", "arrow": True},
    EDGE_DERIVES_FROM: {"color": "#9B59B6", "style": "solid", "arrow": True},
    EDGE_BELONGS_TO: {"color": "#7F8C8D", "style": "solid", "arrow": True},
    EDGE_SUBTOPIC_OF: {"color": "#7F8C8D", "style": "dashed", "arrow": True},
    EDGE_HAS_FORMULA: {"color": "#F5A623", "style": "solid", "arrow": True},
    EDGE_HAS_EXAMPLE: {"color": "#50B86C", "style": "solid", "arrow": True},
    EDGE_HAS_EXPERIMENT: {"color": "#1ABC9C", "style": "solid", "arrow": True},
    EDGE_APPLIES_TO: {"color": "#4A90D9", "style": "solid", "arrow": True},
    EDGE_RELATED_TO: {"color": "#95A5A6", "style": "dotted", "arrow": False},
    EDGE_REQUIRES_MATH: {"color": "#E67E22", "style": "dashed", "arrow": True},
    EDGE_HAS_MISCONCEPTION: {"color": "#E74C3C", "style": "dashed", "arrow": True},
    EDGE_CONTRASTS_WITH: {"color": "#C0392B", "style": "dotted", "arrow": False},
}

# Node type -> Cytoscape shape
NODE_SHAPES = {
    NODE_TYPE_TOPIC: "round-rectangle",
    NODE_TYPE_CONCEPT: "ellipse",
    NODE_TYPE_FORMULA: "diamond",
    NODE_TYPE_EXAMPLE: "rectangle",
    NODE_TYPE_EXPERIMENT: "triangle",
    NODE_TYPE_APPLICATION: "hexagon",
    NODE_TYPE_MISCONCEPTION: "vee",
}

# Difficulty -> border style
DIFFICULTY_STYLES = {
    "foundation": {"border-width": 1, "border-style": "solid"},
    "intermediate": {"border-width": 2, "border-style": "solid"},
    "advanced": {"border-width": 3, "border-style": "double"},
}
