from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime

app = Flask(__name__)
CORS(app)

# --- CONFIGURATION ---
app.config['JWT_SECRET_KEY'] = 'super-secret-nextgen-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=24)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# --- DATABASE (Week 1-4 Data preserved) ---
users_db = {}
products = [
    {"id": 1, "name": "Smart Watch Pro", "price": 199.99},
    {"id": 2, "name": "Noise Cancel Buds", "price": 149.50}
]

# Week 5: Data for the Reporting Charts
orders_db = [
    {"total": 350.00, "date": "Mon"},
    {"total": 450.00, "date": "Tue"},
    {"total": 200.00, "date": "Wed"},
    {"total": 600.00, "date": "Thu"},
    {"total": 800.00, "date": "Fri"}
]

# --- USER AUTHENTICATION (Week 4) ---
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"message": "Missing credentials"}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    users_db[username] = {"username": username, "password": hashed_pw}
    return jsonify({"message": f"User {username} registered securely!"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = users_db.get(username)

    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify({"message": "Login successful!", "token": access_token}), 200
    return jsonify({"message": "Invalid username or password"}), 401

# --- STORE LOGIC (Week 1-3) ---
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

@app.route('/api/checkout', methods=['POST'])
@jwt_required()
def checkout():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Order placed successfully for {current_user}!", "order_id": 999}), 201

# --- ADMIN DASHBOARD & REPORTING (Week 5) ---
@app.route('/api/admin/stats', methods=['GET'])
@jwt_required()
def get_admin_stats():
    total_sales = sum(order['total'] for order in orders_db)
    return jsonify({
        "total_revenue": total_sales,
        "total_users": len(users_db),
        "sales_labels": [o['date'] for o in orders_db],
        "sales_values": [o['total'] for o in orders_db]
    }), 200

@app.route('/api/admin/products', methods=['POST'])
@jwt_required()
def add_admin_product():
    data = request.json
    new_product = {
        "id": len(products) + 1,
        "name": data['name'],
        "price": float(data['price'])
    }
    products.append(new_product)
    return jsonify({"message": "Product added!"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)