from mazo import crear_mazo, extraer_cartas
from utilidades import mostrar_cartas

if __name__ == "__main__":
    print("¡Bienvenido al juego de las cartas!")
    mazo = crear_mazo()
    print("Preparando el mazo de cartas...\n")

    cartas_extraidas = extraer_cartas(mazo)
    mostrar_cartas(cartas_extraidas)

    print("\n¡Gracias por jugar!")
