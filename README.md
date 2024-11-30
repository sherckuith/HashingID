# HashingID
HashingID es una aplicación que gestiona clientes a través de una API REST. Los datos de los clientes se pueden consultar, crear y eliminar, y se procesan utilizando WebSockets para un flujo de datos en tiempo real.

# Proyecto HashingID

## Descripción

HashingID es una aplicación que gestiona clientes a través de una API REST. Los datos de los clientes se pueden consultar, crear y eliminar, y se procesan utilizando WebSockets para un flujo de datos en tiempo real.

## Instalación

1. Clona el repositorio en tu máquina local:
   ```
   git clone https://github.com/sherckuith/HashingID.git
   ```

Navega al directorio del proyecto:

   ```
   cd HashingID
   ```
Levanta los contenedores de Docker:
   ```
  docker-compose up --build
   ```
Accede a la API en tu navegador o Postman usando la URL:
   ```
     http://localhost:5000
   ```

##Uso con Postman

A continuación se explica cómo usar Postman para interactuar con la API de MrJoy, incluyendo cómo crear, consultar y eliminar clientes. Asegúrate de que el servicio está corriendo antes de realizar las peticiones.

### Endpoints
#### 1. GET /clientes
  Descripción: Obtiene todos los clientes registrados.
  Método: GET
  URL: http://localhost:5000/clientes
  Respuesta Esperada:
    ```json
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
        ]```

#### 2. POST /clientes
  Descripción: Crea un nuevo cliente.
  Método: POST
  URL: http://localhost:5000/clientes
  Body (JSON):
    ```json
        {
          "name": "Carlos Lopez",
          "ci": "1102345678",
          "phone": "0987654321",
          "city": "Guayaquil",
          "local": "Local 2",
          "email": "carlos@example.com",
          "points": 20
        }```
 
  Respuesta Esperada:
    ```json
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
      }```

#### 3. DELETE /clientes/{id}
  Descripción: Elimina un cliente por su id.
  Método: DELETE
  ```
  URL: http://localhost:5000/clientes/{id}
   ```
  Reemplaza {id} con el id del cliente que deseas eliminar.
  Respuesta Esperada:
    ```json
      {
        "message": "Cliente eliminado con éxito."
      }
      ```

## Usando Postman
   Para interactuar con la API utilizando Postman:

Importa la colección de Postman: Si deseas importar una colección de Postman, puedes hacerlo desde la opción "Import" y cargar el archivo .json de la colección que te proporcionamos. Esto configurará los endpoints de la API automáticamente.

  Realizar una solicitud GET:
    Abre Postman.
    Selecciona el método GET.
    En la barra de URL, ingresa ``` http://localhost:5000/clientes ```
    Haz clic en "Send".
    La respuesta debería mostrarte todos los clientes registrados en la base de datos.

  Crear un nuevo cliente:
    En Postman, selecciona el método POST.
    Ingresa la URL ``` http://localhost:5000/clientes ```
    En la pestaña "Body", selecciona raw y luego elige el tipo JSON.
    Pega el siguiente JSON:
      ```json
        {
          "name": "Carlos Lopez",
          "ci": "1102345678",
          "phone": "0987654321",
          "city": "Guayaquil",
          "local": "Local 2",
          "email": "carlos@example.com",
          "points": 20
        }```
    Haz clic en "Send".
    La respuesta debería confirmar que el cliente ha sido creado correctamente.


## Eliminar un cliente:

   En Postman, selecciona el método DELETE.
   Ingresa la URL ```http://localhost:5000/clientes/{id}```, reemplazando {id} con el id del cliente que deseas eliminar.
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

# Comandos utiles

## Descargar el script wait-for-it
```
cd /home/VOLTA/mrjoy/backend
git clone https://github.com/vishnubob/wait-for-it.git
```

