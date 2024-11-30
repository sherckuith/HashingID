
import hashlib

def generar_hash(nombre, cedula, telefono, ciudad, local, correo):
    datos = f"{nombre}{cedula}{telefono}{ciudad}{local}{correo}"
    hash_object = hashlib.sha256(datos.encode())
    return hash_object.hexdigest()

# Ejemplo de uso
hash_usuario = generar_hash(
    nombre="FABIAN ORTIZ",
    cedula="123456789",
    telefono="593123456789",
    ciudad="01",
    local="001",
    correo="apm.micro@gmail.com"
)
print(f"Name: {nombre}")
print(f"CI: {cedula}")
print(f"Phone: {telefono}")
print(f"City: {ciudad}")
print(f"Local: {local}")
print(f"Email: {correo}")
print(f"ID: {hash_usuario}")
