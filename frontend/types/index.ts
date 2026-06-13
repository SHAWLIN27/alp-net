export interface GraphNode {
  id: string;
  label: string;
  category: string;       // domain: "01-Kinematics", "02-Forces", etc.
  description: string;
  size: number;
  color: string;
  nodeType: 'topic_hub' | 'leaf_concept';
  x?: number;
  y?: number;
}

export interface GraphEdge {
  source: string;
  target: string;
  relation: string;       // "RELATED_TO", "SUBTOPIC_OF", "PREREQUISITE_OF"
}

export interface ApiGraphData {
  nodes: {
    id: string;
    name: string;
    node_type: string;
    domain: string;
    definition: string;
    difficulty: string;
    metadata: Record<string, unknown>;
  }[];
  edges: {
    source: string;
    target: string;
    edge_type: string;
    label: string;
  }[];
}

export interface SearchResult {
  id: string;
  title: string;
  content: string;
  score: number;
  source_file: string | null;
  metadata: Record<string, string>;
}

export interface DomainStat {
  name: string;
  label: string;
  color: string;
  nodeCount: number;
  edgeCount: number;
}

export const DOMAIN_COLORS: Record<string, string> = {
  "01-mechanics":                   "#38BDF8",  // Blue
  "02-waves":                       "#EC4899",  // Pink
  "03-electricity":                 "#10B981",  // Green
  "04-fields":                      "#A855F7",  // Purple
  "05-thermal-physics":             "#F59E0B",  // Orange
  "06-nuclear-and-particle-physics":"#EF4444",  // Red
  "07-quantum-physics":             "#8B5CF6",  // Violet
  "08-materials":                   "#14B8A6",  // Teal
  "09-astrophysics":                "#6366F1",  // Indigo
  "10-medical-physics":             "#F97316",  // Deep Orange
  "11-mathematical-foundations":    "#06B6D4",  // Cyan
  "12-practical-skills":            "#84CC16",  // Lime
};

export const DOMAIN_LABELS: Record<string, string> = {
  "01-mechanics":                   "Mechanics",
  "02-waves":                       "Waves",
  "03-electricity":                 "Electricity",
  "04-fields":                      "Fields",
  "05-thermal-physics":             "Thermal Physics",
  "06-nuclear-and-particle-physics":"Nuclear & Particle Physics",
  "07-quantum-physics":             "Quantum Physics",
  "08-materials":                   "Materials",
  "09-astrophysics":                "Astrophysics",
  "10-medical-physics":             "Medical Physics",
  "11-mathematical-foundations":    "Math Foundations",
  "12-practical-skills":            "Practical Skills",
};

export function getDomainColor(domain: string): string {
  return DOMAIN_COLORS[domain] || "#38BDF8";
}

export function getDomainLabel(domain: string): string {
  return DOMAIN_LABELS[domain] || domain;
}
