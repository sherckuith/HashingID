# Dockerfile
FROM python:3.10-slim

# Configura la carpeta de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .  # Aquí no es necesario #/app, ya que todo se copia en /app

# Instalación de dependencias del sistema necesarias para asyncpg
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el script wait-for-it
COPY wait-for-it/wait-for-it.sh /usr/local/bin/wait-for-it

# Asegurarse de que el script wait-for-it sea ejecutable
RUN chmod +x /usr/local/bin/wait-for-it

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Establecer el PYTHONPATH
ENV PYTHONPATH=/app:/app/api

# Expone el puerto en el contenedor
EXPOSE 5000

# Comando de inicio
CMD ["wait-for-it", "mrjoy_db:5432", "--", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]

#Este es el comando principal que se ejecuta cuando el contenedor arranca. 
#wait-for-it verificará que el contenedor de la base de datos (mrjoy_db) esté disponible en el 
#puerto 5432 antes de ejecutar el comando de inicio de la aplicación uvicorn.
