# Diccionarios en Python - Almacenar datos con claves
# Fecha: 19 de Marzo de 2026
# Autor: patoraya2

print("="*60)
print("DICCIONARIOS EN PYTHON")
print("="*60)

# ============================================
# 1. ¿QUÉ ES UN DICCIONARIO?
# ============================================

print("\n1. ¿QUÉ ES UN DICCIONARIO?")
print("-"*60)

# Un diccionario es una colección de pares CLAVE: VALOR
# Se define con { }
# Las claves DEBEN ser únicas

persona = {
    "nombre": "patoraya2",
    "edad": 25,
    "ciudad": "Tu Ciudad",
    "profesion": "Developer"
}

print(f"Diccionario persona: {persona}")

# ============================================
# 2. ACCEDER A ELEMENTOS
# ============================================

print("\n2. ACCEDER A ELEMENTOS")
print("-"*60)

persona = {
    "nombre": "patoraya2",
    "edad": 25,
    "ciudad": "Tu Ciudad",
    "profesion": "Developer"
}

# Acceder por CLAVE (no por índice como en listas)
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")
print(f"Ciudad: {persona['ciudad']}")
print(f"Profesión: {persona['profesion']}")

# Método alternativo: .get()
print(f"\nCon .get():")
print(f"Nombre: {persona.get('nombre')}")
print(f"Email: {persona.get('email', 'No disponible')}")  # Si no existe, devuelve default

# ============================================
# 3. AGREGAR Y MODIFICAR ELEMENTOS
# ============================================

print("\n3. AGREGAR Y MODIFICAR ELEMENTOS")
print("-"*60)

persona = {
    "nombre": "patoraya2",
    "edad": 25
}

print(f"Original: {persona}")

# Agregar un nuevo par clave-valor
persona["ciudad"] = "Tu Ciudad"
print(f"Después de agregar ciudad: {persona}")

# Agregar otro
persona["email"] = "patoraya2@example.com"
print(f"Después de agregar email: {persona}")

# Modificar (actualizar) un valor existente
persona["edad"] = 26
print(f"Después de modificar edad: {persona}")

# ============================================
# 4. ELIMINAR ELEMENTOS
# ============================================

print("\n4. ELIMINAR ELEMENTOS")
print("-"*60)

persona = {
    "nombre": "patoraya2",
    "edad": 25,
    "ciudad": "Tu Ciudad",
    "email": "patoraya2@example.com"
}

print(f"Original: {persona}")

# del - Elimina una clave
del persona["email"]
print(f"Después de del persona['email']: {persona}")

# pop() - Elimina y devuelve el valor
ciudad = persona.pop("ciudad")
print(f"Valor eliminado: {ciudad}")
print(f"Diccionario ahora: {persona}")

# ============================================
# 5. VERIFICAR SI UNA CLAVE EXISTE
# ============================================

print("\n5. VERIFICAR SI UNA CLAVE EXISTE")
print("-"*60)

persona = {
    "nombre": "patoraya2",
    "edad": 25,
    "ciudad": "Tu Ciudad"
}

# Usar 'in' para verificar
if "nombre" in persona:
    print("✓ La clave 'nombre' existe")

if "email" in persona:
    print("✓ La clave 'email' existe")
else:
    print("✗ La clave 'email' NO existe")

# ============================================
# 6. OBTENER CLAVES, VALORES Y PARES
# ============================================

print("\n6. OBTENER CLAVES, VALORES Y PARES")
print("-"*60)

persona = {
    "nombre": "patoraya2",
    "edad": 25,
    "ciudad": "Tu Ciudad",
    "profesion": "Developer"
}

# .keys() - Obtener todas las claves
print("Claves:")
for clave in persona.keys():
    print(f"  - {clave}")

# .values() - Obtener todos los valores
print("\nValores:")
for valor in persona.values():
    print(f"  - {valor}")

# .items() - Obtener pares (clave, valor)
print("\nPares (clave, valor):")
for clave, valor in persona.items():
    print(f"  - {clave}: {valor}")

# ============================================
# 7. RECORRER DICCIONARIOS
# ============================================

print("\n7. RECORRER DICCIONARIOS")
print("-"*60)

estudiantes = {
    "patoraya2": 25,
    "Juan": 23,
    "María": 24,
    "Carlos": 26
}

print("Estudiantes y sus edades:")
for nombre, edad in estudiantes.items():
    print(f"  - {nombre}: {edad} años")

# ============================================
# 8. DICCIONARIOS ANIDADOS
# ============================================

print("\n8. DICCIONARIOS ANIDADOS")
print("-"*60)

# Un diccionario dentro de otro diccionario
empresa = {
    "nombre": "TechCorp",
    "empleados": {
        "jefe": {
            "nombre": "patoraya2",
            "puesto": "CEO",
            "salario": 100000
        },
        "desarrollador": {
            "nombre": "Juan",
            "puesto": "Developer",
            "salario": 50000
        }
    }
}

print(f"Empresa: {empresa['nombre']}")
print(f"Jefe: {empresa['empleados']['jefe']['nombre']}")
print(f"Puesto: {empresa['empleados']['jefe']['puesto']}")
print(f"Salario CEO: ${empresa['empleados']['jefe']['salario']}")

