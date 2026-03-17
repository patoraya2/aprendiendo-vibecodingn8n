# Mi primer script en Python
# Fecha: 16 de Marzo de 2026
# Autor: patoraya2

print("¡Hola, mundo!")
print("Este es mi primer script en Python")

# Variables básicas
nombre = "patoraya2"
fecha = "16/03/2026"

print(f"\nMi nombre es: {nombre}")
print(f"Hoy es: {fecha}")

# Función simple
def saludar(nombre):
    """Una función que saluda"""
    return f"¡Hola, {nombre}! Bienvenido a tu viaje de aprendizaje."

print("\n" + saludar(nombre))
