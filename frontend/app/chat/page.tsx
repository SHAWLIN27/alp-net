'use client';

import { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ArrowLeft, Send, Sparkles, User, Bot } from 'lucide-react';
import Link from 'next/link';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  sources?: { title: string; id: string }[];
}

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [streaming, setStreaming] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim() || streaming) return;

    const userMsg: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: input.trim(),
    };

    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setStreaming(true);

    try {
      const res = await fetch('/api/v1/chat/rag', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMsg.content, top_k: 5 }),
      });

      if (!res.ok) throw new Error('Chat failed');

      const reader = res.body?.getReader();
      const decoder = new TextDecoder();
      let assistantContent = '';

      const assistantMsg: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: '',
      };
      setMessages(prev => [...prev, assistantMsg]);

      if (reader) {
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          const chunk = decoder.decode(value, { stream: true });
          const lines = chunk.split('\n');
          for (const line of lines) {
            if (line.startsWith('data: ')) {
              try {
                const data = JSON.parse(line.slice(6));
                if (data.content) {
                  assistantContent += data.content;
                  setMessages(prev =>
                    prev.map(m =>
                      m.id === assistantMsg.id
                        ? { ...m, content: assistantContent, sources: data.sources }
                        : m
                    )
                  );
                }
              } catch {
                // non-JSON data chunk, ignore
              }
            }
          }
        }
      }
    } catch (err) {
      console.error('Chat error:', err);
      setMessages(prev => [
        ...prev,
        {
          id: (Date.now() + 2).toString(),
          role: 'assistant',
          content: 'Sorry, I encountered an error. Please try again.',
        },
      ]);
    } finally {
      setStreaming(false);
    }
  };

  return (
    <div className="flex flex-col h-full bg-[#020617]">
      {/* Header */}
      <header className="flex items-center gap-4 px-6 py-4 border-b border-white/[0.04] bg-[#020617]/90 backdrop-blur-xl">
        <Link
          href="/"
          className="p-2 rounded-xl hover:bg-white/[0.05] text-slate-500 hover:text-slate-300 transition-colors"
        >
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-[#38BDF8] to-[#A855F7] flex items-center justify-center">
            <Sparkles className="w-4 h-4 text-white" />
          </div>
          <div>
            <h1 className="text-sm font-bold text-white">Physics RAG Chat</h1>
            <p className="text-[10px] text-slate-500">Powered by DeepSeek + Knowledge Graph</p>
          </div>
        </div>
      </header>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-6 py-6 space-y-6">
        <AnimatePresence>
          {messages.map((msg) => (
            <motion.div
              key={msg.id}
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              className={`flex gap-4 ${msg.role === 'user' ? 'justify-end' : ''}`}
            >
              {msg.role === 'assistant' && (
                <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-[#38BDF8]/20 to-[#A855F7]/20 flex items-center justify-center flex-shrink-0">
                  <Bot className="w-4 h-4 text-[#38BDF8]" />
                </div>
              )}
              <div
                className={`max-w-[70%] rounded-2xl px-5 py-4 ${
                  msg.role === 'user'
                    ? 'bg-[#38BDF8]/10 border border-[#38BDF8]/20'
                    : 'bg-white/[0.03] border border-white/[0.05]'
                }`}
              >
                <div className="prose prose-invert prose-sm max-w-none">
                  <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
                    {msg.content || (streaming ? 'Thinking...' : '')}
                  </ReactMarkdown>
                </div>
                {msg.sources && msg.sources.length > 0 && (
                  <div className="mt-3 pt-3 border-t border-white/[0.05]">
                    <p className="text-[10px] text-slate-500 mb-1">Sources:</p>
                    {msg.sources.slice(0, 3).map((s, i) => (
                      <span key={i} className="inline-block text-[10px] text-[#38BDF8] mr-2">
                        {s.title}
                      </span>
                    ))}
                  </div>
                )}
              </div>
              {msg.role === 'user' && (
                <div className="w-8 h-8 rounded-xl bg-[#A855F7]/20 flex items-center justify-center flex-shrink-0">
                  <User className="w-4 h-4 text-[#A855F7]" />
                </div>
              )}
            </motion.div>
          ))}
        </AnimatePresence>
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="px-6 py-4 border-t border-white/[0.04] bg-[#020617]/90 backdrop-blur-xl">
        <div className="flex items-center gap-3 max-w-3xl mx-auto">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Ask a physics question..."
            className="flex-1 bg-white/[0.03] border border-white/[0.08] rounded-2xl px-5 py-3 text-sm text-white placeholder-slate-600 outline-none focus:border-[#38BDF8]/30 focus:bg-white/[0.05] transition-all"
            disabled={streaming}
          />
          <button
            onClick={sendMessage}
            disabled={!input.trim() || streaming}
            className="p-3 rounded-2xl bg-gradient-to-br from-[#38BDF8] to-[#A855F7] text-white disabled:opacity-30 disabled:cursor-not-allowed hover:shadow-lg hover:shadow-[#38BDF8]/20 transition-all"
          >
            <Send className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  );
}
