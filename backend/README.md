# Proyecto MrJoy

## Instalación
1. Clona el repositorio.
2. Corre `docker-compose up --build`.
3. Accede a la API REST en `http://localhost:8000`.

## Uso con POSTMAN
### Endpoints
1. **GET /clientes**: Obtiene todos los clientes.
2. **POST /clientes**: Crea un cliente.
   - Body (JSON):
     ```json
     {
       "name": "Juan Perez",
       "ci": "1234567890",
       "phone": "0999999999",
       "city": "Quito",
       "local": "Local 1",
       "email": "juanperez@example.com",
       "points": 10
     }
     ```

## Lógica del Sistema
1. Entrada: Datos de un cliente desde `req_data.py` o `POST /clientes`.
2. Proceso: Generación de hash en `encoder_ws.py`.
3. Salida: Respuesta con datos guardados.


### POSTMAN Collection
#### Exportaremos una colección para que puedas importarla directamente.

1. GET /clientes

URL: http://localhost:8000/clientes
Método: GET

2. POST /clientes

URL: http://localhost:8000/clientes
Método: POST
Body (JSON):

		{
		  "name": "Carlos Lopez",
		  "ci": "1102345678",
		  "phone": "0987654321",
		  "city": "Guayaquil",
		  "local": "Local 2",
		  "email": "carlos@example.com",
		  "points": 20
		}
		
### Estructura de datos:
		
mrjoy/
├── backend
│   ├── api
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   └── main.cpython-39.pyc
│   │   ├── routes.py
│   │   └── tests.py
│   ├── Dockerfile
│   ├── Dockerfile.encoder_ws
│   ├── encoder_ws.py
│   ├── README.md
│   ├── requirements.txt
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_routes.py
│   ├── tests.py
│   └── wait-for-it
│       ├── composer.json
│       ├── LICENSE
│       ├── README.md
│       ├── test
│       │   ├── container-runners.py
│       │   ├── README.md
│       │   ├── requirements.txt
│       │   └── wait-for-it.py
│       └── wait-for-it.sh
├── docker-compose.yml
├── encoder.py
├── init.sql
└── req_data.py

6 directories, 26 files


### Explicacion:

El script req_data.py tiene la funcionalidad de solicitar datos al usuario y enviarlos 
a través de un WebSocket, lo cual es adecuado para una interacción en tiempo real. 

Conexión al WebSocket: Usar websockets.connect(f"ws://{VOLTA_HOST}:{PORT}")

Asegurar que VOLTA_HOST esté configurado correctamente en la red, y que el puerto 5000 
esté abierto para la comunicación.