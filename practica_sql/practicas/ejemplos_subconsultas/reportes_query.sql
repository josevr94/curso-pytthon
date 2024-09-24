-- Active: 1725459882056@@127.0.0.1@5432@ejemplos_subconsultas

-- APRENDIENDO A TRBAJAR CON LAS SUBCONSULTAS: las subconsultas son querys donde usamos dos veces el SELECT y el FROM dentro de las misma query

-- encuentra los empleados que tiene el salario mas alto
SELECT nombre, salario 
FROM empleados
WHERE salario = (SELECT max(salario) FROM empleados)

--encontrar los empleados que ganan mas que el salario promedio de la empresa
SELECT nombre, salario
FROM empleados
WHERE salario > (SELECT avg(salario) FROM empleados)

-- encontrar los nombres de los departamentos donde el salario promedio de los empleados sea superios a 3000
SELECT nombre_departamento
FROM departamentos
WHERE id_departamento IN(SELECT id_departamento from empleados GROUP BY id_departamento
HAVING avg(salario) > 3000)


--contar cuantos empleados hay en cada departamento
SELECT nombre_departamento,(SELECT count(*) FROM empleados WHERE empleados.id_departamento = departamentos.id_departamento) as total_empleados
FROM departamentos
