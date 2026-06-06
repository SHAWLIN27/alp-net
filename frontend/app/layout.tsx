import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

export const dynamic = 'force-dynamic';

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
});

export const metadata: Metadata = {
  title: 'ALP_Net — Physics Knowledge Universe',
  description: 'Interactive physics knowledge graph — CAIE 9702 & Edexcel IAL',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${inter.variable} h-full`}>
      <head>
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/katex@0.17.0/dist/katex.min.css"
          integrity="sha384-HDi2TszSZQwQxXvLWr6sG7H4xxcKIImIrvWq4JxNkgQs5C+WHkAiXdGyH4XbNva"
          crossOrigin="anonymous"
        />
      </head>
      <body className="h-full bg-[#020617] text-slate-200 font-sans antialiased overflow-hidden">
        {children}
      </body>
    </html>
  );
}
