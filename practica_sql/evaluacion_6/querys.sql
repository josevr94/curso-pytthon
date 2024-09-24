-- Active: 1725459882056@@127.0.0.1@5432@empresa_evaluacion_4

-- Listar todos los arriendos con las siguientes columnas: Folio, Fecha, Días, ValorDia,
-- NombreCliente, RutCliente
SELECT a.folio, a.fecha, a.dias, a.valor_dia, c.nombre as nombre_cliente, c.rut as rut_cliente
FROM arriendo a
JOIN cliente c ON c.rut = a.cliente_rut


-- Listar los clientes sin arriendos
SELECT c.*
FROM public.cliente c
LEFT JOIN public.arriendo a ON c.rut = a.cliente_rut
WHERE a.folio IS NULL;

-- Liste RUT y Nombre de las tablas empresa y cliente
SELECT rut, nombre
FROM cliente
UNION
SELECT rut, nombre
FROM empresa

-- Liste la cantidad de arriendos por mes
SELECT count(folio) as arriendos_por_mes, date_part('month', fecha) as mes
FROM arriendo
GROUP BY date_part('month', fecha)