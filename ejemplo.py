import random

# Lista de nombres posibles
nombres = ['Juan', 'Pedro', 'Maria', 'Ana', 'Pablo', 'Sofia', 'Lucas', 'Marta', 'Jorge', 'Laura']

# Función para generar un nombre aleatorio
def generar_nombre():
    return random.choice(nombres)

# Prueba de la función
print(generar_nombre())
