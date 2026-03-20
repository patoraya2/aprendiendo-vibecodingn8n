\# 📚 SQL Básico



\*\*Fecha:\*\* 20 de Marzo de 2026  

\*\*Autor:\*\* patoraya2



\---



\## ¿Qué es SQL?



\*\*SQL\*\* = \*\*S\*\*tructured \*\*Q\*\*uery \*\*L\*\*anguage (Lenguaje de Consulta Estructurado)



Es el lenguaje estándar para:

\- Crear y modificar bases de datos

\- Insertar, actualizar y eliminar datos

\- Consultar y filtrar información

\- Hacer cálculos y análisis



\### SQL vs Python vs Diccionarios



| Concepto | SQL | Python Diccionarios |

|----------|-----|---------------------|

| Estructura | Tablas (filas y columnas) | {"clave": valor} |

| Búsqueda | SELECT WHERE | dict.get() |

| Múltiples registros | Filas | Lista de diccionarios |

| Relaciones | JOINS | Anidar diccionarios |

| Análisis | GROUP BY, agregaciones | Loops y matemática |



\---



\## Conceptos Básicos



\### Base de Datos

Una colección organizada de datos relacionados.



\### Tabla

Una estructura de datos con filas y columnas.



```

Tabla: estudiantes



| id | nombre    | edad | ciudad          | gpa |

|----|-----------|------|-----------------|-----|

| 1  | patoraya2 | 25   | Ciudad Principal | 3.8 |

| 2  | Juan      | 23   | Segunda Ciudad   | 3.5 |

| 3  | María     | 24   | Tercera Ciudad   | 3.9 |

```



\### Columna

Una característica o atributo.



```

Columnas: id, nombre, edad, ciudad, gpa

```



\### Fila

Un registro individual de datos.



```

Fila: (1, 'patoraya2', 25, 'Ciudad Principal', 3.8)

```



\---



\## Crear Tabla



\### Sintaxis básica



```sql

CREATE TABLE nombre\_tabla (

&#x20;   columna1 TIPO\_DATO,

&#x20;   columna2 TIPO\_DATO,

&#x20;   columna3 TIPO\_DATO

);

```



\### Ejemplo: Tabla de estudiantes



```sql

CREATE TABLE IF NOT EXISTS estudiantes (

&#x20;   id SERIAL PRIMARY KEY,

&#x20;   nombre VARCHAR(100) NOT NULL,

&#x20;   edad INT,

&#x20;   ciudad VARCHAR(100),

&#x20;   gpa DECIMAL(3,2),

&#x20;   fecha\_registro DATE

);

```



\### Explicación



| Elemento | Significado |

|----------|-------------|

| `CREATE TABLE` | Crear una tabla |

| `IF NOT EXISTS` | Solo si no existe |

| `id SERIAL PRIMARY KEY` | ID auto-incrementable, identificador único |

| `nombre VARCHAR(100) NOT NULL` | Texto hasta 100 caracteres, OBLIGATORIO |

| `edad INT` | Número entero |

| `gpa DECIMAL(3,2)` | Decimal: 3 dígitos total, 2 después del punto (3.80) |

| `DATE` | Fecha |



\### Tipos de Datos Comunes



```sql

INT                 -- Números enteros

DECIMAL(5,2)        -- Decimales (5 dígitos, 2 después del punto)

VARCHAR(100)        -- Texto variable hasta 100 caracteres

TEXT                -- Texto largo

BOOLEAN             -- Verdadero/Falso

DATE                -- Fecha (YYYY-MM-DD)

TIMESTAMP           -- Fecha y hora

SERIAL              -- Auto-incrementable

```



\---



\## INSERT - Insertar Datos



\### Sintaxis



```sql

INSERT INTO nombre\_tabla (columna1, columna2, columna3)

VALUES (valor1, valor2, valor3);

```



\### Ejemplo: Un estudiante



