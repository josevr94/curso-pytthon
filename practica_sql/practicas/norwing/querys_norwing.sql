-- Active: 1725459882056@@127.0.0.1@5432@norwing
-- Insertar un nuevo cliente
-- Insertar un nuevo empleado
-- Insertar un nuevo producto
-- Consultar todos los clientes
-- Consultar clientes por país
-- Consultar empleados y sus títulos
-- Consultar productos con stock bajo
-- Actualizar la dirección de un cliente
-- Actualizar el precio de un producto
-- Eliminar un cliente
-- Consultar pedidos con detalles del cliente
-- Consultar detalles de los pedidos junto con información del producto
-- Consultar clientes de una región específica
-- Total de ventas (suma de precios unitarios) por pedido
-- Promedio de precios unitarios de los productos
-- Precio máximo y mínimo de productos
-- Contar el número de productos en cada categoría
-- Total de ventas por cliente
-- Consultar productos cuyo nombre contiene 'Widget'
-- Consultar pedidos realizados por ciertos clientes
-- Consultar productos ordenados por precio descendente
-- Consultar clientes ordenados por nombre de la empresa


INSERT INTO public.customers
VALUES('ARA','jose spa', 'jose_luis', 'Owner', 'avs. paine_334', 'santiago',' metropolitana', 897774, 'chile', 569500599965, 090943848);

INSERT INTO public.employees
VALUES(10,'reyes','jose luis','junior','Mr.',1994-10-27,1994-10-27,'paine colonias 49','santiago','metropolitana',90838383,'chile',23329949,2344,'\x','hola que tal',5)

SELECT  first_name
FROM public.employees

SELECT country
FROM public.employees

SELECT first_name,title
FROM public.employees

SELECT MIN(units_in_stock) as menor_cantidad
FROM public.products

SELECT MAX(units_in_stock) as mayor_cantidad
FROM public.products

UPDATE customers
SET company_name = 'jose luis spa'
WHERE customer_id = 'ARA' 

UPDATE products
SET unit_price = 300 
WHERE product_id = 76

SELECT customers.company_name,customers.contact_name,orders.ship_name,orders.ship_city
FROM public.orders JOIN public.customers ON customers.customer_id = orders.customer_id

SELECT od.unit_price as precio_unidad,od.quantity as cantidad,p.product_name as nombre_producto
FROM public.order_details od JOIN public.products p on p.product_id = od.product_id

-- Total de ventas (suma de precios unitarios) por pedido
SELECT order_id, SUM(unit_price * quantity) AS total_sales
FROM order_details
GROUP BY order_id;
 
-- hacer join con costumer para obtener el nombre
 
-- Promedio de precios unitarios de los productos
SELECT AVG(unit_price) AS average_price
FROM products;
 
-- Precio máximo y mínimo de productos
SELECT MAX(unit_price) AS max_price, MIN(unit_price) AS min_price
FROM products;
 
-- Contar el número de productos en cada categoría
SELECT category_id, COUNT(*) AS product_count
FROM products
GROUP BY category_id;
 
SELECT c.company_name, SUM(od.unit_price * od.quantity) AS total_sales
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.company_name; 

SELECT c.contact_name, o.order_id, SUM(od.unit_price * od.quantity) AS total_sales
FROM order_details od
JOIN orders o ON o.order_id = od.order_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.contact_name, o.order_id;