## Actualizar el Dockerfile para copiar wait-for-it
```
   # Dockerfile
      # Tu imagen base
      FROM python:3.9-slim
   # Establecer directorio de trabajo
      WORKDIR /app
   # Copiar los archivos necesarios al contenedor
      COPY . .
   # Copiar el script wait-for-it
      COPY wait-for-it/wait-for-it.sh /usr/local/bin/wait-for-it
   # Asegurarse de que el script wait-for-it sea ejecutable
      RUN chmod +x /usr/local/bin/wait-for-it
   # Instalar las dependencias
      RUN pip install --no-cache-dir -r requirements.txt
   # Exponer el puerto de la aplicación
      EXPOSE 5000
   # El comando para iniciar la aplicación
      CMD ["wait-for-it", "mrjoy_db:5432", "--", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "5000"]
```

## Para uso en la base de datos:

### 1. Instalar PostgreSQL localmente
   En Ubuntu/Debian:
   ```
   sudo apt update
   sudo apt install postgresql postgresql-contrib
   ```
   En Windows:
   Descargue el instalador desde PostgreSQL Downloads: https://www.postgresql.org/download/
   Siga el asistente y configure el usuario administrador (postgres) con una contraseña.

### 2. Iniciar PostgreSQL localmente:
   Linux
   ```
   sudo systemctl start postgresql
   ```
   Windows:
   El servicio debería iniciar automáticamente al completar la instalación.
   
### 3. Acceso al cliente psql:
```
psql -U postgres
```

## Tips basicos para resolver problemas comunes:

### Detener el proceso que está usando el puerto:
   1. Si el puerto está siendo usado por una instancia local de PostgreSQL, puedes detener ese proceso:
      ```
      sudo service postgresql stop
      ```
   3. O, si el proceso está corriendo de manera manual, puedes matarlo directamente:
      ```
      sudo kill <pid>
      ```
      Donde <pid> es el ID del proceso que está usando el puerto.
   5. Verificar qué proceso está utilizando el puerto 5432:
      ```
      sudo lsof -i :5432
      ```


## Para uso de dockers:

Actualizar Docker y docker-compose (opcional): 
   Actualice los repositorios:
   ```
      sudo apt-get update
      sudo apt-get install docker-ce docker-ce-cli containerd.io docker.io -y
      sudo apt install docker-compose -y
      docker-compose version  # Nota: Con guion en el comando
      sudo systemctl enable docker
      sudo systemctl start docker
   ```

Instalar la versión más actualizada de Docker Compose
   Siga estos pasos para descargar e instalar la última versión.
   1. Descargue el binario más reciente:
         ```
         sudo curl -SL "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
         ```
   2. Dé permisos de ejecución:
         ```
         sudo chmod +x /usr/local/bin/docker-compose
         ```
   3. Verifique la instalación:
         ```
         docker-compose --version
         ```
   4. Confirme la ubicación actual de Docker Compose:
         Como binario independiente (usualmente en /usr/local/bin/docker-compose).
            ```
            which docker-compose
            ```

Verifique la versión instalada:
```
docker --version
docker-compose --version
```

Para mostrar los contenedores en ejecución:
```
docker ps -a
```

Para eliminar contenedores que estan corriendo::
```
docker rm -f <CONTAINER_ID>
```

Forzar la detención de un Docker:
```
docker kill <CONTAINER_ID>
```

Detener el contenedor manualmente
```
docker stop <CONTAINER_ID>
```

Reinicio de Docker para liberar los puertos ocupados:
```
sudo systemctl restart docker
```

Eliminar contenedores y volúmenes existentes:
```
docker-compose down --volumes
docker-compose up --build -d
```

Reiniciar la construcción del contenedor:
```
docker-compose down --volumes --rmi all
docker-compose up --build -d
```

Verificar servicios activos:
   Después de levantar los servicios, verificar que estén corriendo con:
   ```
   docker-compose ps
```

Limpiar los contenedores actuales:
```
docker-compose down
```

Iniciar un servicio específico para depuración:
```
docker-compose up mrjoy_db
docker-compose up mrjoy_backend
```
Elimina la cache de los contenedores:
```
docker-compose build --no-cache
```

Testea la aplicacion usando pytest:
```
pip install pytest pytest-mock
pytest api/tests.py
pytest tests/test_routes.py
```

