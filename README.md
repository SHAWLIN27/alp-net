# ALP_Net

A-Level Physics Knowledge Graph RAG system with an Obsidian authoring vault, NetworkX graph store, ChromaDB vector store, FastAPI backend, and React/Cytoscape frontend.

## Stack

- Content: Obsidian Markdown vault
- Graph: NetworkX + JSON
- Vector DB: ChromaDB
- Backend: FastAPI
- Frontend: React + TypeScript + Vite + Cytoscape.js
- LLM: DeepSeek API

## Quick Start

1. Copy `.env` and set `DEEPSEEK_API_KEY`.
2. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   cd frontend && npm install
   ```
3. Start ChromaDB:
   ```bash
   docker compose up -d chromadb
   ```
4. Start backend:
   ```bash
   uvicorn alpnet.api.app:app --reload --host 0.0.0.0 --port 8000
   ```
5. Start frontend:
   ```bash
   cd frontend && npm run dev
   ```

## Development Targets

- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Frontend: http://localhost:5173
