# app.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "This is the greatest PUBLIC Python app ever written. Trust me."

@app.route('/api/items', methods=['GET'])
def get_items():
    items = ["item1", "item2", "item3"]
    return jsonify(items)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = f"item{item_id}"
    return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)
