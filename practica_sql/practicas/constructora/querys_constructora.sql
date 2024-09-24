-- nombre_proyecto  total_presupuesto
-- Proyecto B   800,000
-- Proyecto C   600,000
-- Proyecto D   1,200,000


SELECT p.nombre_proyecto,sum(pd.presupuesto)
FROM proyectos p
JOIN proyecto_detalle pd ON pd.id_proyecto = p.id
GROUP BY p.nombre_proyecto
HAVING sum(pd.presupuesto) > 80000

-- EXTRACT: Clasifica proyectos cuanto se iniciaron por mes
SELECT count(pd.id_proyecto) as proyectos, EXTRACT(MONTH FROM fecha_inicio) as mes
FROM proyecto_detalle pd
GROUP BY EXTRACT(MONTH FROM fecha_inicio)
ORDER BY mes

-- CASE y WHEN: Clasificación de proyectos según su presupuesto
-- presupuesto > 100000 THEN 'Alto
-- presupuesto BETWEEN 50000 AND 100000 THEN 'Medio'
-- ELSE 'Bajo'
SELECT pd.presupuesto, p.nombre_proyecto,
    CASE 
        WHEN pd.presupuesto > 50000 THEN 'Alto' 
        WHEN pd.presupuesto BETWEEN 30000 and 50000 THEN 'Medio'
        ELSE  'Bajo'
    END as Nivel_costo
FROM proyectos p
JOIN proyecto_detalle pd on pd.id_proyecto = p.id