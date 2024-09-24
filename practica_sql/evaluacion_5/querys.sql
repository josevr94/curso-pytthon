-- Active: 1725459882056@@127.0.0.1@5432@peliculas

-- preguntar como enviar este trabajo---------------------------------------------------------------


SELECT pelicula, id 
FROM pelicula
WHERE pelicula.pelicula = 'Titanic'

-- Listar todos los actores que aparecen en la película "Titanic", indicando el título de la película,
-- año de estreno, director y todo el reparto.
SELECT actor FROM reparto 
WHERE id_pelicula = 2

-- Listar los 10 directores más populares, indicando su nombre y cuántas películas aparecen
-- en el top 100.
SELECT director, count(id)
FROM pelicula
GROUP BY director
ORDER BY count(id) DESC
LIMIT 10

-- Indicar cuántos actores distintos hay.
SELECT DISTINCT actor
FROM reparto
GROUP BY actor

-- Indicar las películas estrenadas entre los años 1990 y 1999 (ambos incluidos), ordenadas
-- por título de manera ascendente
SELECT pelicula,estreno
FROM pelicula
WHERE estreno BETWEEN 1990 and 1999
ORDER BY pelicula ASC

-- Listar los actores de la película más nueva.
SELECT actor, estreno
FROM pelicula JOIN reparto on reparto.id_pelicula = pelicula.id
WHERE estreno = (SELECT max(estreno) FROM pelicula)

-- Inserte los datos de una nueva película solo en memoria, y otra película en el disco duro
BEGIN;
SAVEPOINT antes;
INSERT INTO pelicula(id,pelicula,estreno,director)
VALUES(101,'Dune', 2021,'Denis Villeneuve');

ROLLBACK TO antes;

INSERT INTO pelicula(id,pelicula,estreno,director)
VALUES(101,'Dune 2', 2024,'Denis Villeneuve');

COMMIT;


-- Actualice 5 directores utilizando ROLLBACK
BEGIN;

SAVEPOINT antes;
UPDATE pelicula
SET director = 'Christopher Super Nolan'
WHERE id  = 6


UPDATE pelicula
SET director = 'Peter Super Jackson'
WHERE id  = 5


UPDATE pelicula
SET director = 'Miel Gibson'
WHERE id  = 9


UPDATE pelicula
SET director = 'Tim El loco Burton'
WHERE id  = 12

ROLLBACK to antes;

COMMIT;


-- Inserte 3 actores a la película “Rambo” utilizando SAVEPOINT

BEGIN;
SAVEPOINT antes;
INSERT INTO reparto
VALUES(72,'juanito perez')

INSERT INTO reparto
VALUES(72,'diego perez')

INSERT INTO reparto
VALUES(72,'pedro perez')

ROLLBACK to antes;

COMMIT;

-- Elimina las películas estrenadas el año 2008 solo en memoria.
BEGIN;
SAVEPOINT antes;

DELETE FROM pelicula 
WHERE estreno = 2008

ROLLBACK to antes;
COMMIT;

-- Inserte 2 actores para cada película estrenada el 2001.

SELECT p.id, p.estreno, r.actor, p.pelicula
FROM pelicula p JOIN reparto r on r.id_pelicula = p.id
WHERE p.estreno = 2001

BEGIN;
SAVEPOINT ANTES;

INSERT INTO reparto(id_pelicula,actor)
VALUES (13,'jose')


ROLLBACK TO ANTES;


-- Actualice la película “King Kong” por el nombre de “Donkey Kong”, sin efectuar cambios en
-- disco duro.

BEGIN;
SAVEPOINT antes;
UPDATE pelicula SET pelicula = 'Donkey Kong' WHERE pelicula = 'King Kong'

ROLLBACK to antes;
COMMIT; 