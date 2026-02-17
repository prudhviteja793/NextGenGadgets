from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This allows your website to talk to the API

# Mock Data (This simulates your database for now)
products = [
    {"id": 1, "name": "Smart Watch Pro", "price": 199.99},
    {"id": 2, "name": "Noise Cancel Buds", "price": 149.50}
]

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    return jsonify({"message": f"User {data.get('username')} registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    return jsonify({"message": "Login successful!", "token": "dummy-token-123"}), 200

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    return jsonify({"message": f"Product {data.get('product_id')} added to cart!"}), 200

@app.route('/checkout', methods=['POST'])
def checkout():
    return jsonify({"message": "Order placed successfully!", "order_id": 999}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)