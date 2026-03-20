-- SQL BÁSICO - SELECT
-- Fecha: 20 de Marzo de 2026
-- Autor: patoraya2

-- ============================================
-- 1. CREAR TABLA DE EJEMPLO
-- ============================================

-- Crear tabla de estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT,
    ciudad VARCHAR(100),
    gpa DECIMAL(3,2),
    fecha_registro DATE
);

-- ============================================
-- 2. INSERTAR DATOS
-- ============================================

INSERT INTO estudiantes (nombre, edad, ciudad, gpa, fecha_registro) VALUES
('patoraya2', 25, 'Ciudad Principal', 3.8, '2026-01-15'),
('Juan', 23, 'Segunda Ciudad', 3.5, '2026-02-10'),
('María', 24, 'Tercera Ciudad', 3.9, '2026-02-05'),
('Carlos', 26, 'Cuarta Ciudad', 3.6, '2026-01-20'),
('Ana', 22, 'Ciudad Principal', 3.7, '2026-03-01');

-- ============================================
-- 3. SELECT BÁSICO - Traer todos los datos
-- ============================================

-- Traer TODAS las columnas y TODAS las filas
SELECT * FROM estudiantes;

-- ============================================
-- 4. SELECT CON COLUMNAS ESPECÍFICAS
-- ============================================

-- Traer solo nombre y edad
SELECT nombre, edad FROM estudiantes;

-- Traer nombre, ciudad y gpa
SELECT nombre, ciudad, gpa FROM estudiantes;

-- ============================================
-- 5. SELECT CON ALIAS (Renombrar columnas)
-- ============================================

-- Renombrar columnas en la salida
SELECT 
    nombre AS "Nombre Estudiante",
    edad AS "Años",
    gpa AS "Calificación Promedio"
FROM estudiantes;

-- ============================================
-- 6. SELECT CON WHERE (Filtros)
-- ============================================

-- Traer solo estudiantes de 25 años
SELECT * FROM estudiantes
WHERE edad = 25;

-- Traer estudiantes mayores de 23
SELECT * FROM estudiantes
WHERE edad > 23;

-- Traer estudiantes de "Ciudad Principal"
SELECT * FROM estudiantes
WHERE ciudad = 'Ciudad Principal';

-- Traer estudiantes con GPA mayor a 3.7
SELECT nombre, gpa FROM estudiantes
WHERE gpa > 3.7;

-- ============================================
-- 7. SELECT CON MÚLTIPLES CONDICIONES
-- ============================================

-- AND - Ambas condiciones DEBEN cumplirse
SELECT * FROM estudiantes
WHERE edad > 23 AND gpa > 3.6;

-- OR - Al menos UNA condición debe cumplirse
SELECT * FROM estudiantes
WHERE ciudad = 'Ciudad Principal' OR gpa > 3.8;

-- NOT - Negar una condición
SELECT * FROM estudiantes
WHERE NOT ciudad = 'Ciudad Principal';

-- ============================================
-- 8. SELECT CON ORDER BY (Ordenar)
-- ============================================

-- Ordenar por edad (ascendente)
SELECT * FROM estudiantes
ORDER BY edad ASC;

-- Ordenar por edad (descendente)
SELECT * FROM estudiantes
ORDER BY edad DESC;

-- Ordenar por GPA descendente
SELECT nombre, gpa FROM estudiantes
ORDER BY gpa DESC;

-- Ordenar por ciudad, luego por nombre
SELECT * FROM estudiantes
ORDER BY ciudad ASC, nombre ASC;

-- ============================================
-- 9. SELECT CON LIMIT (Limitar resultados)
-- ============================================

-- Traer solo los primeros 3 estudiantes
SELECT * FROM estudiantes
LIMIT 3;

-- Traer los primeros 2 estudiantes ordenados por edad
SELECT nombre, edad FROM estudiantes
ORDER BY edad DESC
LIMIT 2;

-- ============================================
-- 10. SELECT CON OFFSET (Saltar filas)
-- ============================================

-- Saltar los primeros 2 y traer los siguientes 2
SELECT * FROM estudiantes
LIMIT 2 OFFSET 2;

-- Equivalente con FETCH
SELECT * FROM estudiantes
ORDER BY edad
OFFSET 2 ROWS
FETCH NEXT 2 ROWS ONLY;

-- ============================================
-- 11. SELECT DISTINCT (Valores únicos)
-- ============================================

-- Traer ciudades SIN repeticiones
SELECT DISTINCT ciudad FROM estudiantes;

-- Traer edades únicas
SELECT DISTINCT edad FROM estudiantes;

-- ============================================
-- 12. FUNCIONES DE AGREGACIÓN
-- ============================================

-- COUNT() - Contar filas
SELECT COUNT(*) AS total_estudiantes FROM estudiantes;

-- COUNT de una columna específica (ignora NULL)
SELECT COUNT(gpa) FROM estudiantes;

-- SUM() - Sumar valores
SELECT SUM(edad) AS suma_edades FROM estudiantes;

