# Variables y Tipos de Datos en Python
# Fecha: 17 de Marzo de 2026
# Autor: patoraya2

print("="*50)
print("VARIABLES Y TIPOS DE DATOS EN PYTHON")
print("="*50)

# ============================================
# 1. VARIABLES - Contenedores de información
# ============================================

print("\n1. VARIABLES")
print("-"*50)

# Una variable es como una caja donde guardas información
nombre = "patoraya2"
edad = 25
precio = 19.99
activo = True

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Precio: {precio}")
print(f"¿Activo?: {activo}")

# ============================================
# 2. TIPOS DE DATOS PRINCIPALES
# ============================================

print("\n2. TIPOS DE DATOS")
print("-"*50)

# STRING (Texto)
mensaje = "Hola, mundo"
print(f"String: {mensaje}")
print(f"Tipo: {type(mensaje)}")

# INTEGER (Número entero)
numero_entero = 42
print(f"\nEntero: {numero_entero}")
print(f"Tipo: {type(numero_entero)}")

# FLOAT (Número decimal)
numero_decimal = 3.14159
print(f"\nDecimal: {numero_decimal}")
print(f"Tipo: {type(numero_decimal)}")

# BOOLEAN (Verdadero/Falso)
verdadero = True
falso = False
print(f"\nBooleano (True): {verdadero}")
print(f"Booleano (False): {falso}")
print(f"Tipo: {type(verdadero)}")

# ============================================
# 3. OPERACIONES CON VARIABLES
# ============================================

print("\n3. OPERACIONES")
print("-"*50)

# Suma
a = 10
b = 5
suma = a + b
print(f"Suma: {a} + {b} = {suma}")

# Resta
resta = a - b
print(f"Resta: {a} - {b} = {resta}")

# Multiplicación
multiplicacion = a * b
print(f"Multiplicación: {a} * {b} = {multiplicacion}")

# División
division = a / b
print(f"División: {a} / {b} = {division}")

# Potencia
potencia = a ** 2
print(f"Potencia: {a}² = {potencia}")

# Módulo (residuo)
modulo = a % 3
print(f"Módulo: {a} % 3 = {modulo}")

# ============================================
# 4. CONCATENACIÓN DE STRINGS
# ============================================

print("\n4. CONCATENACIÓN DE STRINGS")
print("-"*50)

nombre = "patoraya2"
apellido = "Developer"
ciudad = "Tu Ciudad"

# Forma 1: Con +
resultado1 = nombre + " " + apellido
print(f"Con +: {resultado1}")

# Forma 2: Con f-strings (recomendado)
resultado2 = f"{nombre} {apellido} de {ciudad}"
print(f"Con f-string: {resultado2}")

# ============================================
# 5. CONVERSIÓN DE TIPOS
# ============================================

print("\n5. CONVERSIÓN DE TIPOS")
print("-"*50)

# String a Entero
numero_texto = "123"
numero_convertido = int(numero_texto)
print(f"String '{numero_texto}' convertido a int: {numero_convertido}")

# Entero a String
numero = 456
numero_string = str(numero)
print(f"Int {numero} convertido a string: '{numero_string}'")

# String a Float
precio_texto = "19.99"
precio_float = float(precio_texto)
print(f"String '{precio_texto}' convertido a float: {precio_float}")

# ============================================
# 6. INPUT - Recibir datos del usuario
# ============================================

print("\n6. INPUT - Recibir datos")
print("-"*50)

nombre_usuario = input("¿Cuál es tu nombre?: ")
edad_usuario = int(input("¿Cuántos años tienes?: "))

print(f"\nHola {nombre_usuario}, tienes {edad_usuario} años.")
print(f"El año que viene tendrás {edad_usuario + 1} años.")

# ============================================
# 7. RESUMEN
# ============================================

print("\n" + "="*50)
print("RESUMEN DE TIPOS DE DATOS")
print("="*50)

resumen = {
    "String": "Texto, entre comillas",
    "Integer": "Números enteros, sin punto decimal",
    "Float": "Números decimales, con punto",
    "Boolean": "True o False",
    "List": "Colección de elementos [1, 2, 3]",
    "Dictionary": "Pares clave-valor {'edad': 25}",
}

for tipo, descripcion in resumen.items():
    print(f"• {tipo}: {descripcion}")

print("\n" + "="*50)
print("¡FIN DEL PROGRAMA!")
print("="*50)