# Recorrer diccionarios anidados
print("\nTodos los empleados:")
for tipo, info in empresa['empleados'].items():
    print(f"\n  {tipo.upper()}:")
    print(f"    Nombre: {info['nombre']}")
    print(f"    Puesto: {info['puesto']}")
    print(f"    Salario: ${info['salario']}")

# ============================================
# 9. LISTA DE DICCIONARIOS (Datos estructurados)
# ============================================

print("\n9. LISTA DE DICCIONARIOS")
print("-"*60)

# Una lista que contiene múltiples diccionarios
productos = [
    {"nombre": "Laptop", "precio": 1000, "stock": 5},
    {"nombre": "Mouse", "precio": 25, "stock": 50},
    {"nombre": "Teclado", "precio": 75, "stock": 30},
    {"nombre": "Monitor", "precio": 300, "stock": 10},
]

print("Catálogo de productos:")
for producto in productos:
    print(f"  - {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")

# ============================================
# 10. MÉTODOS ÚTILES
# ============================================

print("\n10. MÉTODOS ÚTILES")
print("-"*60)

persona = {
    "nombre": "patoraya2",
    "edad": 25,
    "ciudad": "Tu Ciudad"
}

# len() - Cantidad de pares
print(f"Cantidad de pares: {len(persona)}")

# clear() - Vaciar diccionario
copia = persona.copy()
copia.clear()
print(f"Diccionario vaciado: {copia}")

# update() - Actualizar con otro diccionario
persona.update({"email": "patoraya2@example.com", "edad": 26})
print(f"Después de update: {persona}")

# ============================================
# 11. EJEMPLO PRÁCTICO: Tienda Online
# ============================================

print("\n11. EJEMPLO PRÁCTICO: Tienda Online")
print("-"*60)

# Catálogo
catalogo = {
    "laptop": {"precio": 1000, "stock": 5},
    "mouse": {"precio": 25, "stock": 50},
    "teclado": {"precio": 75, "stock": 30},
}

# Carrito de compras
carrito = {}

# Agregar productos al carrito
carrito["laptop"] = 1
carrito["mouse"] = 2
carrito["teclado"] = 1

# Calcular total
print("Carrito de compras:")
total = 0
for producto, cantidad in carrito.items():
    precio = catalogo[producto]["precio"]
    subtotal = precio * cantidad
    total += subtotal
    print(f"  - {producto.capitalize()}: ${precio} x {cantidad} = ${subtotal}")

print(f"\nTotal: ${total}")

# ============================================
# 12. EJEMPLO PRÁCTICO: Base de datos de usuarios
# ============================================

print("\n12. EJEMPLO PRÁCTICO: Base de datos de usuarios")
print("-"*60)

# Base de datos simulada
usuarios = {
    "patoraya2": {
        "email": "patoraya2@example.com",
        "edad": 25,
        "ciudad": "Tu Ciudad",
        "activo": True
    },
    "juan": {
        "email": "juan@example.com",
        "edad": 23,
        "ciudad": "Otra Ciudad",
        "activo": True
    },
    "maria": {
        "email": "maria@example.com",
        "edad": 24,
        "ciudad": "Ciudad X",
        "activo": False
    }
}

# Mostrar todos los usuarios
print("Usuarios registrados:")
for username, datos in usuarios.items():
    estado = "✓ Activo" if datos["activo"] else "✗ Inactivo"
    print(f"  @{username}")
    print(f"    Email: {datos['email']}")
    print(f"    Edad: {datos['edad']}")
    print(f"    Ciudad: {datos['ciudad']}")
    print(f"    Estado: {estado}\n")

# Buscar usuario específico
username_buscado = "patoraya2"
if username_buscado in usuarios:
    usuario = usuarios[username_buscado]
    print(f"Perfil de {username_buscado}:")
    print(f"  Email: {usuario['email']}")
    print(f"  Edad: {usuario['edad']}")
else:
    print(f"Usuario {username_buscado} no encontrado")

# ============================================
# 13. COMPARAR DICCIONARIOS
# ============================================

print("\n13. COMPARAR DICCIONARIOS")
print("-"*60)

dict1 = {"nombre": "patoraya2", "edad": 25}
dict2 = {"nombre": "patoraya2", "edad": 25}
dict3 = {"nombre": "Juan", "edad": 23}

print(f"dict1 == dict2: {dict1 == dict2}")  # True
print(f"dict1 == dict3: {dict1 == dict3}")  # False

# ============================================
# RESUMEN
# ============================================

print("\n" + "="*60)
print("RESUMEN DE DICCIONARIOS")
print("="*60)

operaciones = {
    "Crear": "persona = {'nombre': 'patoraya2', 'edad': 25}",
    "Acceder": "persona['nombre']",
    "Agregar": "persona['email'] = 'email@example.com'",
    "Modificar": "persona['edad'] = 26",
    "Eliminar": "del persona['email']",
    "Verificar": "'nombre' in persona",
    "Claves": "persona.keys()",
    "Valores": "persona.values()",
    "Pares": "persona.items()",
    "Largo": "len(persona)",
    "Copiar": "persona.copy()",
    "Vaciar": "persona.clear()",
    "Actualizar": "persona.update({'email': 'nuevo@example.com'})",
}

for operacion, codigo in operaciones.items():
    print(f"• {operacion}: {codigo}")

print("\n" + "="*60)
print("¡FIN DEL PROGRAMA!")
print("="*60)