-- Active: 1725459882056@@127.0.0.1@5432@biblioteca@public

update 
    libros 
  set 
    isbn = 777
where 
    id = 2

update categoria
set descripcion = 'fantasia y magia '
WHERE
id = 2

select * from libros
order by titulo ASC

DELETE  from libros
where id =2

select min(publicacion)
from libros

select max(publicacion)
from libros

select count(publicacion)
from libros

select titulo, autores.nombre, autores.nacionalidad
from libros INNER JOIN autores ON libros.id_autor  = autores.id --el join me muestra los elementos id que tenemos en nuestra tabla libros , nos permite unir la informacion de las tablas que estan conectadas con llaves foraneas

SELECT titulo,categoria.nombre
FROM libros INNER JOIN categoria ON libros.id_categoria = categoria.id
WHERE libros.id =1

update 
  libros 
set 
  titulo = titulo,
  id_autor = id_autor,
  isbn = isbn,
  publicacion = publicacion,
  id_categoria = id_categoria
where 
  id = 'id';