-- Escribe una consulta que devuelva todos los libros cuyos precios estén por encima del precio promedio de los libros de la misma nacionalidad del autor.

SELECT titulo, precio
FROM libros
where precio > (SELECT AVG(precio) FROM libros)

-- Escribe una consulta que muestre el título del libro, su precio, y el número total de ventas para ese libro. Usa una subconsulta en la cláusula SELECT para calcular el número total de ventas por libro. 
SELECT titulo, precio, (SELECT sum(cantidad) FROM ventas WHERE ventas.id_libro = libros.id_libro) as total_ventas
FROM libros

-- Escribe una consulta que muestre el nombre de los autores que han publicado al menos un libro cuyo precio sea mayor que el precio promedio de todos los libros de ese mismo autor.
SELECT DISTINCT nombre
FROM autores
JOIN libros on libros.id_autor = autores.id_autor
WHERE libros.precio > (SELECT AVG(precio) FROM libros WHERE autores.id_autor = libros.id_autor)


-- Escribe una consulta que muestre el nombre de los autores y el total de ventas de libros de cada autor, usando una subconsulta en la cláusula FROM para calcular las ventas por autor.
SELECT a.nombre, sum(v.cantidad)
FROM autores a 
JOIN (SELECT sum(v.cantidad) FROM ventas v )