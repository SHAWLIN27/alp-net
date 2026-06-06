.PHONY: dev install backend frontend ingest clean

# Start all services
dev:
	@echo "Starting ALP_Net development environment..."
	@docker compose up -d chromadb
	@pip install -e ".[dev]"
	@cd frontend && npm install
	@uvicorn alpnet.api.app:app --reload --host 0.0.0.0 --port 8000 &
	@cd frontend && npm run dev &
	@echo ""
	@echo "✅ ALP_Net is running!"
	@echo "   Backend:  http://localhost:8000"
	@echo "   API Docs: http://localhost:8000/docs"
	@echo "   Frontend: http://localhost:5173"
	@echo ""
	@wait

# Install all dependencies
install:
	@pip install -e ".[dev]"
	@cd frontend && npm install

# Backend only
backend:
	@docker compose up -d chromadb
	@uvicorn alpnet.api.app:app --reload --host 0.0.0.0 --port 8000

# Frontend only
frontend:
	@cd frontend && npm run dev

# Ingest vault content
ingest:
	@python -m alpnet.cli.main ingest --full

# Ingest incremental
ingest-incr:
	@python -m alpnet.cli.main ingest --incremental

# Clean up
clean:
	@docker compose down
	@rm -rf data/*.json
	@rm -rf docker-data/
	@echo "Cleaned."