Ejecutar la aplicación FastAPI usando uvicorn de la siguiente manera:
```
uvicorn backend.api.main:app --reload
```

Crea volumenes:
```
docker volume create db_data
```

Verifica los volumenes 
``` ```

Da de baja los volumenes existentes:
```
docker-compose down --volumes
```

Verificar el contenido del Docker Build Context
```
docker build -t test-backend
```

Reconstruye los servicios y levanta los servicios:
```
docker-compose up --build
```

Reconstruye las imágenes:
```
docker-compose build
```

Limpia el caché de Docker
```
docker builder prune -a
```

Para obtener más detalles sobre la configuración y el estado de los contenedores:
```
docker inspect mrjoy_backend
```

Revisa los registros de los contenedores para identificar problemas específicos:
```
docker logs mrjoy_db
```
```
docker logs mrjoy_backend
```

Limpia los volúmenes si los datos podrían estar corruptos:
```
docker volume rm db_data
```

Detén y elimina los contenedores:
```
docker-compose down
```

Iniciar PostgreSQL solo:
```
docker-compose up mrjoy_db
```

Verifica que el contenedor está en ejecución y prueba la conectividad:
```
docker exec -it mrjoy_db psql -U admin -d mrjoy
```

Iniciar el backend:
```
docker-compose up mrjoy_backend
```

Verifica si el puerto 5432 está ocupado:
```
netstat -tuln | grep 5432
```

Revisa los registros del contenedor de PostgreSQL:
```
docker logs mrjoy_db
```

Inspeccionar qué está fallando en el backend:
```
docker logs mrjoy_backend
```

Para verificar que el backend se conecta a la base de datos, accede al contenedor mrjoy_backend:
```
docker exec -it mrjoy_backend bash
```

Prueba la conectividad con un ping
```
ping mrjoy_db
```

Verifica la conexión a PostgreSQL:
```
apt-get install -y postgresql-client
psql -h mrjoy_db -U postgres -d mrjoy
```


## Recomendaciones adicionales:
1. Permisos:
   Asegúrate de que el usuario VOLTA tenga permisos para ejecutar Docker sin necesidad de privilegios de root. Para ello, debes agregar a VOLTA al grupo docker si no lo has hecho ya:
   ```
   sudo usermod -aG docker USER
   ```
   Después de ejecutar este comando, es recomendable cerrar sesión y volver a iniciarla para que los cambios tomen efecto.
3. Verificar el path de docker-compose:
   Verifica que el path a docker-compose (/usr/local/bin/docker-compose) sea el correcto. Puedes hacerlo ejecutando:
   ```
   which docker-compose
   ```
   Si el comando no devuelve /usr/local/bin/docker-compose, ajusta la ruta en el archivo .service según corresponda.
5. Habilitar el servicio:
   Para que el servicio se inicie automáticamente al arrancar el sistema, habilita el servicio con:
   ```
   sudo systemctl enable docker-compose-app.service
   ```
7. Verificación del estado del servicio:
   Después de hacer estos cambios y habilitar el servicio, puedes verificar su estado con:
   ```
   sudo systemctl status docker-compose-app.service
   ```
9. Revisar logs si hay problemas:
   Si el servicio no se inicia correctamente, puedes revisar los logs del servicio con:
   ```
   sudo journalctl -u docker-compose-app.service
   ```


