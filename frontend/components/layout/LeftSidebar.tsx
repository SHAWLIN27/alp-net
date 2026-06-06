'use client';

import { useMemo, useState, useCallback } from 'react';
import { useGraphStore } from '@/store';
import { Atom, GitBranch, Layers, ChevronRight, Dot } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import type { GraphNode } from '@/types';
import { DOMAIN_COLORS, DOMAIN_LABELS } from '@/types';

// ── Tree data types ──
interface TreeNode {
  id: string;
  label: string;
  level: 'domain' | 'subdomain' | 'topic_hub' | 'leaf_concept';
  color: string;
  children: TreeNode[];
  nodeData: GraphNode | null;   // non-null for topic_hub & leaf_concept
  count: number;                 // total descendant nodes
}

// ── Helpers ──
function fmtIdPart(part: string): string {
  // "01-kinematics" → "Kinematics", "scalars-and-vectors" → "Scalars and Vectors"
  return part
    .replace(/^\d+-/, '')
    .replace(/-/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase())
    .trim();
}

function subdomainColor(domainColor: string): string {
  // Lighten the domain color for subdomain level
  return domainColor + 'CC';
}

function topicFolderColor(domainColor: string): string {
  return domainColor + '99';
}

// ── Build tree from flat node list ──
function buildTree(nodes: GraphNode[]): TreeNode[] {
  const domainMap = new Map<string, Map<string, Map<string, GraphNode[]>>>();

  for (const node of nodes) {
    const parts = node.id.split('--');
    if (parts.length < 2) continue;

    const domainKey = parts[0];
    const subdomainKey = parts[1];
    const topicKey = parts.length >= 3 ? parts.slice(2).join('--') : subdomainKey;

    // Determine if this node's topic key represents a hub or leaf
    // Topic hubs have nodeType === 'topic_hub', leaves have 'leaf_concept'
    // For tree purposes, we group by the topic folder (parts[2] or the hub name)

    if (!domainMap.has(domainKey)) {
      domainMap.set(domainKey, new Map());
    }
    const subMap = domainMap.get(domainKey)!;

    if (!subMap.has(subdomainKey)) {
      subMap.set(subdomainKey, new Map());
    }
    const topicMap = subMap.get(subdomainKey)!;

    // Use the topic folder name as key (for hubs) or the hub name extracted from the leaf
    let groupKey: string;
    if (node.nodeType === 'topic_hub') {
      groupKey = topicKey;
    } else {
      // Leaf concept — group under its parent topic hub
      // The topic hub name is parts[2] (the third segment)
      groupKey = parts.length >= 3 ? parts[2] : topicKey;
    }

    if (!topicMap.has(groupKey)) {
      topicMap.set(groupKey, []);
    }
    topicMap.get(groupKey)!.push(node);
  }

  // Convert maps to TreeNode[]
  const domainOrder = [
    '01-mechanics', '02-waves', '03-electricity', '04-fields',
    '05-thermal-physics', '06-nuclear-and-particle-physics',
    '07-quantum-physics', '08-materials', '09-astrophysics',
    '10-medical-physics', '11-mathematical-foundations', '12-practical-skills',
  ];

  const result: TreeNode[] = [];

  for (const [domainKey, subMap] of domainMap) {
    const domainLabel = DOMAIN_LABELS[domainKey] || fmtIdPart(domainKey);
    const domainColor = DOMAIN_COLORS[domainKey] || '#38BDF8';
    const domainChildren: TreeNode[] = [];

    for (const [subKey, topicMap] of subMap) {
      const subLabel = fmtIdPart(subKey);
      const subChildren: TreeNode[] = [];

      for (const [topicKey, topicNodes] of topicMap) {
        const topicLabel = fmtIdPart(topicKey);
        const topicChildren: TreeNode[] = [];

        // Separate hub from leaves
        const hub = topicNodes.find(n => n.nodeType === 'topic_hub');
        const leaves = topicNodes.filter(n => n.nodeType === 'leaf_concept');

        // Create leaf nodes
        for (const leaf of leaves) {
          topicChildren.push({
            id: leaf.id,
            label: leaf.label,
            level: 'leaf_concept' as const,
            color: leaf.color,
            children: [],
            nodeData: leaf,
            count: 0,
          });
        }

        // Create topic hub node
        const hubNode: TreeNode = {
          id: hub?.id || topicKey,
          label: hub?.label || topicLabel,
          level: 'topic_hub' as const,
          color: hub?.color || topicFolderColor(domainColor),
          children: topicChildren,
          nodeData: hub || null,
          count: topicChildren.length,
        };
        subChildren.push(hubNode);
      }

      const subNode: TreeNode = {
        id: `${domainKey}--${subKey}`,
        label: subLabel,
        level: 'subdomain' as const,
        color: subdomainColor(domainColor),
        children: subChildren,
        nodeData: null,
        count: subChildren.reduce((s, c) => s + 1 + c.count, 0),
      };
      domainChildren.push(subNode);
    }

    const domainNode: TreeNode = {
      id: domainKey,
      label: domainLabel,
      level: 'domain' as const,
      color: domainColor,
      children: domainChildren,
      nodeData: null,
      count: domainChildren.reduce((s, c) => s + c.count, 0),
    };
    result.push(domainNode);
  }

  // Sort by domain order
  result.sort((a, b) => {
    const ai = domainOrder.indexOf(a.id);
    const bi = domainOrder.indexOf(b.id);
    if (ai >= 0 && bi >= 0) return ai - bi;
    if (ai >= 0) return -1;
    if (bi >= 0) return 1;
    return a.label.localeCompare(b.label);
  });

  return result;
}

