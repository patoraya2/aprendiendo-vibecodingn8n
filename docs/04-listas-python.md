\# 📋 Listas en Python



\*\*Fecha:\*\* 18 de Marzo de 2026  

\*\*Autor:\*\* patoraya2



\---



\## ¿Qué es una Lista?



Una \*\*lista\*\* es un \*\*contenedor que puede guardar MÚLTIPLES valores\*\*.



\### Analogía

Es como una \*\*caja con compartimentos numerados\*\*:

\- Cada compartimento tiene un número (índice)

\- El primer compartimento es el índice \*\*0\*\*

\- Puedes acceder a cualquier compartimento por su número



\### Sintaxis

```python

lista = \[elemento1, elemento2, elemento3]

```



\### Ejemplo

```python

nombres = \["patoraya2", "Juan", "María", "Carlos"]

numeros = \[1, 2, 3, 4, 5]

mixta = \["texto", 42, 3.14, True]

```



\---



\## Crear Listas



\### Lista vacía

```python

lista\_vacia = \[]

```



\### Lista con elementos

```python

frutas = \["manzana", "banana", "naranja"]

edades = \[25, 30, 35, 40]

```



\### Lista mixta (diferentes tipos)

```python

persona = \["patoraya2", 25, 19.99, True, "Developer"]

```



\---



\## Acceder a Elementos (Índices)



\### Índices Positivos

Los índices comienzan en \*\*0\*\*:



```python

nombres = \["patoraya2", "Juan", "María", "Carlos"]

\#           0            1       2        3



print(nombres\[0])  # patoraya2

print(nombres\[1])  # Juan

print(nombres\[2])  # María

print(nombres\[3])  # Carlos

```



\### Índices Negativos

Los índices negativos cuentan desde el \*\*final\*\*:



```python

nombres = \["patoraya2", "Juan", "María", "Carlos"]

\#           -4           -3      -2       -1



print(nombres\[-1])  # Carlos (último)

print(nombres\[-2])  # María (penúltimo)

print(nombres\[-3])  # Juan

print(nombres\[-4])  # patoraya2 (primero)

```



\---



\## Largo de una Lista



Usa `len()` para saber cuántos elementos tiene:



```python

nombres = \["patoraya2", "Juan", "María", "Carlos"]

cantidad = len(nombres)



print(cantidad)  # 4

```



\---



\## Agregar Elementos



\### append() - Agrega al final

```python

frutas = \["manzana", "banana"]

frutas.append("naranja")



print(frutas)  # \["manzana", "banana", "naranja"]

```



\### insert() - Agrega en posición específica

```python

frutas = \["manzana", "banana", "naranja"]

frutas.insert(1, "pera")  # Inserta en índice 1



print(frutas)  # \["manzana", "pera", "banana", "naranja"]

```



\---



\## Eliminar Elementos



\### remove() - Elimina por valor

```python

frutas = \["manzana", "banana", "naranja"]

frutas.remove("banana")



print(frutas)  # \["manzana", "naranja"]

```



\### pop() - Elimina por índice

```python

frutas = \["manzana", "banana", "naranja"]

eliminada = frutas.pop(1)  # Elimina el índice 1



print(eliminada)  # banana

print(frutas)     # \["manzana", "naranja"]

```



\### pop() sin índice - Elimina el último

```python

frutas = \["manzana", "banana", "naranja"]

ultimo = frutas.pop()



print(ultimo)  # naranja

print(frutas)  # \["manzana", "banana"]

```



\---



\## Recorrer Listas (FOR)



\### For básico

```python

nombres = \["patoraya2", "Juan", "María", "Carlos"]



for nombre in nombres:

&#x20;   print(nombre)

```



Salida:

```

patoraya2

Juan

María

Carlos

```



\### For con índice

```python

nombres = \["patoraya2", "Juan", "María", "Carlos"]



for i in range(len(nombres)):

&#x20;   print(f"Índice {i}: {nombres\[i]}")

```



Salida:

```

Índice 0: patoraya2

Índice 1: Juan

Índice 2: María

Índice 3: Carlos

```



\---



\## Operaciones con Listas



\### Concatenar (Juntar)

```python

lista1 = \[1, 2, 3]

lista2 = \[4, 5, 6]



lista\_junta = lista1 + lista2

print(lista\_junta)  # \[1, 2, 3, 4, 5, 6]

```



\### Repetir

```python

lista = \[0] \* 5

print(lista)  # \[0, 0, 0, 0, 0]



lista2 = \["a", "b"] \* 3

print(lista2)  # \["a", "b", "a", "b", "a", "b"]

```



\---



\## Slicing (Cortes)



\### Sintaxis: `lista\[inicio:fin]`

\*\*Importante:\*\* El `fin` NO se incluye.



```python

numeros = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



\# \[2:5] - Desde índice 2 hasta 4 (5 NO se incluye)

print(numeros\[2:5])  # \[2, 3, 4]



\# \[:5] - Desde el inicio hasta 4

print(numeros\[:5])   # \[0, 1, 2, 3, 4]



\# \[5:] - Desde 5 hasta el final

print(numeros\[5:])   # \[5, 6, 7, 8, 9]



\# \[::2] - Cada 2 elementos

print(numeros\[::2])  # \[0, 2, 4, 6, 8]



\# \[::-1] - Invertir

print(numeros\[::-1]) # \[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

```



