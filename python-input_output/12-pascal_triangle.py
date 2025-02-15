#!/usr/bin/python3
"""Module to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal’s Triangle of size n.

    Args:
        n (int): Number of rows in Pascal’s Triangle.

    Returns:
        list: A list of lists of integers representing Pascal’s Triangle.
    """
    if n <= 0:
        return []  # Si n es 0 o negativo, devolvemos una lista vacía.

    triangle = [[1]]  # Empezamos con la primera fila que siempre es [1].

    for i in range(1, n):  # Comenzamos desde la segunda fila hasta la fila n.
        previous_row = triangle[i - 1]  # Obtenemos la fila anterior.
        new_row = [1]  # Cada nueva fila comienza con 1.

        for j in range(len(previous_row) - 1):
            new_row.append(
                previous_row[j] + previous_row[j + 1]
            )  # Suma los valores superiores.

        new_row.append(1)  # Terminamos cada fila con 1.
        triangle.append(new_row)  # Agregamos la nueva fila al triángulo.

    return triangle  # Devolvemos la lista de listas con el triángulo completo.
