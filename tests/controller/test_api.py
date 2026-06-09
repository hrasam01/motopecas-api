import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from main import app
from app.database.dependencies import get_db
from app.security.auth_dependency import get_current_user


class TestAPI:

    @pytest.fixture
    def client(self):
        app.dependency_overrides[get_db] = lambda: Mock()
        app.dependency_overrides[get_current_user] = lambda: {"sub": "admin@motopecas.com"}
        return TestClient(app)

    def test_root(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json()["mensagem"] == "MotoPeças API funcionando!"

    def test_health_check(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_swagger_disponivel(self, client):
        response = client.get("/docs")
        assert response.status_code == 200
        assert "swagger" in response.text.lower()

    def test_openapi_disponivel(self, client):
        response = client.get("/openapi.json")
        assert response.status_code == 200
        assert response.json()["info"]["title"] == "MotoPeças API"
