# backend/encoder_ws.py
"""
Ruta: ~/mrjoy/backend/encoder_ws.py
Interacción: Recibe datos por WebSocket, genera un hash y devuelve los datos.

Este script escuchará en el puerto 5000 para recibir datos, generar un hash ID y devolver los datos completos.

Ejemplo de Uso:
    - Ejecutar: python encoder_ws.py
    - Enviar datos desde req_data.py y recibir hash generado para luego procesar en la DB.
"""

import hashlib
import json
import websockets
import asyncio
import asyncpg

PORT = 5000
DB_CONFIG = {
    "user": "postgres",
    "password": "password",
    "database": "mrjoy",
    "host": "mrjoy-db",
    "port": 5432
}

# Crear un pool de conexiones para evitar abrir y cerrar conexiones a la base de datos en cada mensaje.
async def get_db_pool():
    return await asyncpg.create_pool(**DB_CONFIG)

# Save.. para usar el pool de conexiones en lugar de crear una nueva conexión cada vez.
async def save_to_db(pool, data):
    async with pool.acquire() as conn:
        query = """
        INSERT INTO CLIENTES (nombre, cedula, telefono, ciudad, local, email, puntos, hash_id, validador)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
        """
        await conn.execute(query, data["name"], data["ci"], data["phone"], data["city"],
                           data["local"], data["email"], data["points"], data["id"], data["validator"])

async def handle_connection(websocket, pool):
    try:
        async for message in websocket:
            data = json.loads(message)
            # Generar hash ID
            data_str = f"{data['name']}{data['ci']}{data['phone']}{data['city']}{data['local']}{data['email']}{data['points']}"
            hash_id = hashlib.sha256(data_str.encode()).hexdigest()
            data["id"] = hash_id

            # Validar el hash generado
            is_valid = hashlib.sha256(data_str.encode()).hexdigest() == hash_id
            data["validator"] = 1 if is_valid else 0

            # Guardar en la base de datos
            await save_to_db(pool, data)

            # Enviar los datos procesados al cliente
            await websocket.send(json.dumps(data))
    except Exception as e:
        print(f"Error en el manejo de la conexión: {e}")
        await websocket.send(json.dumps({"error": "Hubo un error procesando los datos."}))



async def main():
    pool = await get_db_pool()
    async with websockets.serve(lambda ws, path: handle_connection(ws, pool), "0.0.0.0", PORT):
        print(f"Servidor WebSocket escuchando en el puerto {PORT}")
        await asyncio.Future()  # Mantener el servidor corriendo

if __name__ == "__main__":
    asyncio.run(main())
