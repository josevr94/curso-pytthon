BEGIN;

SAVEPOINT antes_transaccion;

UPDATE producto_id 
SET cantidad = cantidad -20
WHERE producto_id = 1

UPDATE producto_id 
SET cantidad = cantidad -10
WHERE producto_id = 2

INSERT INTO pedidos