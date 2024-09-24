-- Mostrar todos los pacientes con la información de su médico y el tratamiento recibido: 
SELECT p.nombre, m.nombre, t.descripcion
FROM citas c 
INNER JOIN pacientes p ON  p.pacienteid = c.pacienteid
INNER JOIN medicos m ON m.medicoid = c.medicoid
INNER JOIN tratamientos t ON t.citaid = c.citaid

-- Mostrar todos los pacientes y, si tienen, el tratamiento recibido y el nombre del médico: 
SELECT p.nombre,t.descripcion,m.nombre
FROM pacientes p
LEFT JOIN citas c ON c.pacienteid = p.pacienteid
LEFT JOIN tratamientos t ON t.citaid = c.citaid
LEFT JOIN medicos m ON m.medicoid = c.medicoid

-- Mostrar todos los tratamientos y, si existen, la información del paciente y del médico: 
SELECT t.descripcion,p.nombre,m.nombre
FROM tratamientos t 
RIGHT JOIN citas c ON c.citaid = t.citaid
RIGHT JOIN pacientes p on p.pacienteid = c.pacienteid
RIGHT JOIN medicos m ON m.medicoid = c.medicoid

-- Mostrar todas las combinaciones posibles de pacientes y médicos: 
SELECT p.nombre,m.nombre
FROM pacientes p 
CROSS JOIN medicos m

-- Mostrar todos los nombres de pacientes y médicos (sin duplicados):
SELECT p.nombre FROM pacientes p
UNION
SELECT m.nombre  FROM medicos m

-- Mostrar los nombres que están tanto en la tabla de pacientes como en la
-- tabla de médicos (aunque en este caso, no deberíamos tener nombres comunes
-- entre pacientes y médicos):
SELECT p.nombre FROM pacientes p
INTERSECT
SELECT m.nombre FROM medicos m

-- Mostrar los nombres de pacientes que no están en la tabla de médicos (en
-- este caso, debería mostrar todos los pacientes porque no compartimos
-- nombres entre las tablas):
SELECT p.nombre  FROM pacientes p
EXCEPT
SELECT m.nombre FROM medicos m JOIN citas c on c.medicoid = c.pacienteid

-- Mostrar los pacientes cuyo cumpleaños es en el mismo mes que la fecha
-- actual:
SELECT p.nombre,p.fechanacimiento
FROM pacientes p
WHERE EXTRACT(DAY FROM p.fechanacimiento) = 15

-- Mostrar todos los nombres de pacientes y los ID de citas:
SELECT p.nombre as NAME, 'nombre'as ID, p.pacienteid FROM pacientes p
UNION
SELECT 'ID_citas' as NAME, 'Id_citas' as ID, c.citaid FROM citas c

-- Mostrar los nombres que se encuentran tanto en pacientes como en médicos
-- (esperamos que esté vacío si no hay nombres comunes):
SELECT pacientes.nombre FROM pacientes
INTERSECT 
SELECT medicos.nombre FROM medicos

-- Mostrar nombres de pacientes que no tienen tratamiento registrado (esto
-- asume que todos los pacientes con citas tienen tratamientos registrados,
-- por lo que debería estar vacío):
SELECT p.nombre FROM pacientes p
EXCEPT
SELECT t.descripcion FROM tratamientos t JOIN citas c ON c.citaid = c.pacienteid
