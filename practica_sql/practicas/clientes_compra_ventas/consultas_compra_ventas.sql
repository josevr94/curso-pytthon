-- Active: 1725459882056@@127.0.0.1@5432@compras_ventas

-- REPORTES 

-- ventas por clientes
SELECT clientes.nombre,count(transaciones.id_cliente),sum(transaciones.precio)
FROM transaciones  JOIN clientes on clientes.id = transaciones.id_cliente
WHERE transaciones.id_tipo_transacion = 2 OR transaciones.id_tipo_transacion = 27
GROUP BY clientes.nombre

-- compras por clientes
SELECT clientes.id,clientes.nombre,count(transaciones.id_cliente) as numero_compras, sum(transaciones.precio) as total_compras
FROM transaciones JOIN clientes on clientes.id = transaciones.id_cliente
GROUP BY clientes.id

-- reporte clientes con ventas y compras
SELECT productos.nombre, 
count(transaciones.id_producto) as cantidad_transacciones,
sum(transaciones.precio) as total_venta
FROM transaciones 
join productos on productos.id = transaciones.id_producto
GROUP BY productos.nombre
