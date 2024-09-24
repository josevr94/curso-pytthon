-- Active: 1725459882056@@127.0.0.1@5432@empresa_evaluacion_4
BEGIN;

-- Insertar 10 datos en la tabla cliente
INSERT INTO public.cliente (rut, nombre, correo, direccion, celular) VALUES
('11111111-1', 'Carlos Ruiz', 'carlos.ruiz@example.com', 'Calle 1, N° 10', '999999999'),
('22222222-2', 'María Lopez', 'maria.lopez@example.com', 'Calle 2, N° 20', '888888888'),
('33333333-3', 'Pedro Martínez', 'pedro.martinez@example.com', 'Calle 3, N° 30', '777777777'),
('44444444-4', 'Lucía Fernández', 'lucia.fernandez@example.com', 'Calle 4, N° 40', '666666666'),
('55555555-5', 'Javier Torres', 'javier.torres@example.com', 'Calle 5, N° 50', '555555555'),
('66666666-6', 'Sofía Herrera', 'sofia.herrera@example.com', 'Calle 6, N° 60', '444444444'),
('77777777-7', 'Diego Sánchez', 'diego.sanchez@example.com', 'Calle 7, N° 70', '333333333'),
('88888888-8', 'Claudia Morales', 'claudia.morales@example.com', 'Calle 8, N° 80', '222222222'),
('99999999-9', 'Andrés Díaz', 'andres.diaz@example.com', 'Calle 9, N° 90', '111111111'),
('10101010-1', 'Gabriela Castillo', 'gabriela.castillo@example.com', 'Calle 10, N° 100', '000000000');

-- Insertar 10 datos en la tabla empresa
INSERT INTO public.empresa (rut, nombre, direccion, telefono, correo, web) VALUES
('33333333-3', 'Construcciones ABC', 'Calle 11, N° 110', '321321321', 'contacto@construccionesabc.cl', 'www.construccionesabc.cl'),
('44444444-4', 'Servicios Técnicos', 'Calle 12, N° 120', '654654654', 'info@serviciostecnicos.cl', 'www.serviciostecnicos.cl'),
('55555555-5', 'Alquiler de Maquinaria', 'Calle 13, N° 130', '987987987', 'contacto@alquilerdemaquinaria.cl', 'www.alquilerdemaquinaria.cl'),
('66666666-6', 'Herramientas y Más', 'Calle 14, N° 140', '345345345', 'ventas@herramientasymas.cl', 'www.herramientasymas.cl'),
('77777777-7', 'Proveedores de Obras', 'Calle 15, N° 150', '567567567', 'info@proveedoresdeobras.cl', 'www.proveedoresdeobras.cl'),
('88888888-8', 'Equipos y Servicios', 'Calle 16, N° 160', '789789789', 'contacto@equiposyservicios.cl', 'www.equiposyservicios.cl'),
('99999999-9', 'Maquinaria y Herramientas', 'Calle 17, N° 170', '123123123', 'info@maquinariayherramientas.cl', 'www.maquinariayherramientas.cl'),
('10101010-1', 'Alquiler de Equipos', 'Calle 18, N° 180', '456456456', 'contacto@alquilerequipos.cl', 'www.alquilerequipos.cl'),
('20202020-2', 'Suministros de Construcción', 'Calle 19, N° 190', '789456123', 'info@suministrosdeconstruccion.cl', 'www.suministrosdeconstruccion.cl'),
('30303030-3', 'Servicios de Mantenimiento', 'Calle 20, N° 200', '321654987', 'contacto@serviciosdemantenimiento.cl', 'www.serviciosdemantenimiento.cl');

-- Insertar 10 datos en la tabla herramienta
INSERT INTO public.herramienta (id_herramienta, nombre, precio_dia) VALUES
(4, 'Lijadora', 6000),
(5, 'Compresor', 8000),
(6, 'Escuadra', 1500),
(7, 'Cortadora de Azulejos', 9000),
(8, 'Generador Eléctrico', 12000),
(9, 'Nivel Láser', 7500),
(10, 'Mezcladora', 10000),
(11, 'Pistola de Calor', 5000),
(12, 'Taladro de Percusión', 11000),
(13, 'Cortadora de Césped', 8500);

-- Insertar 10 datos en la tabla arriendo
INSERT INTO public.arriendo (folio, fecha, dias, valor_dia, garantia, herramienta_id_herrramienta, cliente_rut) VALUES
(3, '2023-09-05', 7, 6000, 'Garantía 3', 4, '11111111-1'),
(4, '2023-09-15', 4, 8000, 'Garantía 4', 5, '22222222-2'),
(5, '2023-09-20', 2, 1500, 'Garantía 5', 6, '33333333-3'),
(6, '2023-09-25', 1, 9000, 'Garantía 6', 7, '44444444-4'),
(7, '2023-09-30', 3, 12000, 'Garantía 7', 8, '55555555-5'),
(8, '2023-10-02', 5, 7500, 'Garantía 8', 9, '66666666-6'),
(9, '2023-10-05', 6, 10000, 'Garantía 9', 10, '77777777-7'),
(10, '2023-10-10', 4, 5000, 'Garantía 10', 11, '88888888-8'),
(11, '2023-10-15', 8, 11000, 'Garantía 11', 12, '99999999-9'),
(12, '2023-10-20', 2, 8500, 'Garantía 12', 13, '10101010-1');

END;

BEGIN;

-- Insertar clientes sin arriendo
INSERT INTO public.cliente (rut, nombre, correo, direccion, celular) VALUES
('12121212-1', 'Felipe Morales', 'felipe.morales@example.com', 'Calle Verde 1', '999888777'),
('13131313-1', 'Valentina Ríos', 'valentina.rios@example.com', 'Calle Azul 2', '888777666'),
('14141414-1', 'Nicolás Paredes', 'nicolas.paredes@example.com', 'Calle Amarilla 3', '777666555'),
('15151515-1', 'Teresa Bravo', 'teresa.bravo@example.com', 'Calle Roja 4', '666555444'),
('16161616-1', 'Eduardo López', 'eduardo.lopez@example.com', 'Calle Rosa 5', '555444333');

END;
