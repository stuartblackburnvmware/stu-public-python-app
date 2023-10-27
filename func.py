from typing import Any
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (replace with your own data or database access)
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

@app.route('/')
def hello_world():
    return "This is the greatest PUBLIC Python app ever written. Trust me."

# API to get a list of items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# API to get details of a specific item
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is not None:
        return jsonify(item)
    return "Item not found", 404

def main(req: Any):
    # Run the Flask app
    app.run(debug=True)

