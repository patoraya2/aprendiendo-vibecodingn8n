\# 🐍 Python Básico - Variables y Tipos de Datos



\*\*Fecha:\*\* 17 de Marzo de 2026  

\*\*Autor:\*\* patoraya2



\---



\## ¿Qué es Python?



Python es un \*\*lenguaje de programación\*\* fácil de leer y muy poderoso.



\### ¿Por qué aprender Python?

\- 🐍 Sintaxis simple y legible

\- 🚀 Muy usado en ciencia de datos, IA, web

\- 💼 Demanda laboral altísima

\- 🎓 Perfecto para aprender a programar

\- 🌍 Comunidad gigante



\---



\## ¿Qué es una Variable?



Una \*\*variable\*\* es un \*\*contenedor donde guardamos información\*\*.



\### Analogía

Es como una \*\*caja etiquetada\*\*:

\- El \*\*nombre\*\* es la etiqueta (ej: `nombre`)

\- El \*\*contenido\*\* es el valor (ej: `"patoraya2"`)



\### Ejemplo

```python

nombre = "patoraya2"

edad = 25

```



Aquí:

\- `nombre` es la variable (la etiqueta)

\- `"patoraya2"` es el valor (lo que guardamos)

\- `=` significa "asigna" (guarda el valor en la variable)



\---



\## Tipos de Datos Principales



\### 1. STRING (Texto)

Cualquier texto entre comillas (`"` o `'`):



```python

nombre = "patoraya2"

mensaje = 'Hola, mundo'

descripcion = "Soy un desarrollador en formación"



print(nombre)  # Salida: patoraya2

```



\*\*Usa `str()` para convertir a string:\*\*

```python

numero = 42

numero\_texto = str(numero)  # "42"

```



\---



\### 2. INTEGER (Número Entero)

Números sin punto decimal:



```python

edad = 25

cantidad = 100

negativo = -15



print(edad)  # Salida: 25

```



\*\*Usa `int()` para convertir a entero:\*\*

```python

texto = "123"

numero = int(texto)  # 123

```



\---



\### 3. FLOAT (Número Decimal)

Números con punto decimal:



```python

precio = 19.99

altura = 1.75

pi = 3.14159



print(precio)  # Salida: 19.99

```



\*\*Usa `float()` para convertir a float:\*\*

```python

texto = "3.14"

numero = float(texto)  # 3.14

```



\---



\### 4. BOOLEAN (Verdadero/Falso)

Solo dos valores posibles: `True` o `False`:



```python

activo = True

desactivado = False

es\_mayor\_de\_edad = True



print(activo)  # Salida: True

```



\*\*Se usa mucho en condiciones:\*\*

```python

edad = 25

es\_adulto = edad >= 18  # True

```



\---



\## Operaciones Aritméticas



\### Suma

```python

a = 10

b = 5

resultado = a + b  # 15

print(resultado)  # 15

```



\### Resta

```python

resultado = a - b  # 5

```



\### Multiplicación

```python

resultado = a \* b  # 50

```



\### División

```python

resultado = a / b  # 2.0 (siempre devuelve float)

```



\### División Entera

```python

resultado = a // b  # 2 (solo la parte entera)

```



\### Potencia

```python

resultado = a \*\* 2  # 100 (10 al cuadrado)

```



\### Módulo (Residuo)

```python

resultado = a % 3  # 1 (el residuo de 10 ÷ 3)

```



\---



\## Concatenación de Strings



\### Forma 1: Con `+` (no recomendado)

```python

nombre = "patoraya2"

apellido = "Developer"

completo = nombre + " " + apellido

print(completo)  # patoraya2 Developer

```



\### Forma 2: Con f-strings (RECOMENDADO ⭐)

```python

nombre = "patoraya2"

edad = 25

mensaje = f"Mi nombre es {nombre} y tengo {edad} años"

print(mensaje)  # Mi nombre es patoraya2 y tengo 25 años

```



\### Forma 3: Con `.format()`

```python

mensaje = "Mi nombre es {} y tengo {} años".format(nombre, edad)

```



\*\*⭐ Usa f-strings, es lo más moderno.\*\*



\---



\## Convertir Entre Tipos



\### String a Entero

```python

texto = "123"

numero = int(texto)

print(numero)  # 123

print(type(numero))  # <class 'int'>

```



\### Entero a String

