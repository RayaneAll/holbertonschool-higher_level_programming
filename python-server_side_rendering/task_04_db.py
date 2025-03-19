import json
import csv
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

def load_products_from_json():
    """Load product data from JSON file."""
    try:
        with open("data/products.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def load_products_from_csv():
    """Load product data from CSV file."""
    try:
        with open("data/products.csv", newline="") as file:
            reader = csv.DictReader(file)
            return [
                {"id": int(row["id"]), "name": row["name"], "category": row["category"], "price": float(row["price"])}
                for row in reader
            ]
    except (FileNotFoundError, csv.Error, ValueError):
        return []

def load_products_from_sql():
    """Load product data from SQLite database."""
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in cursor.fetchall()]
        conn.close()
        return products
    except sqlite3.Error:
        return []

@app.route('/products')
def display_products():
    """Route to display products from JSON, CSV, or SQLite"""
    source = request.args.get("source", "").lower()
    product_id = request.args.get("id")

    if source == "json":
        products = load_products_from_json()
    elif source == "csv":
        products = load_products_from_csv()
    elif source == "sql":
        products = load_products_from_sql()
    else:
        return render_template("product_display.html", error="Wrong source. Use 'json', 'csv', or 'sql'.")

    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p["id"] == product_id]
            if not products:
                return render_template("product_display.html", error=f"Product with ID {product_id} not found.")
        except ValueError:
            return render_template("product_display.html", error="Invalid product ID format.")

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
