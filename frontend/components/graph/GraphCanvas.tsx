'use client';

import { useEffect, useRef, useCallback } from 'react';
import ForceGraph3D from '3d-force-graph';
import * as THREE from 'three';
import { useGraphStore } from '@/store';
import { fetchGraphData, fetchNodeNeighborhood } from '@/lib/api';

// ── Types ──
interface GraphNode {
  id: string;
  name: string;
  domain: string;
  color: string;
  size: number;
  nodeType: string;
}
interface GraphLink {
  source: string;
  target: string;
  relation: string;
}
interface GraphData {
  nodes: GraphNode[];
  links: GraphLink[];
}

// ── API → 3D format ──
const DOMAIN_COLORS: Record<string, string> = {
  '01-Kinematics': '#38BDF8',
  '02-Forces': '#22D3EE',
  '03-Work-Energy-Power': '#10B981',
  '04-Circular-Motion': '#A855F7',
  '05-Gravitational-Fields': '#F59E0B',
  '06-Oscillations': '#EC4899',
};

function apiToGraphData(data: {
  nodes: { id: string; name: string; domain: string; node_type: string; metadata?: Record<string, unknown> }[];
  edges: { source: string; target: string; edge_type: string }[];
}): GraphData {
  const nodes: GraphNode[] = data.nodes.map(n => ({
    id: n.id,
    name: n.name,
    domain: n.domain || 'unknown',
    color: DOMAIN_COLORS[n.domain] || '#38BDF8',
    size: n.node_type === 'Topic' ? 5 : 2.5,
    nodeType: n.node_type === 'Topic' ? 'topic_hub' : 'leaf_concept',
  }));

  const links: GraphLink[] = data.edges.map(e => ({
    source: e.source,
    target: e.target,
    relation: e.edge_type || 'RELATED_TO',
  }));

  return { nodes, links };
}

// ── Glow texture generator ──
const glowTextureCache = new Map<string, THREE.Texture>();

function getGlowTexture(colorHex: string): THREE.Texture {
  const cached = glowTextureCache.get(colorHex);
  if (cached) return cached;

  const size = 128;
  const canvas = document.createElement('canvas');
  canvas.width = size;
  canvas.height = size;
  const ctx = canvas.getContext('2d')!;

  const half = size / 2;
  const gradient = ctx.createRadialGradient(half, half, 0, half, half, half);
  gradient.addColorStop(0, colorHex);
  gradient.addColorStop(0.15, colorHex);
  gradient.addColorStop(0.4, colorHex + '66');
  gradient.addColorStop(0.7, colorHex + '11');
  gradient.addColorStop(1, 'transparent');

  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, size, size);

  const tex = new THREE.CanvasTexture(canvas);
  tex.needsUpdate = true;
  glowTextureCache.set(colorHex, tex);
  return tex;
}

