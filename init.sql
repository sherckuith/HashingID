-- init.sql
CREATE TABLE IF NOT EXISTS CLIENTES (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    cedula VARCHAR(20),
    telefono VARCHAR(15),
    ciudad VARCHAR(50),
    local VARCHAR(50),
    email VARCHAR(100),
    puntos INT DEFAULT 0,
    hash_id VARCHAR(256),
    validador BOOLEAN DEFAULT FALSE
);