```python

numero = 456

texto = str(numero)

print(texto)  # "456"

print(type(texto))  # <class 'str'>

```



\### String a Float

```python

texto = "3.14"

decimal = float(texto)

print(decimal)  # 3.14

```



\---



\## INPUT - Recibir Datos del Usuario



\### Sintaxis Básica

```python

nombre = input("¿Cuál es tu nombre?: ")

print(f"Hola, {nombre}")

```



\*\*Importante:\*\* `input()` SIEMPRE devuelve un \*\*string\*\*.



\### Convertir Input a Número

```python

edad\_texto = input("¿Cuántos años tienes?: ")

edad = int(edad\_texto)  # Convertir a entero

print(f"Tienes {edad} años")

print(f"El año que viene tendrás {edad + 1} años")

```



\---



\## TYPE() - Saber el Tipo de un Dato



```python

nombre = "patoraya2"

edad = 25

precio = 19.99

activo = True



print(type(nombre))   # <class 'str'>

print(type(edad))     # <class 'int'>

print(type(precio))   # <class 'float'>

print(type(activo))   # <class 'bool'>

```



\---



\## Tabla Resumen de Tipos



| Tipo | Ejemplo | Descripción |

|------|---------|-------------|

| String | `"hola"` | Texto |

| Integer | `42` | Número entero |

| Float | `3.14` | Número decimal |

| Boolean | `True` | Verdadero/Falso |



\---



\## Ejemplos Prácticos



\### Ejemplo 1: Calculadora Simple

```python

a = 10

b = 5



print(f"{a} + {b} = {a + b}")

print(f"{a} - {b} = {a - b}")

print(f"{a} \* {b} = {a \* b}")

print(f"{a} / {b} = {a / b}")

```



Salida:

```

10 + 5 = 15

10 - 5 = 5

10 \* 5 = 50

10 / 5 = 2.0

```



\### Ejemplo 2: Saludar al Usuario

```python

nombre = input("¿Cuál es tu nombre?: ")

edad = int(input("¿Cuántos años tienes?: "))

ciudad = input("¿De dónde eres?: ")



print(f"\\n¡Hola {nombre}!")

print(f"Tienes {edad} años y eres de {ciudad}")

```



\### Ejemplo 3: Calcular IMC (Índice de Masa Corporal)

```python

peso = float(input("¿Cuál es tu peso (kg)?: "))

altura = float(input("¿Cuál es tu altura (m)?: "))



imc = peso / (altura \*\* 2)

print(f"\\nTu IMC es: {imc:.2f}")

```



\---



\## Errores Comunes



\### ❌ Error 1: Olvidar convertir input

```python

\# INCORRECTO

edad = input("¿Edad?: ")

print(edad + 1)  # Error: no puedes sumar string + int



\# CORRECTO

edad = int(input("¿Edad?: "))

print(edad + 1)  # Funciona

```



\### ❌ Error 2: Confundir = con ==

```python

\# INCORRECTO

if nombre = "patoraya2":  # SyntaxError

&#x20;   pass



\# CORRECTO

if nombre == "patoraya2":  # Compara

&#x20;   pass

```



\### ❌ Error 3: Usar comillas dentro de comillas sin escapar

```python

\# INCORRECTO

texto = "Dice: "Hola""  # Error



\# CORRECTO

texto = 'Dice: "Hola"'  # Funciona

\# O

texto = "Dice: \\"Hola\\""  # También funciona

```



\---



\## Lo que aprendimos hoy



✅ Variables y cómo funcionan  

✅ 4 tipos de datos principales  

✅ Operaciones aritméticas  

✅ Concatenación de strings  

✅ Conversión de tipos  

✅ Función `input()`  

✅ Función `type()`  

✅ Cómo evitar errores comunes  



\---



\## Próximos Temas



\- \[ ] Listas y Tuplas

\- \[ ] Diccionarios

\- \[ ] Funciones

\- \[ ] Condicionales (if/else)

\- \[ ] Loops (for/while)

\- \[ ] Manejo de excepciones



\---



\## Mi Script de Hoy



Creé: `ejemplos/02-variables-y-tipos.py`



Contiene:

\- Variables básicas

\- Todos los tipos de datos

\- Operaciones aritméticas

\- Concatenación

\- Conversión de tipos

\- Input/Output interactivo



\---



\*\*Última actualización:\*\* 17/03/2026

