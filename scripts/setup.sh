#!/bin/bash

# Privacy Rights Registry - Production-Ready Setup Script
# Now with security hardening, secrets management, and operational improvements

echo "🔒 Privacy Rights Registry - Production Setup"
echo "============================================"

set -e

# Check prerequisites
check_prerequisites() {
    echo "📋 Checking prerequisites..."
    
    command -v python3 >/dev/null || { 
        echo "❌ Python 3 is required but not installed. Please install Python 3.9+"; 
        exit 1; 
    }
    
    command -v docker >/dev/null || { 
        echo "⚠️  Docker not found. Some deployment options will be unavailable."; 
    }
    
    command -v redis-server >/dev/null || { 
        echo "⚠️  Redis not found. Rate limiting will use in-memory storage."; 
    }
    
    echo "✅ Prerequisites check complete"
}

# Create environment file from example
create_env() {
    if [ ! -f .env ]; then
        echo "📝 Creating .env from template..."
        cp .env.example .env
        echo "⚠️  Please edit .env with your production values before running!"
    else
        echo "✅ .env already exists"
    fi
}

# Create virtual environment
setup_venv() {
    if [ ! -d "venv" ]; then
        echo "🐍 Creating virtual environment..."
        python3 -m venv venv
    else
        echo "✅ Virtual environment already exists"
    fi
    
    echo "📦 Installing dependencies..."
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
}

# Initialize database
setup_database() {
    echo "🗄️  Setting up database..."
    source venv/bin/activate
    
    # Create initial migration if it doesn't exist
    if [ ! -d "migrations/versions" ]; then
        echo "📝 Creating initial database migration..."
        alembic revision --autogenerate -m "Initial migration"
    fi
    
    echo "🔄 Running database migrations..."
    alembic upgrade head
}

# Create systemd service (optional)
create_systemd_service() {
    if command -v systemctl >/dev/null; then
        echo "🚀 Creating systemd service..."
        cat > privacy-registry.service << EOF
[Unit]
Description=Privacy Rights Registry API
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$(pwd)
Environment=PATH=$(pwd)/venv/bin
ExecStart=$(pwd)/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
EOF
        echo "📁 Service file created: privacy-registry.service"
        echo "   To install: sudo cp privacy-registry.service /etc/systemd/system/"
        echo "   To enable: sudo systemctl enable privacy-registry"
        echo "   To start: sudo systemctl start privacy-registry"
    fi
}

# Run tests
run_tests() {
    echo "🧪 Running tests..."
    source venv/bin/activate
    python -m pytest tests/ -v
}

# Main execution
main() {
    check_prerequisites
    create_env
    setup_venv
    setup_database
    create_systemd_service
    
    echo ""
    echo "🎉 Privacy Rights Registry - Setup Complete!"
    echo "============================================"
    echo ""
    echo "📋 Next steps:"
    echo "1. Edit .env with your production values"
    echo "2. Run: ./scripts/run.sh"
    echo "3. Test: python -m pytest tests/"
    echo "4. Visit: http://localhost:8000/v1/docs"
    echo ""
    echo "🐳 Or use Docker:"
    echo "1. docker-compose up -d"
    echo "2. curl http://localhost:8000/v1/health"
    echo ""
    echo "🚀 Ready to protect privacy rights in Ireland!"
}

main "$@"