-- Active: 1725459882056@@127.0.0.1@5432@empresa
CREATE DATABASE empresa
BEGIN;

CREATE TABLE IF NOT EXISTS departamentos
(
    departamento_id SERIAL NOT NULL,
    nombre CHARACTER(100) NOT NULL,
    ubicacion CHARACTER(100) NOT NULL,
    PRIMARY KEY (departamento_id)
);

SAVEPOINT tabla_2;

CREATE TABLE IF NOT EXISTS empleados
(
    empleados_id SERIAL NOT NULL,
    nombre CHARACTER(100) NOT NULL,
    puesto CHARACTER(100) NOT NULL,
    salario NUMERIC(10,2) NOT NULL,
    fecha_contratacion DATE,
    departamento_id SERIAL,
    PRIMARY KEY (empleados_id),
    Foreign Key (departamento_id) REFERENCES departamentos(departamento_id)
);

ROLLBACK to tabla_2;

END;


BEGIN;


ALTER TABLE empleados ADD correo_electronico CHARACTER(100) NOT NULL;


ALTER TABLE empleados RENAME to trabajadores;

SAVEPOINT antes_de_eliminar;

DROP TABLE trabajadores;


ROLLBACK to antes_de_eliminar;

END;
