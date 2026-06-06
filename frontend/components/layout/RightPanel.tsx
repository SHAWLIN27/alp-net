'use client';

import { useGraphStore } from '@/store';
import { motion, AnimatePresence } from 'framer-motion';
import { X } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { useEffect, useState, useMemo, useRef } from 'react';
import { fetchConcept } from '@/lib/api';

// ── Section parsing ──
interface ContentSection {
  id: string;
  number: number;
  shortTitle: string;
  fullTitle: string;
  content: string;
}

// Map section numbers to compact tab labels
const SECTION_LABELS: Record<number, string> = {
  1: 'Overview',
  2: 'Syllabus',
  3: 'Definitions',
  4: 'Concepts',
  5: 'Equations',
  6: 'Graphs',
  7: 'Diagrams',
  8: 'Examples',
  9: 'Past Papers',
  10: 'Practicals',
  11: 'Concept Map',
  12: 'Examiner',
  13: 'Revision',
  14: 'Metadata',
};

function parseSections(md: string): ContentSection[] {
  if (!md) return [];

  const headingRegex = /^# (\d+)\.\s+(.+)$/gm;
  const splits: { index: number; number: number; title: string }[] = [];
  let match: RegExpExecArray | null;

  while ((match = headingRegex.exec(md)) !== null) {
    splits.push({
      index: match.index,
      number: parseInt(match[1], 10),
      title: match[2].trim(),
    });
  }

  if (splits.length === 0) {
    return [{
      id: 'overview',
      number: 1,
      shortTitle: 'Content',
      fullTitle: 'Content',
      content: md,
    }];
  }

  const sections: ContentSection[] = [];
  for (let i = 0; i < splits.length; i++) {
    const start = splits[i].index;
    const end = i + 1 < splits.length ? splits[i + 1].index : md.length;
    const rawContent = md.slice(start, end).trim();

    sections.push({
      id: `sec-${splits[i].number}`,
      number: splits[i].number,
      shortTitle: SECTION_LABELS[splits[i].number] || splits[i].title.split(' / ')[0],
      fullTitle: splits[i].title,
      content: rawContent,
    });
  }

  return sections;
}

// ── Component ──
export default function RightPanel() {
  const { selectedNode, selectNode, rightPanelOpen } = useGraphStore();
  const [detailContent, setDetailContent] = useState<string>('');
  const [activeSection, setActiveSection] = useState<string>('');
  const [loading, setLoading] = useState(false);
  const sectionRefs = useRef<Map<string, HTMLDivElement>>(new Map());
  const contentScrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!selectedNode) {
      setDetailContent('');
      return;
    }
    setLoading(true);
    fetchConcept(selectedNode.id)
      .then((data: Record<string, unknown>) => {
        const md = (data.content_md as string) || (data.definition as string) || '';
        setDetailContent(md);
      })
      .catch(() => setDetailContent(''))
      .finally(() => setLoading(false));
  }, [selectedNode]);

  const sections = useMemo(() => parseSections(detailContent), [detailContent]);

  // Auto-select first section
  useEffect(() => {
    if (sections.length > 0) {
      setActiveSection(sections[0].id);
    }
  }, [sections]);

  const scrollToSection = (sectionId: string) => {
    setActiveSection(sectionId);
    const el = sectionRefs.current.get(sectionId);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  if (!selectedNode && !rightPanelOpen) return null;

  return (
    <AnimatePresence>
      {rightPanelOpen && selectedNode && (
        <motion.aside
          initial={{ x: 440, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          exit={{ x: 440, opacity: 0 }}
          transition={{ duration: 0.38, ease: [0.22, 1, 0.36, 1] }}
          className="fixed right-4 top-4 bottom-4 w-[430px] z-30 flex flex-col rounded-2xl border border-white/[0.06] bg-[#020617]/90 backdrop-blur-2xl overflow-hidden shadow-2xl shadow-black/60"
        >
          {/* ── Header ── */}
          <div className="flex-shrink-0 px-5 pt-5 pb-3 border-b border-white/[0.05]">
            <div className="flex items-start justify-between gap-3">
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2 mb-1.5">
                  <span
                    className="w-2.5 h-2.5 rounded-full flex-shrink-0"
                    style={{ backgroundColor: selectedNode.color, boxShadow: `0 0 10px ${selectedNode.color}` }}
                  />
                  <span className="text-[10px] text-slate-500 uppercase tracking-widest">
                    {selectedNode.nodeType === 'topic_hub' ? 'Topic Hub' : 'Sub Topic'}
                  </span>
                  <span className="text-[10px] text-slate-600">·</span>
                  <span className="text-[10px] text-slate-600 truncate">{selectedNode.category}</span>
                </div>
                <h2 className="text-sm font-bold text-white leading-snug">
                  {selectedNode.label}
                </h2>
              </div>
              <button
                onClick={() => selectNode(null)}
                className="p-1.5 rounded-lg hover:bg-white/[0.06] text-slate-500 hover:text-slate-300 transition-colors flex-shrink-0"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            {/* ── Section tabs ── */}
            {sections.length > 1 && (
              <div className="flex gap-1 mt-3 overflow-x-auto -mx-1 px-1"
                   style={{ scrollbarWidth: 'none' }}>
                {sections.map(section => (
                  <button
                    key={section.id}
                    onClick={() => scrollToSection(section.id)}
                    className={`flex-shrink-0 px-3 py-1.5 rounded-lg text-[11px] font-medium transition-all duration-200 ${
                      activeSection === section.id
                        ? 'bg-white/[0.10] text-white shadow-sm'
                        : 'text-slate-500 hover:text-slate-300 hover:bg-white/[0.04]'
                    }`}
                    title={section.fullTitle}
                  >
                    {section.shortTitle}
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* ── Content ── */}
          <div ref={contentScrollRef} className="flex-1 overflow-y-auto">
            {loading ? (
              <div className="flex items-center justify-center h-40">
                <div className="flex items-center gap-2 text-sm text-slate-500">
                  <div className="w-3 h-3 rounded-full border border-[#38BDF8] border-t-transparent animate-spin" />
                  Loading...
                </div>
              </div>
            ) : sections.length > 0 ? (
              <div className="px-5 py-4 space-y-1">
                {sections.map(section => (
                  <div
                    key={section.id}
                    ref={el => { if (el) sectionRefs.current.set(section.id, el); }}
                  >
                    <div className="obsidian-content">
                      <ReactMarkdown
                        remarkPlugins={[remarkMath]}
                        rehypePlugins={[rehypeKatex]}
                      >
                        {section.content}
                      </ReactMarkdown>
                    </div>
                  </div>
                ))}
              </div>
            ) : detailContent ? (
              <div className="px-5 py-4">
                <div className="obsidian-content">
                  <ReactMarkdown
                    remarkPlugins={[remarkMath]}
                    rehypePlugins={[rehypeKatex]}
                  >
                    {detailContent}
                  </ReactMarkdown>
                </div>
              </div>
            ) : (
              <div className="flex items-center justify-center h-40">
                <p className="text-sm text-slate-600">No content available</p>
              </div>
            )}
          </div>

          {/* ── Footer ── */}
          <div className="flex-shrink-0 px-5 py-3 border-t border-white/[0.05]">
            <div className="flex items-center justify-between text-[10px] text-slate-600">
              <span className="truncate max-w-[260px] font-mono">{selectedNode.id}</span>
              <span>{sections.length} sections</span>
            </div>
          </div>
        </motion.aside>
      )}
    </AnimatePresence>
  );
}
