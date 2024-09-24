-- Active: 1725459882056@@127.0.0.1@5432@ejercicio_comprobacion_sesion3
-- Liste la cantidad de arriendos por mes


-- Listar todas ventas con las siguientes columnas: Folio, Fecha, Monto, NombreCliente,
-- RutCliente. 

SELECT folio, fecha, monto, fk_cliente_rut, (SELECT cliente.nombre FROM cliente GROUP BY nombre)
FROM venta  and cliente