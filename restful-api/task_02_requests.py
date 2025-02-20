#!/usr/bin/python3
"""Task: Consuming and processing data from an API using Python"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder API and prints their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"  # URL de la API
    response = requests.get(url)  # Realiza la solicitud GET

    print("Status Code:", response.status_code)  # Muestra el código

    if response.status_code == 200:  # Si la solicitud es exitosa (200 OK)
        data = response.json()  # Convierte la respuesta en un objeto JSON

        for post in data:  # Itera sobre los posts
            print(post.get("title"))  # Imprime el título de cada post
    else:
        print("Error al obtener los datos.")


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder API and saves them into a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"  # URL de la API
    response = requests.get(url)  # Realiza la solicitud GET

    if response.status_code == 200:  # Si la solicitud es exitosa
        data = response.json()  # Convierte la respuesta en JSON

        # Crea una lista de diccionarios con id, title y body
        posts_list = [
            {"id": post.get("id"), "title": post.get("title"),
             "body": post.get("body")}
            for post in data
        ]

        # Guarda los datos en un archivo CSV
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()  # Escribe los encabezados
            writer.writerows(posts_list)  # Escribe los datos

        print("Datos guardados en 'posts.csv'")
    else:
        print("Error al obtener los datos.")
