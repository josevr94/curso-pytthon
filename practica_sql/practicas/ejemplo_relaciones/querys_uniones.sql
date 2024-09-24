-- 1.- INNER JOIN: devuelve las filas que tiene coincidencias en ambas tablas 
SELECT c.customer_name, o.order_date
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id

-- 2.- FULL OUTER JOIN: este operador devuelve todas las filas cuando hay una coincidencia en una de las tablas  (mostrar todo lo que es posible)

SELECT c.customer_name, o.order_date
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id

-- 3.- LEFT JOIN: Devuelve todas las filas de la tabla izquierda y las coincidencias de la tabla derecha 
SELECT c.customer_name, o.order_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id

-- 4.- RIGTH JOIN: devuelve todas las filas de la tabla derecha y las coincidencias de la tabla izquierda 
SELECT c.customer_name, o.order_date
FROM customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id

--5.- FULL JOIN: devuelve todas las filas cuando hay una coincidencia en una de las tablas, incluyendo la fila que no coinciden en ninguna de las dos tablas 
SELECT c.customer_name, o.order_date
FROM customers c
FULL JOIN orders o ON c.customer_id = o.customer_id

--6.- INTERSECT: devuelve las filas comunes entre dos consultas
SELECT customer_id FROM customers
INTERSECT
SELECT customer_id FROM customers

-- 7.- producto cartesiando: todas las combinaciones posibles de fila 
SELECT c.customer_name, o.order_date
FROM customers c, orders o

--8.- UNION Combina los resultados de dos o mas consultas. Elimina los duplicados
--une dos tablas en una (en este caso las tablas no son muy parecidas por ende hay que rellenar con NULL as)
SELECT customer_name as name , 'Customer' as source, NULL as order_date
FROM customers
UNION
SELECT 'order' as name, 'order' as source, order_date
FROM orders;

--9.- MINUS o EXCEPT: Devuelve las filas que estan en la primera consulta pero no en la segunda 
-- en este caso devuelve 'david' quien no a realizado ninguna compra, este comando devuelve el cliente que no a realizad ninguna orden
SELECT customer_name FROM customers 
EXCEPT
SELECT customer_name FROM orders o JOIN customers c on  c.customer_id =o.customer_id