// ── Recursive tree node component ──
function TreeNodeItem({
  node,
  depth,
  onSelect,
}: {
  node: TreeNode;
  depth: number;
  onSelect: (n: GraphNode) => void;
}) {
  const [expanded, setExpanded] = useState(depth < 2); // auto-expand first 2 levels
  const hasChildren = node.children.length > 0;
  const isClickable = node.nodeData !== null;

  const handleClick = () => {
    if (hasChildren) {
      setExpanded(!expanded);
    }
    if (isClickable && node.nodeData) {
      onSelect(node.nodeData);
    }
  };

  const dotSize = node.level === 'domain' ? 'w-2 h-2' :
    node.level === 'subdomain' ? 'w-1.5 h-1.5' :
    node.level === 'topic_hub' ? 'w-2 h-2' : 'w-1.5 h-1.5';

  const textSize = node.level === 'domain' ? 'text-[11px] font-semibold' :
    node.level === 'subdomain' ? 'text-[10.5px] font-medium' :
    node.level === 'topic_hub' ? 'text-[10.5px] font-medium' : 'text-[10px]';

  const textOpacity = node.level === 'leaf_concept' ? 'text-slate-400' :
    node.level === 'topic_hub' ? 'text-slate-300' : 'text-slate-200';

  return (
    <div className="select-none">
      <button
        onClick={handleClick}
        className="w-full flex items-center gap-1.5 py-1 px-1.5 rounded-md text-left transition-all duration-150 hover:bg-white/[0.04] group"
        style={{ paddingLeft: `${depth * 14 + 6}px` }}
      >
        {/* Expand/collapse chevron */}
        <span className="w-3.5 flex-shrink-0 flex items-center justify-center">
          {hasChildren ? (
            <motion.span
              animate={{ rotate: expanded ? 90 : 0 }}
              transition={{ duration: 0.15 }}
              className="text-slate-600"
            >
              <ChevronRight className="w-3 h-3" />
            </motion.span>
          ) : (
            <Dot className="w-3 h-3 text-slate-700" />
          )}
        </span>

        {/* Color dot */}
        <span
          className={`${dotSize} rounded-full flex-shrink-0`}
          style={{
            backgroundColor: node.color,
            boxShadow: node.level === 'domain' || node.level === 'topic_hub'
              ? `0 0 6px ${node.color}`
              : 'none',
          }}
        />

        {/* Label */}
        <span className={`${textSize} ${textOpacity} truncate flex-1 leading-tight group-hover:text-white transition-colors`}>
          {node.label}
        </span>

        {/* Count badge */}
        {node.count > 0 && (
          <span className="text-[9px] text-slate-600 tabular-nums flex-shrink-0">
            {node.count}
          </span>
        )}
      </button>

      {/* Children */}
      <AnimatePresence>
        {expanded && hasChildren && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2, ease: 'easeInOut' }}
            style={{ overflow: 'hidden' }}
          >
            {node.children.map(child => (
              <TreeNodeItem
                key={child.id}
                node={child}
                depth={depth + 1}
                onSelect={onSelect}
              />
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

// ── Main sidebar component ──
export default function LeftSidebar() {
  const { nodes, edges, selectNode, focusNode } = useGraphStore();

  const totalNodes = nodes.length;
  const totalEdges = edges.length;

  const tree = useMemo(() => buildTree(nodes), [nodes]);
  const totalDomains = tree.length;

  const handleSelect = useCallback((node: GraphNode) => {
    selectNode(node);
    focusNode(node.id);
  }, [selectNode, focusNode]);

  return (
    <motion.aside
      initial={{ x: -320, opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      transition={{ duration: 0.6, ease: 'easeOut' }}
      className="fixed left-4 top-4 bottom-4 w-60 z-30 flex flex-col gap-3 pointer-events-none"
    >
      {/* ── Logo + Stats ── */}
      <div className="pointer-events-auto rounded-2xl border border-white/[0.06] bg-[#020617]/85 backdrop-blur-2xl px-4 py-3.5">
        <div className="flex items-center gap-2.5 mb-3">
          <div className="w-7 h-7 rounded-lg bg-gradient-to-br from-[#38BDF8] to-[#A855F7] flex items-center justify-center flex-shrink-0">
            <Atom className="w-4 h-4 text-white" />
          </div>
          <div>
            <h1 className="text-xs font-bold text-white tracking-wide leading-none">ALP_NET</h1>
            <p className="text-[9px] text-slate-500 tracking-widest uppercase leading-none mt-0.5">Universe</p>
          </div>
        </div>

        <div className="grid grid-cols-3 gap-1.5">
          <MiniStat icon={<Atom className="w-3 h-3" />} value={totalNodes} label="Nodes" />
          <MiniStat icon={<GitBranch className="w-3 h-3" />} value={totalEdges} label="Edges" />
          <MiniStat icon={<Layers className="w-3 h-3" />} value={totalDomains} label="Domains" />
        </div>
      </div>

      {/* ── Tree view ── */}
      <div className="pointer-events-auto flex-1 overflow-y-auto rounded-2xl border border-white/[0.06] bg-[#020617]/85 backdrop-blur-2xl py-3">
        <div className="px-3 mb-2">
          <h3 className="text-[10px] font-semibold text-slate-500 uppercase tracking-widest">
            Knowledge Tree
          </h3>
        </div>

        {tree.map(domain => (
          <TreeNodeItem
            key={domain.id}
            node={domain}
            depth={0}
            onSelect={handleSelect}
          />
        ))}

        {tree.length === 0 && (
          <p className="px-3 py-4 text-[10px] text-slate-600 text-center">
            Loading tree...
          </p>
        )}
      </div>

      {/* ── Footer ── */}
      <div className="pointer-events-auto text-center">
        <p className="text-[9px] text-slate-600">CAIE 9702 · Edexcel IAL</p>
      </div>
    </motion.aside>
  );
}

// ── Mini stat box ──
function MiniStat({ icon, value, label }: { icon: React.ReactNode; value: number; label: string }) {
  return (
    <div className="flex flex-col items-center gap-0.5 p-1.5 rounded-lg bg-white/[0.03] border border-white/[0.04]">
      <div className="text-slate-500">{icon}</div>
      <span className="text-xs font-bold text-white tabular-nums leading-none">{value}</span>
      <span className="text-[8px] text-slate-500 uppercase tracking-wider leading-none">{label}</span>
    </div>
  );
}
