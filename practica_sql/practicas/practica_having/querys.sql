-- Ejemplo 1: Productos con ventas totales superiores a 100 unidades
SELECT p.nombre, sum(v.cantidad) as total_vendido
FROM productos p
JOIN ventas v on p.id_producto = v.id_producto
GROUP BY p.nombre
HAVING sum(v.cantidad)> 100

-- Ejemplo 2: Categorías con ingresos superiores a $10,000
SELECT c.nombre_categoria, sum(v.cantidad * p.precio) as ingresos_totales
FROM productos p
JOIN ventas v ON p.id_producto = v.id_producto
JOIN categorias c ON p.id_categoria = c.id_categoria
GROUP BY c.nombre_categoria
HAVING sum(v.cantidad * p.precio) > 10000

-- Ejemplo 3: Proveedores con más de 5 productos registrados

SELECT prov.nombre_proveedor, count(p.id_producto) as productos_registro
FROM productos p
JOIN proveedores prov ON p.id_proveedor = prov.id_proveedor
GROUP BY nombre_proveedor
HAVING count(p.nombre)> 1


-- Ejemplo 4: Productos con un precio promedio de ventas superior a $50

SELECT p.nombre,AVG(p.precio) as precio_promedio
FROM productos p
GROUP BY p.nombre
HAVING AVG(p.precio) > 50

-- ###EXtract
-- Extraer el año de las ventas
select id_venta, fecha_venta, EXTRACT(YEAR FROM fecha_venta) 
from ventas

select id_venta, fecha_venta, DATE_PART('year', fecha_venta) as year
from ventas


-- Extraer el mes de las ventas
select id_venta, fecha_venta, EXTRACT(MONTH FROM fecha_venta) 
from ventas

select id_venta, fecha_venta, DATE_PART('month', fecha_venta) as mes
from ventas


-- Ventas realizadas en un mes específico
 SELECT id_venta, fecha_venta, cantidad
 from ventas
 where EXTRACT(MONTH FROM  fecha_venta) =8

--  agrupar ventas por anio
SELECT date_part('year', fecha_venta) as anio, COUNT(*) as total_ventas
from ventas
GROUP BY date_part('year', fecha_venta)
ORDER BY anio


-- Agrupor ventas por mes
SELECT date_part('month', fecha_venta) as mes, sum(v.cantidad * p.precio) as ingresos
from ventas v
JOIN productos p on  v.id_producto = p.id_producto
GROUP BY date_part('month', fecha_venta)
ORDER BY mes

-- Ventas realizadas en un año específico

-- Número de ventas por mes


-- Ingresos mensuales


-- #ejemplo de case when

-- Clasificar ventas en categorías de cantidad (Alta, media o Baja)
SELECT id_venta, cantidad, 
    CASE
        WHEN CANTIDAD > 100 THEN 'ALTA'
        WHEN CANTIDAD BETWEEN 50 AND 100 THEN 'Media'
        ELSE 'BAJA'
    END
from ventas

-- Ejemplo 2: Asignar descuentos según el precio del producto 10% productos  caro, 5% productos medios, 1% productos barato
SELECT nombre, precio, 
    CASE 
        WHEN  precio > 100 THEN  '10%'
        WHEN precio BETWEEN 50 AND 100 THEN '5% descuento'
        ELSE ' 1%'
    END as tipo_descuento
FROM productos

-- Ejemplo 3: Clasificar ventas por estación del año Invierno (6,7,8), Primavera(9,10,11), Verano(12,1,2), otono(3,4,5)

SELECT id_venta, fecha_venta,
    CASE 
        WHEN EXTRACT(MONTH FROM fecha_venta) IN (6,7,8)  THEN  'INVIERNO' 
        WHEN EXTRACT(MONTH FROM fecha_venta) IN (9,10,11)  THEN  'PRIMAVERA' 
        WHEN EXTRACT(MONTH FROM fecha_venta) IN (12,1,2)  THEN  'VERANO' 
        ELSE 'OTONO'
    END as Estacion
FROM ventas

-- Ejemplo 4: Calcular el estado del stock de productos Poco stock <10,  stock moderado 10 a 50,  stock alto > 50

SELECT nombre, cantidad,
    CASE 
        WHEN  CANTIDAD <10 THEN 'POCO STOCK' 
        WHEN CANTIDAD  BETWEEN 10  AND 50 THEN 'STOCK MODERADO'
        ELSE 'STOCK ALTO'
    END as estado_stock
from productos