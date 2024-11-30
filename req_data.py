# backend/req_data.py
"""
Ruta: ~/mrjoy/backend/req_data.py
Interacción: Solicita datos por terminal, los envía por WebSocket y muestra la respuesta.

Este script envía los datos al backend y muestra la respuesta.

Ejemplo de Uso:
    - Ejecutar: python req_data.py
    - Ingresar datos por terminal.
"""

import asyncio
import websockets
import json

VOLTA_HOST = "192.168.100.184"
PORT = 5000

async def send_data():
    # Solicitar datos del usuario con validación
    try:
        name = input("Ingrese nombre: ")
        ci = input("Ingrese cédula: ")
        phone = input("Ingrese teléfono: ")
        city = input("Ingrese ciudad: ")
        local = input("Ingrese local: ")
        email = input("Ingrese email: ")

        # Validación de puntos
        while True:
            try:
                points = int(input("Ingrese puntos: "))
                break  # Si la conversión es exitosa, sale del bucle
            except ValueError:
                print("Por favor, ingrese un valor numérico para los puntos.")

        data = {
            "name": name,
            "ci": ci,
            "phone": phone,
            "city": city,
            "local": local,
            "email": email,
            "points": points
        }

        async with websockets.connect(f"ws://{VOLTA_HOST}:{PORT}") as websocket:
            # Enviar datos
            await websocket.send(json.dumps(data))
            # Recibir respuesta
            response = await websocket.recv()
            print("Respuesta del servidor:", response)

    except Exception as e:
        print(f"Error al enviar los datos: {e}")

if __name__ == "__main__":
    asyncio.run(send_data())

