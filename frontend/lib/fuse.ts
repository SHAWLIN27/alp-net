import Fuse from 'fuse.js';
import type { GraphNode } from '@/types';

let fuseInstance: Fuse<GraphNode> | null = null;

export function createFuseIndex(nodes: GraphNode[]): Fuse<GraphNode> {
  fuseInstance = new Fuse(nodes, {
    keys: ['label', 'description', 'category'],
    threshold: 0.3,
    includeScore: true,
    minMatchCharLength: 1,
  });
  return fuseInstance;
}

export function searchNodes(query: string): GraphNode[] {
  if (!fuseInstance || !query.trim()) return [];
  return fuseInstance.search(query).slice(0, 10).map(r => r.item);
}
