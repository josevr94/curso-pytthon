-- Active: 1725459882056@@127.0.0.1@5432@sistemas_pagos

SELECT nombre
from estudiantes

SELECT e.nombre
FROM estudiantes e  JOIN pago p on e.id = p.id_estudiantes