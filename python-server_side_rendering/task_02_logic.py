import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def show_items():
    """Load items from a JSON file and render them in an HTML template"""
    try:
        with open("data/items.json", "r") as file:
            data = json.load(file)
            items = data.get("items", [])  # Default to an empty list if "items" is missing
    except (FileNotFoundError, json.JSONDecodeError):
        items = []  # Handle missing or invalid JSON files

    return render_template("items.html", items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
