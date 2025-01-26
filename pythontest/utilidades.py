def mostrar_cartas(cartas):
    """Muestra las cartas extraídas con sus nombres al revés y suma los valores."""
    suma_valores = 0
    print("=== Tus cartas extraídas ===")
    for carta in cartas:
        nombre_completo = f"{carta['nombre']} de {carta['tipo']}"
        nombre_reverso = nombre_completo[::-1]  # Nombre al revés
        suma_valores += carta["valor"]
        print(f"Carta: {nombre_completo} | Al revés: {nombre_reverso} | Valor: {carta['valor']}")
    print("============================")
    print(f"Suma total de valores: {suma_valores}")
