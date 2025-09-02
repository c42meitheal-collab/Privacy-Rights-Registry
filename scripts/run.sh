#!/bin/bash

# Privacy Rights Registry - Development Server Runner

set -e

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '#' | xargs)
fi

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Run ./scripts/setup.sh first"
    exit 1
fi

# Run database migrations
echo "🔄 Running database migrations..."
alembic upgrade head

# Start the server
echo "🚀 Starting Privacy Rights Registry..."
echo "📡 API Documentation: http://localhost:8000/v1/docs"
echo "🔍 Health Check: http://localhost:8000/v1/health"
echo "📊 Global Stats: http://localhost:8000/v1/transparency/global"
echo ""
echo "Press Ctrl+C to stop"

uvicorn main:app --reload --host 0.0.0.0 --port 8000 --log-level info