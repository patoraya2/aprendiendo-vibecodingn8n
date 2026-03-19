\# 📚 Diccionarios en Python



\*\*Fecha:\*\* 19 de Marzo de 2026  

\*\*Autor:\*\* patoraya2



\---



\## ¿Qué es un Diccionario?



Un \*\*diccionario\*\* es una colección de pares \*\*CLAVE: VALOR\*\*.



\### Analogía

Es como un \*\*diccionario real\*\*:

\- \*\*Palabra\*\* = Clave

\- \*\*Definición\*\* = Valor



Ejemplo:

```

palabra → definición

"python" → "lenguaje de programación"

"diccionario" → "colección de pares clave-valor"

```



\### Características

\- Las \*\*claves DEBEN ser únicas\*\*

\- Se define con `{ }`

\- Acceso rápido por clave (no por índice)

\- Flexible: puede contener diferentes tipos de datos



\### Sintaxis

```python

diccionario = {

&#x20;   "clave1": "valor1",

&#x20;   "clave2": "valor2",

&#x20;   "clave3": "valor3"

}

```



\### Ejemplo

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25,

&#x20;   "ciudad": "Tu Ciudad",

&#x20;   "profesion": "Developer"

}

```



\---



\## Crear Diccionarios



\### Diccionario vacío

```python

diccionario\_vacio = {}

```



\### Diccionario con elementos

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25,

&#x20;   "email": "patoraya2@example.com"

}

```



\### Diccionario con tipos mixtos

```python

datos\_mixtos = {

&#x20;   "nombre": "patoraya2",        # string

&#x20;   "edad": 25,                   # int

&#x20;   "altura": 1.75,               # float

&#x20;   "activo": True,               # bool

&#x20;   "hobbies": \["código", "gaming"]  # list

}

```



\---



\## Acceder a Elementos



\### Acceso con \[ ]

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25,

&#x20;   "ciudad": "Tu Ciudad"

}



print(persona\["nombre"])    # patoraya2

print(persona\["edad"])      # 25

print(persona\["ciudad"])    # Tu Ciudad

```



\### Acceso con .get()

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25

}



\# .get() devuelve el valor o None si no existe

print(persona.get("nombre"))           # patoraya2

print(persona.get("email"))            # None

print(persona.get("email", "No hay"))  # No hay (valor por defecto)

```



\### Diferencia \[ ] vs .get()

```python

persona = {"nombre": "patoraya2"}



\# Con \[ ] - Si no existe, ERROR

print(persona\["email"])  # KeyError: 'email' ❌



\# Con .get() - Si no existe, devuelve None

print(persona.get("email"))  # None ✓

```



\---



\## Agregar y Modificar Elementos



\### Agregar nuevo par clave-valor

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25

}



\# Agregar ciudad

persona\["ciudad"] = "Tu Ciudad"

print(persona)

\# {'nombre': 'patoraya2', 'edad': 25, 'ciudad': 'Tu Ciudad'}



\# Agregar email

persona\["email"] = "patoraya2@example.com"

print(persona)

\# {'nombre': 'patoraya2', 'edad': 25, 'ciudad': 'Tu Ciudad', 'email': 'patoraya2@example.com'}

```



\### Modificar (actualizar) un valor existente

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25

}



print(f"Edad antes: {persona\['edad']}")  # 25



persona\["edad"] = 26



print(f"Edad después: {persona\['edad']}")  # 26

```



\---



\## Eliminar Elementos



\### del - Elimina una clave

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25,

&#x20;   "email": "patoraya2@example.com"

}



del persona\["email"]

print(persona)

\# {'nombre': 'patoraya2', 'edad': 25}

```



\### pop() - Elimina y devuelve el valor

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25,

&#x20;   "ciudad": "Tu Ciudad"

}



\# pop() elimina y devuelve el valor

ciudad = persona.pop("ciudad")



print(ciudad)    # Tu Ciudad

print(persona)   # {'nombre': 'patoraya2', 'edad': 25}

```



\### clear() - Vaciar todo el diccionario

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25

}



persona.clear()

print(persona)  # {}

