-- Active: 1725459882056@@127.0.0.1@5432@compras_ventas
-- Insertar datos en la tabla clientes
INSERT INTO public.clientes (nombre, ap_paterno, direccion) VALUES
('Ana Martínez', 'González', 'Calle de la Reforma 123, Ciudad de México'),
('Luis Fernández', 'Ramírez', 'Av. Juárez 456, Monterrey'),
('Carlos Pérez', 'López', 'Plaza Central 789, Guadalajara'),
('Sofía Morales', 'Jiménez', 'Calle del Carmen 234, Puebla'),
('Miguel Torres', 'Sánchez', 'Avenida de la Paz 567, León'),
('Claudia Ruiz', 'Vázquez', 'Calle 8 de Septiembre 345, Querétaro'),
('Alejandro Díaz', 'Moreno', 'Boulevard Constituyentes 678, San Luis Potosí'),
('Verónica Gómez', 'Cabrera', 'Avenida Juárez 890, Tijuana'),
('Roberto Martínez', 'Gómez', 'Calle 16 de Septiembre 101, Mérida'),
('Laura González', 'Aragón', 'Calle de los Plátanos 202, Chihuahua');

-- Insertar datos en la tabla productos
INSERT INTO public.productos (nombre, descripcion) VALUES
('Laptop Dell XPS 13', 'Laptop ultradelgada con procesador i7 y 16GB de RAM'),
('Smartphone Samsung Galaxy S23', 'Smartphone con pantalla AMOLED y 128GB de almacenamiento'),
('Auriculares Bose QuietComfort 45', 'Auriculares con cancelación de ruido'),
('Reloj Apple Watch Series 8', 'Reloj inteligente con monitoreo de salud y GPS'),
('Televisor LG OLED 55"', 'Televisor con tecnología OLED y resolución 4K'),
('Cámara Sony Alpha 7 IV', 'Cámara sin espejo con sensor full-frame'),
('Tablet iPad Air', 'Tablet con pantalla Retina y procesador M1'),
('Teclado mecánico Logitech G Pro', 'Teclado mecánico con retroiluminación RGB'),
('Altavoces Sonos One', 'Altavoces inteligentes con sonido de alta calidad'),
('Impresora HP OfficeJet Pro', 'Impresora multifunción con capacidad de escaneo y copia');

-- Insertar datos en la tabla tipo_transacciones
INSERT INTO public.tipo_transaciones (nombre, descripcion) VALUES
('Compra', 'Compra de productos'),
('Devolución', 'Devolución de productos'),
('Reparación', 'Servicio de reparación de productos'),
('Garantía', 'Servicio de garantía'),
('Suscripción', 'Compra de suscripción de servicios');

-- Insertar datos en la tabla transacciones
INSERT INTO public.transaciones (id_cliente, id_producto, id_tipo_transacion, fecha, precio, cantidad) VALUES
(1, 1, 1, '2024-01-15', 1200.00, 1),
(2, 2, 1, '2024-02-20', 899.99, 2),
(3, 3, 1, '2024-03-10', 299.99, 1),
(4, 4, 1, '2024-04-05', 399.99, 1),
(5, 5, 1, '2024-05-18', 1500.00, 1),
(6, 6, 1, '2024-06-22', 2500.00, 1),
(7, 7, 1, '2024-07-30', 749.99, 1),
(8, 8, 1, '2024-08-15', 149.99, 2),
(9, 9, 1, '2024-09-10', 120.00, 3),
(10, 10, 1, '2024-10-01', 349.99, 1),
(1, 2, 2, '2024-01-20', 899.99, 1),
(2, 3, 2, '2024-02-25', 299.99, 1),
(3, 4, 2, '2024-03-15', 399.99, 1),
(4, 5, 2, '2024-04-10', 1500.00, 1),
(5, 6, 2, '2024-05-25', 2500.00, 1),
(6, 7, 2, '2024-06-28', 749.99, 2),
(7, 8, 2, '2024-07-15', 149.99, 1),
(8, 9, 2, '2024-08-30', 120.00, 2),
(9, 10, 2, '2024-09-12', 349.99, 1),
(10, 1, 3, '2024-10-05', 1200.00, 1),
(1, 2, 3, '2024-11-02', 899.99, 1),
(2, 3, 3, '2024-11-15', 299.99, 1),
(3, 4, 3, '2024-12-01', 399.99, 1),
(4, 5, 3, '2024-12-20', 1500.00, 1),
(5, 6, 3, '2024-12-30', 2500.00, 1);