-- AVG() - Promedio
SELECT AVG(gpa) AS promedio_gpa FROM estudiantes;

-- MIN() - Mínimo
SELECT MIN(edad) AS edad_minima FROM estudiantes;

-- MAX() - Máximo
SELECT MAX(gpa) AS mejor_gpa FROM estudiantes;

-- ============================================
-- 13. SELECT CON GROUP BY
-- ============================================

-- Agrupar por ciudad y contar estudiantes
SELECT ciudad, COUNT(*) AS cantidad_estudiantes
FROM estudiantes
GROUP BY ciudad
ORDER BY cantidad_estudiantes DESC;

-- Agrupar por ciudad y calcular promedio GPA
SELECT ciudad, AVG(gpa) AS promedio_gpa
FROM estudiantes
GROUP BY ciudad;

-- Agrupar por edad
SELECT edad, COUNT(*) AS cantidad
FROM estudiantes
GROUP BY edad;

-- ============================================
-- 14. SELECT CON HAVING (Filtrar grupos)
-- ============================================

-- Mostrar solo ciudades con más de 1 estudiante
SELECT ciudad, COUNT(*) AS cantidad
FROM estudiantes
GROUP BY ciudad
HAVING COUNT(*) > 1;

-- Mostrar solo ciudades con promedio GPA > 3.7
SELECT ciudad, AVG(gpa) AS promedio_gpa
FROM estudiantes
GROUP BY ciudad
HAVING AVG(gpa) > 3.7;

-- ============================================
-- 15. SELECT CON CASE (Condicionales)
-- ============================================

-- Clasificar estudiantes por rendimiento
SELECT 
    nombre,
    gpa,
    CASE 
        WHEN gpa >= 3.8 THEN 'Excelente'
        WHEN gpa >= 3.5 THEN 'Muy Bueno'
        WHEN gpa >= 3.0 THEN 'Bueno'
        ELSE 'Necesita mejorar'
    END AS clasificacion
FROM estudiantes;

-- Clasificar por edad
SELECT 
    nombre,
    edad,
    CASE 
        WHEN edad < 23 THEN 'Joven'
        WHEN edad BETWEEN 23 AND 25 THEN 'Adulto joven'
        ELSE 'Mayor'
    END AS grupo_edad
FROM estudiantes;

-- ============================================
-- 16. OPERADORES ÚTILES
-- ============================================

-- IN - Valores dentro de una lista
SELECT * FROM estudiantes
WHERE ciudad IN ('Ciudad Principal', 'Segunda Ciudad');

-- NOT IN
SELECT * FROM estudiantes
WHERE ciudad NOT IN ('Ciudad Principal');

-- BETWEEN - Entre rangos
SELECT * FROM estudiantes
WHERE edad BETWEEN 23 AND 25;

-- LIKE - Búsqueda de texto (% = cualquier carácter)
SELECT * FROM estudiantes
WHERE nombre LIKE 'p%';  -- Nombres que empiezan con 'p'

-- ILIKE - Búsqueda insensible a mayúsculas (PostgreSQL)
SELECT * FROM estudiantes
WHERE nombre ILIKE 'P%';  -- Funciona con 'p' o 'P'

-- ============================================
-- 17. NULL - Valores nulos
-- ============================================

-- Traer filas donde una columna ES NULL
SELECT * FROM estudiantes
WHERE ciudad IS NULL;

-- Traer filas donde una columna NO ES NULL
SELECT * FROM estudiantes
WHERE ciudad IS NOT NULL;

-- ============================================
-- 18. EJEMPLOS COMBINADOS
-- ============================================

-- Encontrar estudiante con mejor GPA en Ciudad Principal
SELECT nombre, gpa
FROM estudiantes
WHERE ciudad = 'Ciudad Principal'
ORDER BY gpa DESC
LIMIT 1;

-- Contar estudiantes por rango de edad
SELECT 
    CASE 
        WHEN edad < 23 THEN 'Menores de 23'
        WHEN edad BETWEEN 23 AND 25 THEN 'Entre 23-25'
        ELSE 'Mayores de 25'
    END AS rango_edad,
    COUNT(*) AS cantidad
FROM estudiantes
GROUP BY 
    CASE 
        WHEN edad < 23 THEN 'Menores de 23'
        WHEN edad BETWEEN 23 AND 25 THEN 'Entre 23-25'
        ELSE 'Mayores de 25'
    END
ORDER BY cantidad DESC;

-- Estudiantes ordenados por GPA, mostrando su clasificación
SELECT 
    nombre,
    ciudad,
    gpa,
    CASE 
        WHEN gpa >= 3.8 THEN 'Excelente'
        WHEN gpa >= 3.5 THEN 'Muy Bueno'
        ELSE 'Bueno'
    END AS clasificacion
FROM estudiantes
ORDER BY gpa DESC;

-- ============================================
-- LIMPIAR (Descomenta para eliminar la tabla)
-- ============================================

-- DROP TABLE IF EXISTS estudiantes;