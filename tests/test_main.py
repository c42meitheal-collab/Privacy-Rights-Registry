"""
Privacy Rights Registry - API Tests
Test suite for the Irish Privacy Rights Registry API

This test suite validates:
- User registration and privacy rights management
- Anti-doxxing protection enforcement
- Company registration and API key management
- Transparency and compliance reporting
- GDPR/Irish Data Protection law compliance
"""

import pytest
import asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import json
from datetime import datetime, timedelta

# Import the main application
from main import app, get_db, Settings


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
async def async_client():
    """Create an async test client"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


class TestHealthCheck:
    """Test health check endpoint"""
    
    def test_health_check_success(self, client):
        """Test successful health check"""
        response = client.get("/v1/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] in ["healthy", "degraded"]
        assert "timestamp" in data
        assert "version" in data


class TestUserRegistration:
    """Test user registration and privacy rights management"""
    
    def test_user_registration_success(self, client):
        """Test successful user registration with strong password"""
        user_data = {
            "email": "test@example.ie",
            "password": "StrongPass123!",
            "rights": {
                "erasure": True,
                "no_sale": True,
                "no_profiling": False,
                "no_marketing": True,
                "data_portability": True,
                "access_request": True,
                "anti_doxxing": True  # Anti-doxxing protection enabled
            }
        }
        
        response = client.post("/v1/register", json=user_data)
        assert response.status_code == 201
        data = response.json()
        
        # Verify response structure
        assert "token" in data
        assert "rights" in data
        assert "expires_at" in data
        assert data["rights"]["anti_doxxing"] is True
        assert data["message"] == "User registered successfully"
    
    def test_user_registration_weak_password(self, client):
        """Test that weak passwords are rejected"""
        user_data = {
            "email": "test@example.ie",
            "password": "weak",
            "rights": {"erasure": True}
        }
        
        response = client.post("/v1/register", json=user_data)
        assert response.status_code == 422  # Validation error


class TestCompanyRegistration:
    """Test company registration and API key management"""
    
    def test_company_registration_success(self, client):
        """Test successful company registration"""
        company_data = {
            "name": "Test Company Ltd",
            "contact_email": "legal@testcompany.ie"
        }
        
        response = client.post("/v1/company/register", json=company_data)
        assert response.status_code == 201
        data = response.json()
        
        # Verify response structure
        assert "api_key" in data
        assert "company_id" in data
        assert data["name"] == "Test Company Ltd"
        assert data["api_key"].startswith("prr_")  # Prefixed API key


class TestAntiDoxxingProtection:
    """Test anti-doxxing protection enforcement"""
    
    def test_anti_doxxing_blocks_lookup(self, client):
        """Test that anti-doxxing protection blocks data lookups"""
        # Register user with anti-doxxing protection
        user_data = {
            "email": "protected@example.ie",
            "password": "StrongPass123!",
            "rights": {"anti_doxxing": True}
        }
        
        user_response = client.post("/v1/register", json=user_data)
        assert user_response.status_code == 201
        token = user_response.json()["token"]
        
        # Register company
        company_data = {
            "name": "Test Company",
            "contact_email": "test@company.ie"
        }
        
        company_response = client.post("/v1/company/register", json=company_data)
        assert company_response.status_code == 201
        api_key = company_response.json()["api_key"]
        
        # Try to lookup protected user - should be blocked
        headers = {"Authorization": f"Bearer {api_key}"}
        lookup_response = client.get(f"/v1/registry/{token}", headers=headers)
        
        assert lookup_response.status_code == 403
        assert "anti-doxxing protection" in lookup_response.json()["detail"]


class TestTransparencyReporting:
    """Test transparency and compliance reporting"""
    
    def test_global_transparency_endpoint(self, client):
        """Test global transparency statistics"""
        response = client.get("/v1/transparency/global")
        assert response.status_code == 200
        data = response.json()
        
        # Verify required fields
        required_fields = [
            "total_users", "total_companies", "total_lookups",
            "blocked_lookups", "protection_rate"
        ]
        
        for field in required_fields:
            assert field in data
            assert isinstance(data[field], (int, float))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])