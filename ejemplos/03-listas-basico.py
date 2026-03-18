# Listas en Python - Colecciones de datos
# Fecha: 18 de Marzo de 2026
# Autor: patoraya2

print("="*50)
print("LISTAS EN PYTHON")
print("="*50)

# ============================================
# 1. ¿QUÉ ES UNA LISTA?
# ============================================

print("\n1. ¿QUÉ ES UNA LISTA?")
print("-"*50)

# Una lista es un contenedor que puede guardar MÚLTIPLES valores
# Se define con [ ]

numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

nombres = ["patoraya2", "Juan", "María", "Carlos"]
print(f"Lista de nombres: {nombres}")

# Una lista puede tener DIFERENTES tipos
mixta = ["patoraya2", 25, 19.99, True]
print(f"Lista mixta: {mixta}")

# ============================================
# 2. ACCEDER A ELEMENTOS (ÍNDICES)
# ============================================

print("\n2. ACCEDER A ELEMENTOS")
print("-"*50)

nombres = ["patoraya2", "Juan", "María", "Carlos"]

# Los índices COMIENZAN EN 0
print(f"Primer elemento (índice 0): {nombres[0]}")
print(f"Segundo elemento (índice 1): {nombres[1]}")
print(f"Tercero elemento (índice 2): {nombres[2]}")

# Índices negativos: cuentan desde el final
print(f"Último elemento (índice -1): {nombres[-1]}")
print(f"Penúltimo (índice -2): {nombres[-2]}")

# ============================================
# 3. LARGO DE UNA LISTA
# ============================================

print("\n3. LARGO DE UNA LISTA")
print("-"*50)

nombres = ["patoraya2", "Juan", "María", "Carlos"]
cantidad = len(nombres)

print(f"La lista tiene {cantidad} elementos")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista: {numeros}")
print(f"Cantidad de números: {len(numeros)}")

# ============================================
# 4. AGREGAR ELEMENTOS
# ============================================

print("\n4. AGREGAR ELEMENTOS")
print("-"*50)

frutas = ["manzana", "banana", "naranja"]
print(f"Lista original: {frutas}")

# append() - Agrega al final
frutas.append("uva")
print(f"Después de append('uva'): {frutas}")

# insert() - Agrega en posición específica
frutas.insert(1, "pera")  # Agrega en índice 1
print(f"Después de insert(1, 'pera'): {frutas}")

# ============================================
# 5. ELIMINAR ELEMENTOS
# ============================================

print("\n5. ELIMINAR ELEMENTOS")
print("-"*50)

frutas = ["manzana", "banana", "naranja", "uva"]
print(f"Lista original: {frutas}")

# remove() - Elimina por valor
frutas.remove("banana")
print(f"Después de remove('banana'): {frutas}")

# pop() - Elimina por índice y lo devuelve
ultimo = frutas.pop()  # Elimina el último
print(f"Elemento eliminado con pop(): {ultimo}")
print(f"Lista después de pop(): {frutas}")

# ============================================
# 6. RECORRER LISTAS (FOR)
# ============================================

print("\n6. RECORRER LISTAS")
print("-"*50)

nombres = ["patoraya2", "Juan", "María", "Carlos"]

print("Imprimiendo cada nombre:")
for nombre in nombres:
    print(f"  - {nombre}")

print("\nImprimiendo con índice:")
for i in range(len(nombres)):
    print(f"  Índice {i}: {nombres[i]}")

# ============================================
# 7. OPERACIONES CON LISTAS
# ============================================

print("\n7. OPERACIONES CON LISTAS")
print("-"*50)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatenar (juntar)
lista_junta = lista1 + lista2
print(f"Concatenar: {lista1} + {lista2} = {lista_junta}")

# Repetir
lista_repetida = [0] * 5
print(f"Repetir [0] * 5 = {lista_repetida}")

# ============================================
# 8. SLICING (Cortes)
# ============================================

print("\n8. SLICING (Cortes)")
print("-"*50)

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista completa: {numeros}")

# [inicio:fin] - fin NO se incluye
print(f"[2:5]: {numeros[2:5]}")  # Elementos 2, 3, 4

# [:5] - desde el principio hasta 5
print(f"[:5]: {numeros[:5]}")  # Elementos 0, 1, 2, 3, 4

# [5:] - desde 5 hasta el final
print(f"[5:]: {numeros[5:]}")  # Elementos 5, 6, 7, 8, 9

# [::2] - cada 2 elementos
print(f"[::2]: {numeros[::2]}")  # Elementos pares: 0, 2, 4, 6, 8

# ============================================
# 9. MÉTODOS ÚTILES
# ============================================

print("\n9. MÉTODOS ÚTILES")
print("-"*50)

numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - Ordena de menor a mayor
numeros_ordenados = sorted(numeros)
print(f"sorted(): {numeros_ordenados}")

# count() - Cuenta cuántas veces aparece un elemento
cantidad_unos = numeros.count(1)
print(f"Contar cuántos 1 hay: {cantidad_unos}")

# index() - Encuentra la posición de un elemento
posicion = numeros.index(5)
print(f"Posición del 5: {posicion}")

# ============================================
# 10. LISTA DE DICCIONARIOS
# ============================================

print("\n10. LISTA DE DICCIONARIOS (Datos estructurados)")
print("-"*50)

estudiantes = [
    {"nombre": "patoraya2", "edad": 25, "curso": "Python"},
    {"nombre": "Juan", "edad": 23, "curso": "JavaScript"},
    {"nombre": "María", "edad": 24, "curso": "Python"},
]

print("Estudiantes:")
for estudiante in estudiantes:
    print(f"  - {estudiante['nombre']}, {estudiante['edad']} años, curso: {estudiante['curso']}")

# ============================================
# 11. EJEMPLO PRÁCTICO: Carrito de compras
# ============================================

print("\n11. EJEMPLO PRÁCTICO: Carrito de compras")
print("-"*50)

carrito = []

# Agregar productos
carrito.append({"producto": "Laptop", "precio": 1000, "cantidad": 1})
carrito.append({"producto": "Mouse", "precio": 25, "cantidad": 2})
carrito.append({"producto": "Teclado", "precio": 75, "cantidad": 1})

print("Tu carrito:")
total = 0
for item in carrito:
    subtotal = item["precio"] * item["cantidad"]
    total += subtotal
    print(f"  - {item['producto']}: ${item['precio']} x {item['cantidad']} = ${subtotal}")

print(f"\nTotal: ${total}")

# ============================================
# RESUMEN
# ============================================

print("\n" + "="*50)
print("RESUMEN DE LISTAS")
print("="*50)

operaciones = {
    "append()": "Agrega al final",
    "insert()": "Agrega en posición",
    "remove()": "Elimina por valor",
    "pop()": "Elimina por índice",
    "len()": "Largo de la lista",
    "sorted()": "Ordena",
    "count()": "Cuenta repeticiones",
    "index()": "Encuentra posición",
}

for operacion, descripcion in operaciones.items():
    print(f"• {operacion}: {descripcion}")

print("\n" + "="*50)
print("¡FIN DEL PROGRAMA!")
print("="*50)