## Para que el dopcker se ejecute al iniciar el sistema:

   Docker puede configurarse para que se inicie automáticamente al arrancar el sistema operativo. Esto lo puedes hacer con el siguiente comando:
   ```
   sudo systemctl enable docker
   ```

   Crea un servicio docker-compose-app.service en /etc/systemd/system/docker-compose-app.service
   ```
   sudo nano /etc/systemd/system/docker-compose-app.service
   sudo nano /etc/systemd/system/backend.service

   ```

   Introduzca el siguiente contenido:
   ```
   docker-compose-app.service:
   [Unit]
   Description=Docker Compose Application
   After=docker.service
   Requires=docker.service

   [Service]
   WorkingDirectory=/home/USUARIO/HashingID
   ExecStart=/usr/local/bin/docker-compose up -d
   ExecStop=/usr/local/bin/docker-compose down
   Restart=always
   User=USUARIO

   [Install]
   WantedBy=multi-user.target


   backend.service:
   [Unit]
   Description=Docker Compose Backend
   After=network.target
   
   [Service]
   Type=oneshot
   WorkingDirectory=/home/USUARIO/HashingID/backend
   ExecStart=/usr/bin/docker-compose up -d
   ExecStop=/usr/bin/docker-compose down
   RemainAfterExit=yes
   
   [Install]
   WantedBy=multi-user.target

   ```
   Explicacion de las dependencias de servicio:
   1. After=docker.service: Esto asegura que tu servicio docker-compose-app.service se inicie después de que Docker esté disponible.
   2. Requires=docker.service: Esto garantiza que el servicio Docker esté en funcionamiento antes de intentar iniciar el servicio Docker Compose. Si Docker no está disponible, este servicio no se iniciará.
   3. WorkingDirectory: El directorio de trabajo está configurado correctamente como /home/USUARIO/HashingID, que es donde está el proyecto. Asegúrece de que este directorio contenga tu archivo docker-compose.yml.
   4. ExecStart: El comando para iniciar el servicio es correcto: /usr/local/bin/docker-compose up -d. Esto ejecuta Docker Compose en segundo plano, como es necesario para mantener la aplicación en funcionamiento después de un reinicio del sistema.
   5. ExecStop: El comando de detención también está correcto: /usr/local/bin/docker-compose down, que apagará y eliminará los contenedores al detener el servicio.
   6. Restart=always: Esta configuración asegura que el servicio Docker Compose se reinicie automáticamente si falla o se detiene. Esto es ideal si desea que sus aplicaciones Docker estén siempre disponibles.
   7. User=USUARIO: El servicio se ejecutará como el usuario USUARIO, lo cual es correcto si tienes permisos adecuados para acceder a Docker y a los directorios necesarios.
      
   ### Habilitar y arrancar el servicio de systemd:
   
   Una vez creado el archivo de servicio, recarga systemd y habilita el servicio para que se inicie automáticamente:
   Para docker-compose-app.service:
   ```
               sudo systemctl daemon-reload
               sudo systemctl enable docker-compose-app
               sudo systemctl start docker-compose-app
   ```
   Para backend.service:
   ```
               sudo systemctl restart backend.service
               sudo systemctl enable backend.service
               sudo systemctl start backend.service
   ```
      Esto garantiza que los contenedores de Docker se inicien automáticamente cuando el sistema operativo se reinicie.   
   Para proporcionar más información sobre por qué backend.service
   ```
            journalctl -xe
   ```

## Configurar Docker Compose para que los contenedores se inicien automáticamente.
   ```
      services:
         backend:
            restart: unless-stopped
   ```
   
   El valor restart: unless-stopped asegura que los contenedores se reinicien automáticamente, excepto si se detienen manualmente. Las opciones posibles para restart son:
   
      1. no: No reiniciar el contenedor (por defecto).
      2. always: Reiniciar el contenedor cuando Docker se reinicia.
      3. unless-stopped: Reiniciar el contenedor a menos que se haya detenido manualmente.


# Pruebas:
Ejecuta las pruebas dentro del contenedor: 
   Accede al contenedor backend:
   ```
      docker exec -it mrjoy_backend bash
   ```
   
   1. Ejecuta el script directamente:
      ```
      python /app/req_data.py
      ```
   2. Usando Pytest: Ejecuta pytest desde la raíz del proyecto o una carpeta específica:
      ```
      pytest
      #Si deseas más detalles en los resultados:
         pytest -v
      ```
   3. Verifica dentro del contenedor que el PYTHONPATH esté configurado correctamente:
      ```
      docker exec -it mrjoy_backend bash
      echo $PYTHONPATH
      ```
      El resultado debería incluir /app, /app/api, y /backend.
   4. Prueba la importación:
      ```
      python -c "import api.main"
      ```

   

      



