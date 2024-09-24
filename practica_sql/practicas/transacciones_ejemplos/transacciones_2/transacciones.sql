-- Active: 1725459882056@@127.0.0.1@5432@transacciones_2
BEGIN;
CREATE TABLE productos ( 
producto_id SERIAL PRIMARY KEY, 
nombre TEXT, 
cantidad INT 
);

CREATE TABLE pedidos ( 
pedido_id SERIAL PRIMARY KEY, 
producto_id INT, 
cantidad INT, 
fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

END;