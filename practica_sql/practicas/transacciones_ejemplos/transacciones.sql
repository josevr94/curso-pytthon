-- Active: 1725459882056@@127.0.0.1@5432@transacciones_ejemplos
CREATE TABLE cuentas (
    cuenta_id SERIAL PRIMARY KEY,
    nombre TEXT,
    saldo DECIMAL
);
 
CREATE TABLE transacciones (
    transaccion_id SERIAL PRIMARY KEY,
    desde_cuenta_id INT,
    hacia_cuenta_id INT,
    monto DECIMAL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
 