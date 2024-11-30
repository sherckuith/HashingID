# backend/tests.py
"""
Ruta: ~/mrjoy/backend/tests.py
Interacción: Proporciona pruebas automáticas para la API REST.

Este es un archivo básico para pruebas automáticas.

Ejemplo de Uso:
    - Ejecutar: pytest tests.py
"""

import pytest
from fastapi.testclient import TestClient
from api_rest import app

client = TestClient(app)

def test_get_clients():
    response = client.get("/clientes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_post_clients():
    new_client = {
        "name": "Test User",
        "ci": "9876543210",
        "phone": "0912345678",
        "city": "Guayaquil",
        "local": "Local 2",
        "email": "testuser@example.com",
        "points": 20
    }
    response = client.post("/clientes", json=new_client)
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"