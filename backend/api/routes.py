from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from .encoder_ws import generar_hash  # Función para generar el hash

router = APIRouter()

# Clase para validar los datos del cliente
class Cliente(BaseModel):
    name: str
    ci: str
    phone: str
    city: str
    local: str
    email: EmailStr
    puntos: int  # Campo obligatorio para los puntos del cliente

# Función para insertar cliente en la base de datos
async def insertar_cliente_en_db(name, ci, phone, city, local, email, hash_id, puntos):
    # Reemplaza esto con el código para interactuar con tu base de datos
    query = """
        INSERT INTO clientes (nombre, cedula, telefono, ciudad, local, email, hash_id, puntos)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
    """
    try:
        # Aquí debes usar tu librería de conexión a la base de datos, como asyncpg
        await database.execute(query, (name, ci, phone, city, local, email, hash_id, puntos))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al insertar cliente: {str(e)}")

# Ruta para crear un nuevo cliente
@router.post("/clientes")
async def crear_cliente(cliente: Cliente):
    # Generar hash único para el cliente
    hash_id = generar_hash(
        cliente.name, cliente.ci, cliente.phone,
        cliente.city, cliente.local, cliente.email
    )
    
    # Insertar cliente en la base de datos
    try:
        await insertar_cliente_en_db(
            cliente.name, cliente.ci, cliente.phone, cliente.city,
            cliente.local, cliente.email, hash_id, cliente.puntos
        )
        return {"message": "Cliente creado exitosamente", "hash_id": hash_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el cliente: {str(e)}")