```sql

INSERT INTO estudiantes (nombre, edad, ciudad, gpa, fecha\_registro)

VALUES ('patoraya2', 25, 'Ciudad Principal', 3.8, '2026-01-15');

```



\### Insertar múltiples filas



```sql

INSERT INTO estudiantes (nombre, edad, ciudad, gpa, fecha\_registro) VALUES

('patoraya2', 25, 'Ciudad Principal', 3.8, '2026-01-15'),

('Juan', 23, 'Segunda Ciudad', 3.5, '2026-02-10'),

('María', 24, 'Tercera Ciudad', 3.9, '2026-02-05');

```



\---



\## SELECT - Consultar Datos



\### Traer TODO



```sql

SELECT \* FROM estudiantes;

```



Devuelve todas las columnas y todas las filas.



\### Traer columnas específicas



```sql

SELECT nombre, edad FROM estudiantes;

```



Devuelve solo nombre y edad.



\### Renombrar columnas (ALIAS)



```sql

SELECT 

&#x20;   nombre AS "Nombre Estudiante",

&#x20;   edad AS "Años",

&#x20;   gpa AS "Calificación"

FROM estudiantes;

```



\---



\## WHERE - Filtrar Datos



\### Comparadores



```sql

= (igual)

> (mayor)

< (menor)

>= (mayor o igual)

<= (menor o igual)

!= o <> (diferente)

```



\### Ejemplos



```sql

\-- Estudiantes de 25 años

SELECT \* FROM estudiantes

WHERE edad = 25;



\-- Estudiantes mayores de 23

SELECT \* FROM estudiantes

WHERE edad > 23;



\-- Estudiantes con GPA mayor a 3.7

SELECT \* FROM estudiantes

WHERE gpa > 3.7;



\-- Estudiantes de "Ciudad Principal"

SELECT \* FROM estudiantes

WHERE ciudad = 'Ciudad Principal';

```



\### Múltiples condiciones



\#### AND (ambas deben cumplirse)

```sql

SELECT \* FROM estudiantes

WHERE edad > 23 AND gpa > 3.6;

```



\#### OR (al menos una debe cumplirse)

```sql

SELECT \* FROM estudiantes

WHERE ciudad = 'Ciudad Principal' OR gpa > 3.8;

```



\#### NOT (negar)

```sql

SELECT \* FROM estudiantes

WHERE NOT ciudad = 'Ciudad Principal';

```



\---



\## ORDER BY - Ordenar Resultados



\### Ascendente (defecto)



```sql

SELECT \* FROM estudiantes

ORDER BY edad ASC;

```



Resultado:

```

| id | nombre    | edad |

|----|-----------|------|

| 2  | Juan      | 23   |

| 3  | María     | 24   |

| 1  | patoraya2 | 25   |

```



\### Descendente



```sql

SELECT \* FROM estudiantes

ORDER BY gpa DESC;

```



\### Ordenar por múltiples columnas



```sql

SELECT \* FROM estudiantes

ORDER BY ciudad ASC, nombre ASC;

```



\---



\## LIMIT - Limitar Resultados



```sql

\-- Solo los primeros 3

SELECT \* FROM estudiantes

LIMIT 3;



\-- Los mejores 2 estudiantes por GPA

SELECT nombre, gpa FROM estudiantes

ORDER BY gpa DESC

LIMIT 2;

```



\---



\## OFFSET - Saltar Filas



```sql

\-- Saltar los primeros 2, traer los siguientes 2

SELECT \* FROM estudiantes

LIMIT 2 OFFSET 2;

```



Útil para \*\*paginación\*\*:

\- Página 1: `LIMIT 10 OFFSET 0`

\- Página 2: `LIMIT 10 OFFSET 10`

\- Página 3: `LIMIT 10 OFFSET 20`



\---



\## DISTINCT - Valores Únicos



```sql

\-- Ciudades sin repeticiones

SELECT DISTINCT ciudad FROM estudiantes;

```



