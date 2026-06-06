'use client';

import dynamic from 'next/dynamic';
import LeftSidebar from '@/components/layout/LeftSidebar';
import RightPanel from '@/components/layout/RightPanel';
import BottomSearch from '@/components/layout/BottomSearch';
import ParticleBackground from '@/components/effects/ParticleBackground';
import { useGraphStore } from '@/store';
import { motion, AnimatePresence } from 'framer-motion';

const GraphCanvas = dynamic(() => import('@/components/graph/GraphCanvas'), {
  ssr: false,
  loading: () => (
    <div className="absolute inset-0 flex items-center justify-center z-10">
      <div className="flex flex-col items-center gap-4">
        <div className="w-8 h-8 rounded-full border-2 border-[#38BDF8] border-t-transparent animate-spin" />
        <p className="text-sm text-slate-500">Loading Knowledge Universe...</p>
      </div>
    </div>
  ),
});

export default function HomePage() {
  const { isLoading } = useGraphStore();

  return (
    <main className="relative w-full h-full overflow-hidden">
      <ParticleBackground />

      <AnimatePresence>
        {isLoading && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="absolute inset-0 z-20 flex items-center justify-center bg-[#020617]/80 backdrop-blur-sm"
          >
            <div className="flex flex-col items-center gap-5">
              <div className="relative">
                <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-[#38BDF8] to-[#A855F7] animate-pulse" />
                <div className="absolute inset-0 rounded-2xl bg-gradient-to-br from-[#38BDF8] to-[#A855F7] blur-xl opacity-50 animate-pulse" />
              </div>
              <div className="text-center">
                <h2 className="text-lg font-bold text-white mb-1">ALP_NET</h2>
                <p className="text-sm text-slate-500">Initializing Physics Knowledge Universe</p>
              </div>
              <div className="flex gap-1.5">
                {[0, 1, 2].map((i) => (
                  <motion.div
                    key={i}
                    className="w-2 h-2 rounded-full bg-[#38BDF8]"
                    animate={{ opacity: [0.3, 1, 0.3] }}
                    transition={{ duration: 1.2, delay: i * 0.2, repeat: Infinity }}
                  />
                ))}
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      <GraphCanvas />
      <LeftSidebar />
      <RightPanel />
      <BottomSearch />
    </main>
  );
}
