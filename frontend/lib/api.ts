import axios from 'axios';
import type { ApiGraphData, SearchResult } from '@/types';

const API_BASE = typeof window !== 'undefined'
  ? process.env.NEXT_PUBLIC_API_URL || '/api/v1'
  : '/api/v1';

const api = axios.create({
  baseURL: API_BASE,
  timeout: 30_000,
});

export async function fetchGraphData(): Promise<ApiGraphData> {
  const { data } = await api.get<ApiGraphData>('/graph/topics');
  return data;
}

export async function fetchNodeNeighborhood(nodeId: string, depth = 2): Promise<ApiGraphData> {
  const { data } = await api.get<ApiGraphData>(
    `/graph/concepts/${encodeURIComponent(nodeId)}/neighborhood?depth=${depth}`
  );
  return data;
}

export async function fetchConcept(nodeId: string) {
  const { data } = await api.get(`/graph/concepts/${encodeURIComponent(nodeId)}`);
  return data;
}

export async function semanticSearch(query: string, topK = 8): Promise<SearchResult[]> {
  const { data } = await api.post('/search/semantic', { query, top_k: topK });
  return data.results ?? [];
}
