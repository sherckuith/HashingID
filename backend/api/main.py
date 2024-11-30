# backend/api/main.py
"""
Ruta: ~/mrjoy/backend/api_rest.py
Interacción: Proporciona una API REST para interactuar con encoder_ws.py y la base de datos.

Este script permite interactuar con el sistema usando métodos HTTP como GET, POST y PATCH.

Ejemplo de Uso:
    - GET /clientes -> Obtiene todos los clientes.
    - POST /clientes -> Añade un nuevo cliente.
"""

from fastapi import FastAPI, HTTPException
from api.routes import router
import asyncpg
import hashlib
import os

app = FastAPI()

app.include_router(router)

# Configuración de la base de datos utilizando variables de entorno
DB_CONFIG = {
    "user": os.getenv("DB_USER", "postgres"),  # Utiliza DB_USER del entorno, por defecto 'postgres'
    "password": os.getenv("DB_PASSWORD", "password"),  # Utiliza DB_PASSWORD del entorno
    "database": os.getenv("DB_NAME", "mrjoy"),  # Utiliza DB_NAME del entorno, por defecto 'mrjoy'
    "host": os.getenv("DB_HOST", "mrjoy_db"),  # Utiliza DB_HOST del entorno, por defecto 'mrjoy_db'
    "port": int(os.getenv("DB_PORT", 5432))  # Utiliza DB_PORT del entorno, por defecto 5432
}

@app.on_event("startup")
async def startup():
    """Se conecta a la base de datos cuando la aplicación arranca."""
    global conn
    try:
        conn = await asyncpg.connect(**DB_CONFIG)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar a la base de datos: {str(e)}")

@app.on_event("shutdown")
async def shutdown():
    """Cierra la conexión a la base de datos al apagar la aplicación."""
    await conn.close()

@app.get("/clientes")
async def get_clients():
    """Obtiene todos los clientes de la base de datos."""
    query = "SELECT * FROM CLIENTES"
    try:
        clients = await conn.fetch(query)
        return clients
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener clientes: {str(e)}")

@app.post("/clientes")
async def create_client(client: dict):
    """Crea un nuevo cliente en la base de datos."""
    query = """
    INSERT INTO CLIENTES (nombre, cedula, telefono, ciudad, local, email, puntos, hash_id, validador)
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
    RETURNING *
    """
    try:
        # Creación del hash_id del cliente para la seguridad
        client_str = f"{client['name']}{client['ci']}{client['phone']}{client['city']}{client['local']}{client['email']}{client['points']}"
        client["hash_id"] = hashlib.sha256(client_str.encode()).hexdigest()
        client["validador"] = 1  # Siempre se valida al crear
        result = await conn.fetchrow(query, client["name"], client["ci"], client["phone"],
                                     client["city"], client["local"], client["email"],
                                     client["points"], client["hash_id"], client["validador"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear cliente: {str(e)}")
