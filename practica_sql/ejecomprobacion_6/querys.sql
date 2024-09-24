-- Active: 1725459882056@@127.0.0.1@5432@ejercicio_comprobacion_sesion3

-- Listar todos los vehículos que no han sido vendidos.
SELECT id_vehiculo as id_autos_no_vendidos FROM vehiculo
EXCEPT
SELECT fk_vehiculo_idvehiculo FROM venta

-- Listar todas las ventas de enero del 2020 con las columnas: Folio, FechaVenta,
-- MontoVenta, NombreCliente, RutCliente, Patente, NombreMarca, y Modelo.
SELECT ve.folio, ve.fecha, ve.monto, c.rut, c.nombre, v.patente, v.marca,v.modelo 
FROM venta ve
JOIN cliente c ON c.rut = ve.fk_cliente_rut
JOIN vehiculo v ON v.id_vehiculo = ve.fk_vehiculo_idvehiculo
WHERE EXTRACT(YEAR FROM fecha) = 2024

-- Sumar las ventas por mes y marca del año 2020    ### revisar #####
SELECT sum(monto),date_part('month', fecha) as mes
FROM venta
WHERE EXTRACT(YEAR FROM fecha) = 2024
GROUP BY date_part('month', fecha)
ORDER BY mes

SELECT  sum(v.monto), ve.marca 
FROM venta v
JOIN vehiculo ve  ON ve.id_vehiculo = v.fk_vehiculo_idvehiculo
WHERE EXTRACT(YEAR FROM fecha) = 2024
GROUP BY ve.marca

-- Listar Rut y Nombre de las tablas cliente y empresa.
SELECT rut, nombre
FROM empresa
UNION
SELECT rut, nombre
FROM cliente
