import json
import csv
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

@app.route('/products')
def display_products():
    """Route to display products from JSON or CSV file based on query parameters."""
    source = request.args.get("source", "").lower()
    product_id = request.args.get("id")

    if source == "json":
        products = load_products_from_json()
    elif source == "csv":
        products = load_products_from_csv()
    else:
        return render_template("product_display.html", error="Wrong source. Use 'json' or 'csv'.")

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