```



\---



\## Verificar si una Clave Existe



\### Usar 'in'

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25,

&#x20;   "ciudad": "Tu Ciudad"

}



\# Verificar si la clave existe

if "nombre" in persona:

&#x20;   print("✓ La clave 'nombre' existe")



if "email" in persona:

&#x20;   print("Tiene email")

else:

&#x20;   print("✗ La clave 'email' NO existe")

```



\---



\## Obtener Claves, Valores y Pares



\### .keys() - Obtener todas las claves

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25,

&#x20;   "ciudad": "Tu Ciudad"

}



print(persona.keys())  # dict\_keys(\['nombre', 'edad', 'ciudad'])



for clave in persona.keys():

&#x20;   print(clave)

```



Salida:

```

nombre

edad

ciudad

```



\### .values() - Obtener todos los valores

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25,

&#x20;   "ciudad": "Tu Ciudad"

}



print(persona.values())  # dict\_values(\['patoraya2', 25, 'Tu Ciudad'])



for valor in persona.values():

&#x20;   print(valor)

```



Salida:

```

patoraya2

25

Tu Ciudad

```



\### .items() - Obtener pares (clave, valor)

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25,

&#x20;   "ciudad": "Tu Ciudad"

}



print(persona.items())

\# dict\_items(\[('nombre', 'patoraya2'), ('edad', 25), ('ciudad', 'Tu Ciudad')])



for clave, valor in persona.items():

&#x20;   print(f"{clave}: {valor}")

```



Salida:

```

nombre: patoraya2

edad: 25

ciudad: Tu Ciudad

```



\---



\## Recorrer Diccionarios



\### Recorrer con .items()

```python

estudiantes = {

&#x20;   "patoraya2": 25,

&#x20;   "Juan": 23,

&#x20;   "María": 24,

&#x20;   "Carlos": 26

}



print("Estudiantes y sus edades:")

for nombre, edad in estudiantes.items():

&#x20;   print(f"  - {nombre}: {edad} años")

```



Salida:

```

Estudiantes y sus edades:

&#x20; - patoraya2: 25 años

&#x20; - Juan: 23 años

&#x20; - María: 24 años

&#x20; - Carlos: 26 años

```



\### Recorrer solo claves

```python

for nombre in estudiantes:

&#x20;   print(nombre)

\# Equivalente a: for nombre in estudiantes.keys():

```



\### Recorrer solo valores

```python

for edad in estudiantes.values():

&#x20;   print(edad)

```



\---



\## Diccionarios Anidados



\### Estructura

```python

empresa = {

&#x20;   "nombre": "TechCorp",

&#x20;   "empleados": {

&#x20;       "jefe": {

&#x20;           "nombre": "patoraya2",

&#x20;           "puesto": "CEO",

&#x20;           "salario": 100000

&#x20;       },

&#x20;       "desarrollador": {

&#x20;           "nombre": "Juan",

&#x20;           "puesto": "Developer",

&#x20;           "salario": 50000

&#x20;       }

&#x20;   }

}

```



\### Acceso a valores anidados

```python

print(empresa\["nombre"])                          # TechCorp

print(empresa\["empleados"]\["jefe"]\["nombre"])    # patoraya2

print(empresa\["empleados"]\["jefe"]\["salario"])   # 100000

```



\### Recorrer diccionarios anidados

```python

for tipo, info in empresa\['empleados'].items():

&#x20;   print(f"\\n{tipo.upper()}:")

&#x20;   print(f"  Nombre: {info\['nombre']}")

&#x20;   print(f"  Puesto: {info\['puesto']}")

&#x20;   print(f"  Salario: ${info\['salario']}")

```



Salida:

```

JEFE:

&#x20; Nombre: patoraya2

&#x20; Puesto: CEO

&#x20; Salario: $100000



DESARROLLADOR:

&#x20; Nombre: Juan

&#x20; Puesto: Developer

&#x20; Salario: $50000

```



\---



\## Lista de Diccionarios



\### Estructura

```python

productos = \[

&#x20;   {"nombre": "Laptop", "precio": 1000, "stock": 5},

&#x20;   {"nombre": "Mouse", "precio": 25, "stock": 50},

&#x20;   {"nombre": "Teclado", "precio": 75, "stock": 30},

&#x20;   {"nombre": "Monitor", "precio": 300, "stock": 10},

]

