#!/usr/bin/env python3
from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

def read_json():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception:
        return []

def read_csv():
    products = []
    try:
        with open("products.csv", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        return []
    return products

@app.route('/products')
def display_products():
    source = request.args.get("source")
    id_param = request.args.get("id")

    # Seleccionar fuente de datos
    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    else:
        return render_template("product_display.html", error="Wrong source")

    # Filtrar por id si se pasa
    if id_param:
        try:
            id_num = int(id_param)
            products = [p for p in products if p["id"] == id_num]
            if not products:
                return render_template("product_display.html", error="Product not found")
        except ValueError:
            return render_template("product_display.html", error="Invalid ID format")

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
