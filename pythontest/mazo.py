import random

def crear_mazo():
    """Crea un mazo estándar de 52 cartas con valores y tipos."""
    valores = {
        "As": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 11, "Q": 12, "K": 13
    }
    tipos = ["Trébol", "Diamante", "Corazón", "Espada"]
    mazo = []
    for tipo in tipos:
        for nombre, valor in valores.items():
            mazo.append({"nombre": nombre, "tipo": tipo, "valor": valor})
    return mazo

def extraer_cartas(mazo):
    """Extrae entre 3 y 5 cartas al azar del mazo."""
    cantidad = random.randint(3, 5)  # Selecciona un número aleatorio entre 3 y 5
    return random.sample(mazo, cantidad)
