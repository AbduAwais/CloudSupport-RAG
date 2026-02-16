.PHONY: help setup install-backend install-frontend run dev run-backend run-frontend clean fill-db

# Variables
PYTHON := python3
PIP := pip3
NODE := node
NPM := npm
VENV := .venv

help:
	@echo "RAG Project - Available Commands"
	@echo "================================"
	@echo "make setup              - Complete setup (venv + install all dependencies)"
	@echo "make install            - Install all dependencies (backend + frontend)"
	@echo "make install-backend    - Install backend dependencies"
	@echo "make install-frontend   - Install frontend dependencies"
	@echo "make run                - Run backend and frontend together"
	@echo "make dev                - Run frontend in dev mode only"
	@echo "make run-backend        - Run backend API server only"
	@echo "make run-frontend       - Run frontend dev server only"
	@echo "make fill-db            - Populate ChromaDB with documents"
	@echo "make clean              - Remove node_modules and venv"
	@echo "make format             - Format Python code"
	@echo "make lint               - Lint Python code"

# Setup the project
setup: venv install-backend install-frontend
	@echo "✅ Project setup complete!"
	@echo "Run 'make run' to start the project"

# Install all dependencies
install: install-backend install-frontend
	@echo "✅ All dependencies installed"

# Create virtual environment
venv:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating Python virtual environment..."; \
		$(PYTHON) -m venv $(VENV); \
		. $(VENV)/bin/activate && $(PIP) install --upgrade pip; \
		echo "✅ Virtual environment created"; \
	else \
		echo "Virtual environment already exists"; \
	fi

# Install backend dependencies
install-backend: venv
	@echo "Installing backend dependencies..."
	. $(VENV)/bin/activate && cd backend && $(PIP) install -r requirements.txt
	@echo "✅ Backend dependencies installed"

# Install frontend dependencies
install-frontend:
	@echo "Installing frontend dependencies..."
	cd frontend && $(NPM) install
	@echo "✅ Frontend dependencies installed"

# Populate ChromaDB
fill-db: venv
	@echo "Populating ChromaDB with documents..."
	. $(VENV)/bin/activate && cd backend && $(PYTHON) fill_db.py
	@echo "✅ Database populated"

# Run both backend and frontend
run: run-backend run-frontend

# Run only backend
run-backend: venv
	@echo "🚀 Starting backend API server..."
	. $(VENV)/bin/activate && cd backend && $(PYTHON) app.py

# Run only frontend
run-frontend:
	@echo "🚀 Starting frontend dev server..."
	cd frontend && $(NPM) run dev

# Run frontend in dev mode (alternative target)
dev:
	@echo "🚀 Starting frontend dev server..."
	cd frontend && $(NPM) run dev

# Build frontend
build-frontend:
	@echo "Building frontend..."
	cd frontend && $(NPM) run build
	@echo "✅ Frontend build complete"

# Format Python code
format:
	@echo "Formatting Python code..."
	. $(VENV)/bin/activate && $(PYTHON) -m black backend/ --line-length=100
	@echo "✅ Code formatted"

# Lint Python code
lint:
	@echo "Linting Python code..."
	. $(VENV)/bin/activate && cd backend && $(PYTHON) -m pylint **/*.py
	@echo "✅ Linting complete"

# Clean up
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV)
	rm -rf frontend/node_modules
	rm -rf frontend/dist
	rm -rf backend/__pycache__
	rm -rf backend/**/__pycache__
	rm -f backend/conversations.db
	@echo "✅ Cleanup complete"

# Full reset
reset: clean setup
	@echo "✅ Project reset complete!"
