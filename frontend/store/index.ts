import { create } from 'zustand';
import type { GraphNode, GraphEdge, DomainStat } from '@/types';
import { DOMAIN_COLORS, DOMAIN_LABELS } from '@/types';

interface GraphState {
  // Data
  nodes: GraphNode[];
  edges: GraphEdge[];
  domainStats: DomainStat[];

  // UI State
  selectedNode: GraphNode | null;
  hoveredNode: string | null;
  searchQuery: string;
  searchResults: GraphNode[];
  activeDomains: Set<string>;
  rightPanelOpen: boolean;
  isLoading: boolean;
  focusNodeId: string | null;   // external trigger for 3D camera focus

  // Actions
  setGraphData: (nodes: GraphNode[], edges: GraphEdge[]) => void;
  selectNode: (node: GraphNode | null) => void;
  focusNode: (nodeId: string | null) => void;
  hoverNode: (nodeId: string | null) => void;
  setSearchQuery: (query: string) => void;
  toggleDomain: (domain: string) => void;
  setRightPanelOpen: (open: boolean) => void;
  setLoading: (loading: boolean) => void;
  computeDomainStats: () => void;
  getFilteredGraph: () => { nodes: GraphNode[]; edges: GraphEdge[] };
}

export const useGraphStore = create<GraphState>((set, get) => ({
  nodes: [],
  edges: [],
  domainStats: [],
  selectedNode: null,
  hoveredNode: null,
  searchQuery: '',
  searchResults: [],
  activeDomains: new Set(),
  rightPanelOpen: false,
  isLoading: true,
  focusNodeId: null,

  setGraphData: (nodes, edges) => {
    set({ nodes, edges });
    get().computeDomainStats();
  },

  selectNode: (node) => set({ selectedNode: node, rightPanelOpen: !!node }),

  focusNode: (nodeId) => set({ focusNodeId: nodeId }),

  hoverNode: (nodeId) => set({ hoveredNode: nodeId }),

  setSearchQuery: (query) => set({ searchQuery: query }),

  toggleDomain: (domain) => {
    const domains = new Set(get().activeDomains);
    if (domains.has(domain)) domains.delete(domain);
    else domains.add(domain);
    set({ activeDomains: domains });
  },

  setRightPanelOpen: (open) => set({ rightPanelOpen: open }),

  setLoading: (loading) => set({ isLoading: loading }),

  computeDomainStats: () => {
    const { nodes } = get();
    const domainMap = new Map<string, { count: number; label: string; color: string }>();

    for (const n of nodes) {
      const domain = n.category || 'unknown';
      if (!domainMap.has(domain)) {
        domainMap.set(domain, {
          count: 0,
          label: DOMAIN_LABELS[domain] || domain,
          color: DOMAIN_COLORS[domain] || '#666',
        });
      }
      domainMap.get(domain)!.count++;
    }

    const stats: DomainStat[] = Array.from(domainMap.entries()).map(
      ([name, { count, label, color }]) => ({
        name,
        label,
        color,
        nodeCount: count,
        edgeCount: 0,
      })
    );

    set({ domainStats: stats });
  },

  getFilteredGraph: () => {
    const { nodes, edges, activeDomains } = get();
    if (activeDomains.size === 0) return { nodes, edges };

    const filteredNodes = nodes.filter(n => activeDomains.has(n.category));
    const filteredNodeIds = new Set(filteredNodes.map(n => n.id));
    const filteredEdges = edges.filter(
      e => filteredNodeIds.has(e.source) && filteredNodeIds.has(e.target)
    );

    return { nodes: filteredNodes, edges: filteredEdges };
  },
}));
