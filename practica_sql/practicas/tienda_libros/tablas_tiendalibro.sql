-- Active: 1725459882056@@127.0.0.1@5432@tienda_libros
CREATE TABLE autores (
    id_autor SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    nacionalidad VARCHAR(50)
);

-- Crear la tabla de libros
CREATE TABLE libros (
    id_libro SERIAL PRIMARY KEY,
    titulo VARCHAR(150),
    precio NUMERIC(10, 2),
    id_autor INT REFERENCES autores(id_autor),
    fecha_publicacion DATE
);

-- Crear la tabla de ventas
CREATE TABLE ventas (
    id_venta SERIAL PRIMARY KEY,
    id_libro INT REFERENCES libros(id_libro),
    cantidad INT,
    fecha_venta DATE
);

-- Insertar datos en la tabla de autores
INSERT INTO autores (nombre, nacionalidad) VALUES
('Gabriel García Márquez', 'Colombiana'),
('Isabel Allende', 'Chilena'),
('J.K. Rowling', 'Británica'),
('Jorge Luis Borges', 'Argentina');

-- Insertar datos en la tabla de libros
INSERT INTO libros (titulo, precio, id_autor, fecha_publicacion) VALUES
('Cien años de soledad', 25.99, 1, '1967-05-30'),
('El amor en los tiempos del cólera', 20.99, 1, '1985-09-10'),
('La casa de los espíritus', 18.50, 2, '1982-09-20'),
('Harry Potter y la piedra filosofal', 15.99, 3, '1997-06-26'),
('Ficciones', 22.00, 4, '1944-06-15');

-- Insertar datos en la tabla de ventas
INSERT INTO ventas (id_libro, cantidad, fecha_venta) VALUES
(1, 3, '2023-01-15'),
(2, 5, '2023-02-20'),
(3, 2, '2023-01-18'),
(4, 10, '2023-03-25'),
(5, 1, '2023-01-10'),
(1, 4, '2023-03-05');