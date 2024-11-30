import pytest
from fastapi.testclient import TestClient
from .main import app  # Importar la instancia de la app de FastAPI desde main.py

client = TestClient(app)

# Prueba para crear un cliente exitosamente
def test_crear_cliente():
    response = client.post("/clientes", json={
        "name": "Juan Pérez",
        "ci": "1234567890",
        "phone": "593987654321",
        "city": "Guayaquil",
        "local": "001",
        "email": "juan.perez@example.com",
        "puntos": 100
    })
    assert response.status_code == 200
    assert "hash_id" in response.json()
    assert response.json()["message"] == "Cliente creado exitosamente"

# Prueba para campos faltantes
def test_crear_cliente_faltan_datos():
    response = client.post("/clientes", json={
        "name": "Juan Pérez",
        "ci": "1234567890",
        # Falta el campo phone
        "city": "Guayaquil",
        "local": "001",
        "email": "juan.perez@example.com",
        "puntos": 100
    })
    assert response.status_code == 422  # Error por validación de datos

# Prueba para email inválido
def test_crear_cliente_email_invalido():
    response = client.post("/clientes", json={
        "name": "Juan Pérez",
        "ci": "1234567890",
        "phone": "593987654321",
        "city": "Guayaquil",
        "local": "001",
        "email": "email_invalido",  # Email no válido
        "puntos": 100
    })
    assert response.status_code == 422  # Error por validación de email

# Prueba para puntos como valor negativo
def test_crear_cliente_puntos_negativos():
    response = client.post("/clientes", json={
        "name": "Juan Pérez",
        "ci": "1234567890",
        "phone": "593987654321",
        "city": "Guayaquil",
        "local": "001",
        "email": "juan.perez@example.com",
        "puntos": -10  # Puntos no debería ser negativo
    })
    assert response.status_code == 422  # Error por validación personalizada (opcional)

# Prueba para la respuesta de base de datos no disponible
@pytest.mark.asyncio
async def test_error_base_datos(mocker):
    mocker.patch(
        "api.routes.insertar_cliente_en_db",
        side_effect=Exception("Base de datos no disponible")
    )
    response = client.post("/clientes", json={
        "name": "Juan Pérez",
        "ci": "1234567890",
        "phone": "593987654321",
        "city": "Guayaquil",
        "local": "001",
        "email": "juan.perez@example.com",
        "puntos": 100
    })
    assert response.status_code == 500
    assert "Base de datos no disponible" in response.json()["detail"]