\---



\## Métodos Útiles



\### sorted() - Ordena

```python

numeros = \[3, 1, 4, 1, 5, 9, 2, 6]

ordenados = sorted(numeros)



print(ordenados)  # \[1, 1, 2, 3, 4, 5, 6, 9]

```



\### count() - Cuenta repeticiones

```python

numeros = \[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

cantidad = numeros.count(4)



print(cantidad)  # 4

```



\### index() - Encuentra posición

```python

frutas = \["manzana", "banana", "naranja", "uva"]

posicion = frutas.index("banana")



print(posicion)  # 1

```



\### in - Verificar si existe

```python

frutas = \["manzana", "banana", "naranja"]



if "banana" in frutas:

&#x20;   print("¡Tenemos banana!")  # Esto se imprime



if "uva" in frutas:

&#x20;   print("Tenemos uva")  # Esto NO se imprime

```



\---



\## Lista de Diccionarios



Puedes guardar \*\*diccionarios dentro de listas\*\*:



```python

estudiantes = \[

&#x20;   {"nombre": "patoraya2", "edad": 25, "curso": "Python"},

&#x20;   {"nombre": "Juan", "edad": 23, "curso": "JavaScript"},

&#x20;   {"nombre": "María", "edad": 24, "curso": "Python"},

]



\# Acceder

print(estudiantes\[0]\["nombre"])  # patoraya2



\# Recorrer

for estudiante in estudiantes:

&#x20;   print(f"{estudiante\['nombre']}: {estudiante\['curso']}")

```



\---



\## Ejemplo Práctico: Carrito de Compras



```python

carrito = \[]



\# Agregar productos

carrito.append({"producto": "Laptop", "precio": 1000, "cantidad": 1})

carrito.append({"producto": "Mouse", "precio": 25, "cantidad": 2})

carrito.append({"producto": "Teclado", "precio": 75, "cantidad": 1})



\# Calcular total

total = 0

print("Tu carrito:")

for item in carrito:

&#x20;   subtotal = item\["precio"] \* item\["cantidad"]

&#x20;   total += subtotal

&#x20;   print(f"  - {item\['producto']}: ${item\['precio']} x {item\['cantidad']} = ${subtotal}")



print(f"\\nTotal: ${total}")

```



Salida:

```

Tu carrito:

&#x20; - Laptop: $1000 x 1 = $1000

&#x20; - Mouse: $25 x 2 = $50

&#x20; - Teclado: $75 x 1 = $75



Total: $1125

```



\---



\## Tabla Resumen de Métodos



| Método | Uso | Ejemplo |

|--------|-----|---------|

| `append()` | Agrega al final | `lista.append(4)` |

| `insert()` | Agrega en posición | `lista.insert(0, 1)` |

| `remove()` | Elimina por valor | `lista.remove(2)` |

| `pop()` | Elimina por índice | `lista.pop(0)` |

| `len()` | Largo | `len(lista)` |

| `sorted()` | Ordena | `sorted(lista)` |

| `count()` | Cuenta | `lista.count(2)` |

| `index()` | Encuentra | `lista.index(2)` |

| `in` | Verifica | `2 in lista` |



\---



\## Errores Comunes



\### ❌ Error 1: Índice fuera de rango

```python

\# INCORRECTO

lista = \[1, 2, 3]

print(lista\[5])  # IndexError: list index out of range



\# CORRECTO

print(lista\[2])  # 3

```



\### ❌ Error 2: Confundir índices

```python

\# INCORRECTO

lista = \["a", "b", "c"]

print(lista\[1:3])  # Esperabas \["b"], pero es \["b", "c"]



\# CORRECTO

print(lista\[1:2])  # \["b"]

```



\### ❌ Error 3: Modificar lista mientras recorres

```python

\# INCORRECTO

lista = \[1, 2, 3, 4, 5]

for elemento in lista:

&#x20;   if elemento == 3:

&#x20;       lista.remove(elemento)  # ⚠️ Problema



\# CORRECTO

lista = \[1, 2, 3, 4, 5]

lista = \[x for x in lista if x != 3]

```



\---



\## Lo que aprendimos hoy



✅ Crear listas  

✅ Acceder a elementos con índices  

✅ Agregar y eliminar elementos  

✅ Recorrer listas con for  

✅ Slicing (cortes)  

✅ Métodos útiles (append, remove, pop, etc.)  

✅ Lista de diccionarios  

✅ Ejemplo práctico: carrito de compras  



\---



\## Próximos Temas



\- \[ ] Diccionarios en profundidad

\- \[ ] Tuplas

\- \[ ] Conjuntos (Sets)

\- \[ ] Comprensión de listas

\- \[ ] Funciones

\- \[ ] Manejo de archivos



\---



\## Mi Script de Hoy



Creé: `ejemplos/03-listas-basico.py`



Contiene:

\- Crear y acceder a listas

\- Agregar y eliminar elementos

\- Recorrer con for

\- Operaciones y slicing

\- Métodos útiles

\- Lista de diccionarios

\- Ejemplo: carrito de compras



\---



\*\*Última actualización:\*\* 18/03/2026



