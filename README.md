# HashingID
HashingID es una aplicación que gestiona clientes a través de una API REST. Los datos de los clientes se pueden consultar, crear y eliminar, y se procesan utilizando WebSockets para un flujo de datos en tiempo real.

# Proyecto HashingID

## Descripción

HashingID es una aplicación que gestiona clientes a través de una API REST. Los datos de los clientes se pueden consultar, crear y eliminar, y se procesan utilizando WebSockets para un flujo de datos en tiempo real.

## Instalación

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/sherckuith/HashingID.git
Navega al directorio del proyecto:
bash
  cd HashingID
Levanta los contenedores de Docker:
bash
  docker-compose up --build
Accede a la API en tu navegador o Postman usando la URL:
http
  http://localhost:5000


##Uso con Postman

A continuación se explica cómo usar Postman para interactuar con la API de MrJoy, incluyendo cómo crear, consultar y eliminar clientes. Asegúrate de que el servicio está corriendo antes de realizar las peticiones.

### Endpoints
#### 1. GET /clientes
  Descripción: Obtiene todos los clientes registrados.
  Método: GET
  URL: http://localhost:5000/clientes
  Respuesta Esperada:
    json
        [
          {
            "id": 1,
            "name": "Juan Perez",
            "ci": "1234567890",
            "phone": "0999999999",
            "city": "Quito",
            "local": "Local 1",
            "email": "juanperez@example.com",
            "points": 10,
            "hash_id": "hashedvalue",
            "validador": false
          },
          ...
        ]

#### 2. POST /clientes
  Descripción: Crea un nuevo cliente.
  Método: POST
  URL: http://localhost:5000/clientes
  Body (JSON):
    json
        {
          "name": "Carlos Lopez",
          "ci": "1102345678",
          "phone": "0987654321",
          "city": "Guayaquil",
          "local": "Local 2",
          "email": "carlos@example.com",
          "points": 20
        }
 
  Respuesta Esperada:
    json
      {
        "message": "Cliente creado con éxito.",
        "client": {
          "id": 1,
          "name": "Carlos Lopez",
          "ci": "1102345678",
          "phone": "0987654321",
          "city": "Guayaquil",
          "local": "Local 2",
          "email": "carlos@example.com",
          "points": 20,
          "hash_id": "hashedvalue",
          "validador": false
        }
      }

#### 3. DELETE /clientes/{id}
  Descripción: Elimina un cliente por su id.
  Método: DELETE
  URL: http://localhost:5000/clientes/{id}
  Reemplaza {id} con el id del cliente que deseas eliminar.
  Respuesta Esperada:
    json
      {
        "message": "Cliente eliminado con éxito."
      }

## Usando Postman
   Para interactuar con la API utilizando Postman:

Importa la colección de Postman: Si deseas importar una colección de Postman, puedes hacerlo desde la opción "Import" y cargar el archivo .json de la colección que te proporcionamos. Esto configurará los endpoints de la API automáticamente.

  Realizar una solicitud GET:
    Abre Postman.
    Selecciona el método GET.
    En la barra de URL, ingresa http://localhost:5000/clientes.
    Haz clic en "Send".
    La respuesta debería mostrarte todos los clientes registrados en la base de datos.

  Crear un nuevo cliente:
    En Postman, selecciona el método POST.
    Ingresa la URL http://localhost:5000/clientes.
    En la pestaña "Body", selecciona raw y luego elige el tipo JSON.
    Pega el siguiente JSON:
      json
        {
          "name": "Carlos Lopez",
          "ci": "1102345678",
          "phone": "0987654321",
          "city": "Guayaquil",
          "local": "Local 2",
          "email": "carlos@example.com",
          "points": 20
        }
    Haz clic en "Send".
    La respuesta debería confirmar que el cliente ha sido creado correctamente.


## Eliminar un cliente:

    En Postman, selecciona el método DELETE.
    Ingresa la URL http://localhost:5000/clientes/{id}, reemplazando {id} con el id del cliente que deseas eliminar.
    Haz clic en "Send".
    La respuesta debería confirmar que el cliente ha sido eliminado.

## Estructura de la API
    La API está estructurada de la siguiente manera:

### GET /clientes: Devuelve una lista de todos los clientes en la base de datos.
### POST /clientes: Recibe un JSON con los datos del cliente y lo agrega a la base de datos.
### DELETE /clientes/{id}: Elimina un cliente especificado por su id.


## Lógica del Sistema

    Entrada: Los datos de los clientes pueden ser recibidos a través de una petición POST /clientes o mediante la ejecución del script req_data.py, que también solicita los datos del cliente y los envía al backend.

    Proceso: El servidor genera un hash_id único para cada cliente utilizando el archivo encoder_ws.py. Este hash es utilizado para validar y almacenar de manera segura la información del cliente.

    Salida: El servidor responde con el estado de la operación (éxito o fallo) y los datos guardados, como el id del cliente generado y el hash_id asignado.

## Postman Collection
    Si prefieres importar la colección de Postman para tener una configuración más rápida, sigue estos pasos:

      Haz clic en "Import" en Postman.
      Selecciona el archivo .json de la colección proporcionado.
      Todos los endpoints de la API estarán listos para ser usados.

## Explicación del Sistema

    El archivo req_data.py permite solicitar datos al usuario y enviarlos a través de WebSockets para interacción en tiempo real. Asegúrate de que VOLTA_HOST esté correctamente configurado en la red, y que el puerto 5000 esté abierto para la comunicación.
