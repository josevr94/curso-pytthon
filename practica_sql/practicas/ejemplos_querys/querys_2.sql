-- Active: 1725459882056@@127.0.0.1@5432@tienda2


SELECT productos.nombre, movimiento_stock.tipo_movimiento as Movimiento,movimiento_stock.cantidad
FROM movimiento_stock JOIN productos on productos.id = movimiento_stock.product_id

SELECT * 
from movimiento_stock
WHERE tipo_movimiento LIKE '%entrada%'

UPDATE productos
set stock = stock + 50
WHERE id =1

SELECT tipo_movimiento, sum(cantidad) as total 
from movimiento_stock
GROUP BY tipo_movimiento

SELECT AVG(precios) as precio_promedio
FROM productos

SELECT min(precios) as precio_minimo, max(precios) as precio_maximo
FROM productos