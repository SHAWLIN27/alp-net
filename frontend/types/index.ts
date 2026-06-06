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
  "01-Kinematics":     "#38BDF8",
  "02-Forces":         "#22D3EE",
  "03-Work-Energy-Power": "#10B981",
  "04-Circular-Motion":   "#A855F7",
  "05-Gravitational-Fields": "#F59E0B",
  "06-Oscillations":   "#EC4899",
};

export const DOMAIN_LABELS: Record<string, string> = {
  "01-Kinematics":     "Kinematics",
  "02-Forces":         "Forces",
  "03-Work-Energy-Power": "Work, Energy & Power",
  "04-Circular-Motion":   "Circular Motion",
  "05-Gravitational-Fields": "Gravitational Fields",
  "06-Oscillations":   "Oscillations",
};

export function getDomainColor(domain: string): string {
  return DOMAIN_COLORS[domain] || "#38BDF8";
}

export function getDomainLabel(domain: string): string {
  return DOMAIN_LABELS[domain] || domain;
}
