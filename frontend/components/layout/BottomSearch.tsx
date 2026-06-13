'use client';

import { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, RotateCcw, Crosshair, Maximize2 } from 'lucide-react';
import { useGraphStore } from '@/store';
import { createFuseIndex, searchNodes } from '@/lib/fuse';

export default function BottomSearch() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<ReturnType<typeof searchNodes>>([]);
  const [showResults, setShowResults] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  const { nodes, selectNode, focusNode, triggerGraphCommand } = useGraphStore();

  useEffect(() => {
    if (nodes.length > 0) createFuseIndex(nodes);
  }, [nodes]);

  const handleSearch = (value: string) => {
    setQuery(value);
    if (value.trim()) {
      const r = searchNodes(value);
      setResults(r);
      setShowResults(true);
    } else {
      setResults([]);
      setShowResults(false);
    }
  };

  const handleSelect = (node: (typeof results)[0]) => {
    selectNode(node);
    focusNode(node.id);      // trigger 3D camera focus
    setShowResults(false);
    setQuery(node.label);
  };

  const handleReset = () => {
    selectNode(null);
    setQuery('');
    setResults([]);
    triggerGraphCommand('reset');
  };

  const handleCenter = () => {
    triggerGraphCommand('center');
  };

  const handleFit = () => {
    triggerGraphCommand('fit');
  };

  // ── Cmd+K / Ctrl+K keyboard shortcut ──
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        inputRef.current?.focus();
      }
    }
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, []);

  return (
    <motion.div
      initial={{ y: 100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, delay: 0.3, ease: 'easeOut' }}
      className="fixed bottom-6 left-1/2 -translate-x-1/2 z-30 flex items-end gap-3"
    >
      <div className="flex gap-2">
        <ControlButton icon={<RotateCcw className="w-4 h-5" />} label="Reset" onClick={handleReset} />
        <ControlButton icon={<Crosshair className="w-4 h-5" />} label="Center" onClick={handleCenter} />
        <ControlButton icon={<Maximize2 className="w-4 h-5" />} label="Fit" onClick={handleFit} />
      </div>

      <div className="relative">
        <div className="flex items-center gap-3 px-5 py-3 rounded-2xl border border-white/[0.08] bg-[#020617]/80 backdrop-blur-2xl shadow-2xl shadow-black/50">
          <Search className="w-4 h-5 text-slate-500" />
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => handleSearch(e.target.value)}
            onFocus={() => query.trim() && setShowResults(true)}
            onBlur={() => setTimeout(() => setShowResults(false), 200)}
            placeholder="Search knowledge nodes..."
            className="w-64 bg-transparent text-sm text-white placeholder-slate-600 outline-none"
          />
          <kbd className="hidden sm:inline-flex items-center gap-0.5 px-2 py-0.5 rounded-md bg-white/[0.05] text-[10px] text-slate-600 border border-white/[0.06]">
            ⌘K
          </kbd>
        </div>

        <AnimatePresence>
          {showResults && results.length > 0 && (
            <motion.div
              initial={{ opacity: 0, y: -8 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -8 }}
              className="absolute bottom-full mb-2 left-0 right-0 rounded-xl border border-white/[0.06] bg-[#020617]/90 backdrop-blur-2xl overflow-hidden shadow-xl"
            >
              {results.map((node) => (
                <button
                  key={node.id}
                  onMouseDown={(e) => { e.preventDefault(); handleSelect(node); }}
                  className="w-full flex items-center gap-3 px-4 py-2.5 text-left hover:bg-white/[0.05] transition-colors"
                >
                  <span
                    className="w-2 h-2 rounded-full flex-shrink-0"
                    style={{ backgroundColor: node.color, boxShadow: `0 0 6px ${node.color}` }}
                  />
                  <div className="min-w-0">
                    <p className="text-sm text-slate-200 truncate">{node.label}</p>
                    <p className="text-[10px] text-slate-500">{node.category}</p>
                  </div>
                </button>
              ))}
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </motion.div>
  );
}

function ControlButton({ icon, label, onClick }: { icon: React.ReactNode; label: string; onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      className="flex flex-col items-center gap-1 p-3 rounded-2xl border border-white/[0.06] bg-[#020617]/80 backdrop-blur-2xl text-slate-500 hover:text-[#38BDF8] hover:border-[#38BDF8]/20 transition-all duration-300 shadow-lg shadow-black/50"
      title={label}
    >
      {icon}
    </button>
  );
}