// ── Sci‑fi node builder ──
function buildNodeObject(node: GraphNode): THREE.Group {
  const group = new THREE.Group();
  const color = new THREE.Color(node.color);
  const isHub = node.nodeType === 'topic_hub';
  const radius = isHub ? 2.0 : 1.0;

  // ── Core sphere ──
  const sphereGeo = new THREE.SphereGeometry(radius, 32, 32);
  const sphereMat = new THREE.MeshStandardMaterial({
    color,
    emissive: color,
    emissiveIntensity: 0.55,
    roughness: 0.25,
    metalness: 0.15,
  });
  const sphere = new THREE.Mesh(sphereGeo, sphereMat);
  group.add(sphere);

  // ── Outer glow sprite ──
  const glowTex = getGlowTexture(node.color);
  const spriteMat = new THREE.SpriteMaterial({
    map: glowTex,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
    depthTest: true,
    opacity: 0.55,
    transparent: true,
  });
  const glowSprite = new THREE.Sprite(spriteMat);
  const glowScale = radius * 7;
  glowSprite.scale.set(glowScale, glowScale, 1);
  group.add(glowSprite);

  // ── Ring (topic hubs only) ──
  if (isHub) {
    const ringGeo = new THREE.TorusGeometry(radius * 1.7, 0.06, 16, 80);
    const ringMat = new THREE.MeshStandardMaterial({
      color,
      emissive: color,
      emissiveIntensity: 0.9,
      roughness: 0.1,
      metalness: 0.4,
      transparent: true,
      opacity: 0.85,
    });
    const ring = new THREE.Mesh(ringGeo, ringMat);
    ring.rotation.x = Math.PI / 2.4;
    ring.rotation.y = Math.PI / 6;
    group.add(ring);

    // Second thinner ring at a different angle
    const ring2Geo = new THREE.TorusGeometry(radius * 1.9, 0.04, 12, 64);
    const ring2Mat = new THREE.MeshStandardMaterial({
      color,
      emissive: color,
      emissiveIntensity: 0.7,
      roughness: 0.15,
      metalness: 0.3,
      transparent: true,
      opacity: 0.65,
    });
    const ring2 = new THREE.Mesh(ring2Geo, ring2Mat);
    ring2.rotation.x = Math.PI / 1.6;
    ring2.rotation.y = -Math.PI / 5;
    group.add(ring2);
  }

  return group;
}