```



\### Recorrer lista de diccionarios

```python

for producto in productos:

&#x20;   print(f"  - {producto\['nombre']}: ${producto\['precio']} (Stock: {producto\['stock']})")

```



Salida:

```

&#x20; - Laptop: $1000 (Stock: 5)

&#x20; - Mouse: $25 (Stock: 50)

&#x20; - Teclado: $75 (Stock: 30)

&#x20; - Monitor: $300 (Stock: 10)

```



\---



\## Métodos Útiles



\### len() - Cantidad de pares

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25,

&#x20;   "ciudad": "Tu Ciudad"

}



print(len(persona))  # 3

```



\### copy() - Copiar diccionario

```python

persona\_original = {"nombre": "patoraya2", "edad": 25}

persona\_copia = persona\_original.copy()



\# Modificar la copia NO afecta el original

persona\_copia\["edad"] = 30



print(persona\_original\["edad"])  # 25

print(persona\_copia\["edad"])     # 30

```



\### update() - Actualizar con otro diccionario

```python

persona = {

&#x20;   "nombre": "patoraya2",

&#x20;   "edad": 25

}



nuevo\_datos = {

&#x20;   "email": "patoraya2@example.com",

&#x20;   "edad": 26  # Esto sobrescribe el valor existente

}



persona.update(nuevo\_datos)

print(persona)

\# {'nombre': 'patoraya2', 'edad': 26, 'email': 'patoraya2@example.com'}

```



\---



\## Ejemplo Práctico: Tienda Online



```python

\# Catálogo

catalogo = {

&#x20;   "laptop": {"precio": 1000, "stock": 5},

&#x20;   "mouse": {"precio": 25, "stock": 50},

&#x20;   "teclado": {"precio": 75, "stock": 30},

}



\# Carrito de compras

carrito = {

&#x20;   "laptop": 1,

&#x20;   "mouse": 2,

&#x20;   "teclado": 1

}



\# Calcular total

print("Carrito de compras:")

total = 0

for producto, cantidad in carrito.items():

&#x20;   precio = catalogo\[producto]\["precio"]

&#x20;   subtotal = precio \* cantidad

&#x20;   total += subtotal

&#x20;   print(f"  - {producto.capitalize()}: ${precio} x {cantidad} = ${subtotal}")



print(f"\\nTotal: ${total}")

```



Salida:

```

Carrito de compras:

&#x20; - Laptop: $1000 x 1 = $1000

&#x20; - Mouse: $25 x 2 = $50

&#x20; - Teclado: $75 x 1 = $75



Total: $1125

```



\---



\## Ejemplo Práctico: Base de Datos de Usuarios



```python

\# Base de datos simulada

usuarios = {

&#x20;   "patoraya2": {

&#x20;       "email": "patoraya2@example.com",

&#x20;       "edad": 25,

&#x20;       "ciudad": "Tu Ciudad",

&#x20;       "activo": True

&#x20;   },

&#x20;   "juan": {

&#x20;       "email": "juan@example.com",

&#x20;       "edad": 23,

&#x20;       "ciudad": "Otra Ciudad",

&#x20;       "activo": True

&#x20;   },

&#x20;   "maria": {

&#x20;       "email": "maria@example.com",

&#x20;       "edad": 24,

&#x20;       "ciudad": "Ciudad X",

&#x20;       "activo": False

&#x20;   }

}



\# Mostrar todos los usuarios

print("Usuarios registrados:")

for username, datos in usuarios.items():

&#x20;   estado = "✓ Activo" if datos\["activo"] else "✗ Inactivo"

&#x20;   print(f"  @{username}")

&#x20;   print(f"    Email: {datos\['email']}")

&#x20;   print(f"    Edad: {datos\['edad']}")

&#x20;   print(f"    Estado: {estado}\\n")



\# Buscar usuario específico

username\_buscado = "patoraya2"

if username\_buscado in usuarios:

&#x20;   usuario = usuarios\[username\_buscado]

&#x20;   print(f"Perfil de {username\_buscado}:")

&#x20;   print(f"  Email: {usuario\['email']}")

&#x20;   print(f"  Edad: {usuario\['edad']}")

else:

&#x20;   print(f"Usuario {username\_buscado} no encontrado")

```