Resultado:

```

ciudad

Ciudad Principal

Segunda Ciudad

Tercera Ciudad

```



\---



\## Funciones de Agregación



\### COUNT - Contar filas



```sql

SELECT COUNT(\*) AS total FROM estudiantes;

\-- Resultado: 5



SELECT COUNT(gpa) FROM estudiantes;

\-- Cuenta solo filas donde gpa NO ES NULL

```



\### SUM - Sumar



```sql

SELECT SUM(edad) FROM estudiantes;

\-- Suma todas las edades

```



\### AVG - Promedio



```sql

SELECT AVG(gpa) FROM estudiantes;

\-- Promedio de GPA

```



\### MIN - Mínimo



```sql

SELECT MIN(edad) FROM estudiantes;

\-- Edad más baja

```



\### MAX - Máximo



```sql

SELECT MAX(gpa) FROM estudiantes;

\-- Mejor GPA

```



\---



\## GROUP BY - Agrupar Datos



\### Contar por grupo



```sql

SELECT ciudad, COUNT(\*) AS cantidad

FROM estudiantes

GROUP BY ciudad

ORDER BY cantidad DESC;

```



Resultado:

```

ciudad              | cantidad

Ciudad Principal    | 2

Segunda Ciudad      | 1

Tercera Ciudad      | 1

Cuarta Ciudad       | 1

```



\### Promedio por grupo



```sql

SELECT ciudad, AVG(gpa) AS promedio\_gpa

FROM estudiantes

GROUP BY ciudad;

```



\---



\## HAVING - Filtrar Grupos



\### Solo ciudades con más de 1 estudiante



```sql

SELECT ciudad, COUNT(\*) AS cantidad

FROM estudiantes

GROUP BY ciudad

HAVING COUNT(\*) > 1;

```



\### Solo ciudades con promedio GPA > 3.7



```sql

SELECT ciudad, AVG(gpa) AS promedio\_gpa

FROM estudiantes

GROUP BY ciudad

HAVING AVG(gpa) > 3.7;

```



\---



\## CASE - Condicionales



```sql

SELECT 

&#x20;   nombre,

&#x20;   gpa,

&#x20;   CASE 

&#x20;       WHEN gpa >= 3.8 THEN 'Excelente'

&#x20;       WHEN gpa >= 3.5 THEN 'Muy Bueno'

&#x20;       WHEN gpa >= 3.0 THEN 'Bueno'

&#x20;       ELSE 'Necesita mejorar'

&#x20;   END AS clasificacion

FROM estudiantes;

```



Resultado:

```

nombre      | gpa | clasificacion

patoraya2   | 3.8 | Excelente

Juan        | 3.5 | Muy Bueno

María       | 3.9 | Excelente

Carlos      | 3.6 | Muy Bueno

Ana         | 3.7 | Muy Bueno

```



\---



\## Operadores Útiles



\### IN - Valores en lista



```sql

SELECT \* FROM estudiantes

WHERE ciudad IN ('Ciudad Principal', 'Segunda Ciudad');

```



\### NOT IN



```sql

SELECT \* FROM estudiantes

WHERE ciudad NOT IN ('Ciudad Principal');

```



\### BETWEEN - Rango



```sql

SELECT \* FROM estudiantes

WHERE edad BETWEEN 23 AND 25;

```



\### LIKE - Búsqueda de texto



```sql

SELECT \* FROM estudiantes

WHERE nombre LIKE 'p%';  -- Empieza con 'p'



SELECT \* FROM estudiantes

WHERE nombre LIKE '%a%';  -- Contiene 'a'



SELECT \* FROM estudiantes

WHERE nombre LIKE '%ez';  -- Termina con 'ez'

```



\### ILIKE - Búsqueda insensible (PostgreSQL)



```sql

SELECT \* FROM estudiantes

WHERE nombre ILIKE 'P%';  -- Funciona con 'p'\*