// ── Component ──
export default function GraphCanvas() {
  const containerRef = useRef<HTMLDivElement>(null);
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const graphRef = useRef<any>(null);
  const graphDataRef = useRef<GraphData>({ nodes: [], links: [] });
  const clickTimers = useRef<Map<string, number>>(new Map());

  const setGraphData = useGraphStore(s => s.setGraphData);
  const selectNode = useGraphStore(s => s.selectNode);
  const setLoading = useGraphStore(s => s.setLoading);
  const focusNodeId = useGraphStore(s => s.focusNodeId);

  // ── Init ──
  useEffect(() => {
    let cancelled = false;

    async function init() {
      try {
        setLoading(true);
        const apiData = await fetchGraphData();
        const gData = apiToGraphData(apiData);
        graphDataRef.current = gData;

        // Update Zustand store
        if (!cancelled) {
          setGraphData(
            gData.nodes.map(n => ({
              id: n.id,
              label: n.name,
              category: n.domain,
              description: '',
              size: n.size,
              color: n.color,
              nodeType: n.nodeType as 'topic_hub' | 'leaf_concept',
            })),
            gData.links.map(l => ({ source: l.source, target: l.target, relation: l.relation }))
          );
        }

        if (!containerRef.current || cancelled) return;

        // ── Build 3D force graph ──
        const g = (ForceGraph3D as any)()(containerRef.current)
          .graphData(gData)
          .backgroundColor('#020617')

          // Nodes — custom sci‑fi objects
          .nodeThreeObject((n: unknown) => buildNodeObject(n as GraphNode))
          .nodeThreeObjectExtend(true)

          // Links — visible but elegant
          .linkColor(() => 'rgba(56, 189, 248, 0.18)')
          .linkWidth(0.5)
          .linkOpacity(0.35)
          .linkDirectionalParticles(0)
          .linkDirectionalParticleWidth(0)

          // Labels
          .nodeLabel((n: unknown) => (n as GraphNode).name)

          // Force simulation
          .numDimensions(3)
          .forceEngine('d3')
          .d3AlphaDecay(0.015)
          .d3VelocityDecay(0.35)
          .warmupTicks(80)
          .cooldownTicks(300)
          .cooldownTime(15000)

          // Camera
          .showNavInfo(false)
          .cameraPosition({ x: 150, y: 100, z: 220 })
          .enableNodeDrag(true)
          .enableNavigationControls(true)
          .enablePointerInteraction(true);

        // ── Add extra lights for sci‑fi materials ──
        const scene = g.scene();
        if (scene) {
          // Stronger ambient for base visibility
          const ambient = new THREE.AmbientLight(0x334466, 1.8);
          scene.add(ambient);

          // Key light from top-right-front
          const keyLight = new THREE.DirectionalLight(0xffffff, 2.5);
          keyLight.position.set(200, 300, 200);
          scene.add(keyLight);

          // Fill light from bottom-left
          const fillLight = new THREE.DirectionalLight(0x4488cc, 1.2);
          fillLight.position.set(-150, -50, -100);
          scene.add(fillLight);

          // Rim/back light for depth
          const rimLight = new THREE.DirectionalLight(0x88aadd, 1.0);
          rimLight.position.set(0, 0, -200);
          scene.add(rimLight);
        }

        // ── Single click → select + show right panel ──
        // ── Double click → expand neighborhood ──
        g.onNodeClick((n: unknown, event: MouseEvent) => {
          const node = n as GraphNode;
          const now = Date.now();
          const last = clickTimers.current.get(node.id) || 0;
          clickTimers.current.set(node.id, now);

          if (now - last < 350) {
            // ── DOUBLE CLICK: expand neighborhood ──
            clickTimers.current.delete(node.id);
            fetchNodeNeighborhood(node.id, 2)
              .then(neighborData => {
                const newData = apiToGraphData(neighborData);
                graphDataRef.current = newData;
                g.graphData(newData);

                // Update store
                setGraphData(
                  newData.nodes.map(n => ({
                    id: n.id,
                    label: n.name,
                    category: n.domain,
                    description: '',
                    size: n.size,
                    color: n.color,
                    nodeType: n.nodeType as 'topic_hub' | 'leaf_concept',
                  })),
                  newData.links.map(l => ({ source: l.source, target: l.target, relation: l.relation }))
                );
              })
              .catch(console.error);
          } else {
            // ── SINGLE CLICK: select + gentle camera move ──
            // Use setTimeout so double-click has time to cancel
            setTimeout(() => {
              const now2 = Date.now();
              const last2 = clickTimers.current.get(node.id) || 0;
              // If more than 350ms passed since last click, treat as single
              if (now2 - last2 >= 350) {
                selectNode({
                  id: node.id,
                  label: node.name,
                  category: node.domain,
                  description: '',
                  size: node.size,
                  color: node.color,
                  nodeType: node.nodeType as 'topic_hub' | 'leaf_concept',
                });

                // Gentle camera focus on node
                const pos = n as Record<string, number>;
                if (pos.x !== undefined) {
                  g.cameraPosition(
                    { x: pos.x + 50, y: pos.y + 30, z: pos.z + 100 },
                    n as object,
                    1200
                  );
                }
              }
            }, 360);
          }
        });

        // ── Hover effects ──
        g.onNodeHover((n: unknown | null) => {
          if (containerRef.current) {
            containerRef.current.style.cursor = n ? 'pointer' : 'grab';
          }
        });

        graphRef.current = g;
      } catch (err) {
        console.error('[GraphCanvas] Error:', err);
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    init();

    return () => {
      cancelled = true;
      graphRef.current?.pauseAnimation();
    };
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  // ── Resize handler ──
  useEffect(() => {
    function onResize() {
      if (graphRef.current) {
        graphRef.current.width(window.innerWidth);
        graphRef.current.height(window.innerHeight);
      }
    }
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);

  // ── External focus trigger (from search / sidebar) ──
  useEffect(() => {
    if (!focusNodeId || !graphRef.current) return;

    const g = graphRef.current;
    const currentData = g.graphData() as GraphData;
    const targetNode = currentData.nodes.find(n => n.id === focusNodeId);
    if (targetNode) {
      // Node is in current graph data — fly camera to it
      const pos = targetNode as unknown as Record<string, number>;
      if (pos.x !== undefined) {
        g.cameraPosition(
          { x: pos.x + 50, y: pos.y + 30, z: pos.z + 100 },
          targetNode as object,
          1200
        );
      }
    }
  }, [focusNodeId]);

  return <div ref={containerRef} className="absolute inset-0 z-10" />;
}