Salida:

```

Usuarios registrados:

&#x20; @patoraya2

&#x20;   Email: patoraya2@example.com

&#x20;   Edad: 25

&#x20;   Estado: ✓ Activo



&#x20; @juan

&#x20;   Email: juan@example.com

&#x20;   Edad: 23

&#x20;   Estado: ✓ Activo



&#x20; @maria

&#x20;   Email: maria@example.com

&#x20;   Edad: 24

&#x20;   Estado: ✗ Inactivo



Perfil de patoraya2:

&#x20; Email: patoraya2@example.com

&#x20; Edad: 25

```



\---



\## Tabla Resumen de Métodos



| Método | Uso | Ejemplo |

|--------|-----|---------|

| `dict\[clave]` | Acceder a valor | `persona\["nombre"]` |

| `.get()` | Acceder seguro | `persona.get("email", "N/A")` |

| `dict\[clave] = valor` | Agregar/Modificar | `persona\["edad"] = 26` |

| `del dict\[clave]` | Eliminar | `del persona\["email"]` |

| `.pop()` | Eliminar y devolver | `edad = persona.pop("edad")` |

| `.clear()` | Vaciar | `persona.clear()` |

| `clave in dict` | Verificar | `"nombre" in persona` |

| `.keys()` | Todas las claves | `persona.keys()` |

| `.values()` | Todos los valores | `persona.values()` |

| `.items()` | Pares clave-valor | `persona.items()` |

| `len()` | Cantidad de pares | `len(persona)` |

| `.copy()` | Copiar | `copia = persona.copy()` |

| `.update()` | Actualizar | `persona.update(otros)` |



\---



\## Errores Comunes



\### ❌ Error 1: Acceder a clave inexistente

```python

\# INCORRECTO

persona = {"nombre": "patoraya2"}

print(persona\["email"])  # KeyError: 'email' ❌



\# CORRECTO

print(persona.get("email", "No disponible"))  # No disponible ✓

```



\### ❌ Error 2: Confundir claves duplicadas

```python

\# INCORRECTO - La segunda clave sobrescribe la primera

diccionario = {

&#x20;   "edad": 25,

&#x20;   "edad": 26  # Esto reemplaza el valor anterior

}

print(diccionario)  # {'edad': 26}



\# CORRECTO - Usa claves diferentes

diccionario = {

&#x20;   "edad\_actual": 25,

&#x20;   "edad\_proxima": 26

}

```



\### ❌ Error 3: Usar tipos mutables como claves

```python

\# INCORRECTO - Las listas NO pueden ser claves

diccionario = {

&#x20;   \[1, 2, 3]: "valor"  # TypeError ❌

}



\# CORRECTO - Usa tipos inmutables (strings, números, tuplas)

diccionario = {

&#x20;   (1, 2, 3): "valor",  # Tupla ✓

&#x20;   "lista": \[1, 2, 3]   # Lista como valor ✓

}

```



\---



\## Lo que aprendimos hoy



✅ Crear diccionarios  

✅ Acceder a elementos por clave  

✅ Agregar y modificar pares  

✅ Eliminar elementos  

✅ Verificar si existe una clave  

✅ Obtener claves, valores y pares  

✅ Recorrer diccionarios  

✅ Diccionarios anidados  

✅ Lista de diccionarios  

✅ Métodos útiles  

✅ Ejemplos prácticos  



\---



\## Próximos Temas



\- \[ ] Tuplas (colecciones inmutables)

\- \[ ] Conjuntos (Sets)

\- \[ ] Comprensión de diccionarios

\- \[ ] Funciones

\- \[ ] Manejo de errores (try/except)

\- \[ ] Manejo de archivos



\---



\## Mi Script de Hoy



Creé: `ejemplos/05-diccionarios-basico.py`



Contiene:

\- Crear y acceder a diccionarios

\- Agregar, modificar y eliminar pares

\- Verificar existencia de claves

\- Métodos: keys(), values(), items()

\- Diccionarios anidados

\- Lista de diccionarios

\- Ejemplos: tienda online y base de datos



\---



\*\*Última actualización:\*\* 19/03/2026

