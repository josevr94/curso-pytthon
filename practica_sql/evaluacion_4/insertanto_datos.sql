-- Active: 1725459882056@@127.0.0.1@5432@empresa_evaluacion_4

-- insertando una empresa
INSERT INTO empresa (rut, nombre, direccion, telefono, correo, web)
VALUES('77345343-9', 'pez dorado', 'calle redonda 8883', '9983728239', 'evaluacion@sesion4.com', 'www.pez_dorado.com')

-- insertando 5 herramientas

INSERT INTO herramienta(id_herramienta, nombre, precio_dia)
VALUES(2233443, 'motocierra', 5000)

INSERT INTO herramienta(id_herramienta, nombre, precio_dia)
VALUES(2233448, 'taladro', 2000)

INSERT INTO herramienta(id_herramienta, nombre, precio_dia)
VALUES(2233449, 'cortadora de pasto', 10000)

INSERT INTO herramienta(id_herramienta, nombre, precio_dia)
VALUES(2233444, 'carretilla', 1000)

INSERT INTO herramienta(id_herramienta, nombre, precio_dia)
VALUES(2233567, 'horilladora', 6000)


-- insertando 3 clientes
INSERT INTO cliente(rut, nombre, correo, direccion, celular)
VALUES('10934399-8', 'juan perez', 'juanperez@gmail.com', 'calle juan perez, santiago', '993843277')

INSERT INTO cliente(rut, nombre, correo, direccion, celular)
VALUES('13934399-3', 'andres rodriguez', 'andres_rodriguez@gmail.com', 'santan rosa n 199, santiago', '7243773434')

INSERT INTO cliente(rut, nombre, correo, direccion, celular)
VALUES('16934399-7', 'diego hernandez', 'diegoh@gmail.com', 'lastarria n 546, santiago', '56734852323')


-- borrando al ultimo cliente
DELETE FROM cliente WHERE cliente.rut = '16934399-7'

-- eliminando la primera herramienta
DELETE FROM herramienta WHERE id_herramienta = 2233443


-- insertar 2 arriendo para cada cliente
-- cliente 1
INSERT INTO arriendo(folio, fecha, dias, valor_dia, garantia, herramienta_id_herrramienta, cliente_rut)
VALUES(5557774, '10/12/2023', 5 ,6000, '30 dias', 2233567, '10934399-8' )

INSERT INTO arriendo(folio, fecha, dias, valor_dia, garantia, herramienta_id_herrramienta, cliente_rut)
VALUES(5557456, '11/10/2023', 10 ,10000, '30 dias', 2233449, '10934399-8' )

-- cliente 2
INSERT INTO arriendo(folio, fecha, dias, valor_dia, garantia, herramienta_id_herrramienta, cliente_rut)
VALUES(6655446, '23/07/2023', 20 ,1000, '30 dias', 2233444, '13934399-3' )

INSERT INTO arriendo(folio, fecha, dias, valor_dia, garantia, herramienta_id_herrramienta, cliente_rut)
VALUES(5558876, '15/09/2023', 11 ,2000, '30 dias', 2233448, '13934399-3' )


-- modificar el correo del primero cliente
UPDATE cliente
SET correo = 'juanperez2@gmail.com'
WHERE cliente.rut = '10934399-8'

-- lista herramientas
SELECT herramienta.nombre
FROM herramienta

-- lista arriendos del segundo cliente
SELECT *
FROM arriendo
WHERE arriendo.cliente_rut = '13934399-3'

-- lista clientes cuyo nombre tenga una A
SELECT c.nombre as nombres_con_A
FROM cliente c
WHERE c.nombre LIKE '%a%';

-- obtener el nombre de la segunda herramienta insertada
SELECT herramienta.nombre
FROM herramienta
LIMIT 1 OFFSET 1

-- cambiando fecha de los dos primeros arriendos 
UPDATE arriendo
SET fecha = '2020/01/15'
WHERE folio = 5557774 AND  folio = 5557456

SELECT a.folio, a.fecha, a.valor_dia
FROM arriendo a
WHERE EXTRACT(MONTH FROM a.fecha) = '10'


