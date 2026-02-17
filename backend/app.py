from flask import Flask, request, jsonify
from flask_cors import CORS
# TASK: Install these via terminal: pip install flask-bcrypt Flask-JWT-Extended
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime

app = Flask(__name__)
CORS(app)

# --- STEP 2: BACKEND CONFIGURATION ---
# The Secret Key is used to sign the JWTs so they cannot be forged.
app.config['JWT_SECRET_KEY'] = 'super-secret-nextgen-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=24)

bcrypt = Bcrypt(app)  # Initializes the password hashing tool
jwt = JWTManager(app)  # Initializes the JWT manager

# Mock Database
# In a real app, users would be in a MySQL table.
# For now, we store them here to demonstrate hashing.
users_db = {}

products = [
    {"id": 1, "name": "Smart Watch Pro", "price": 199.99},
    {"id": 2, "name": "Noise Cancel Buds", "price": 149.50}
]


# --- TASK: HASH PASSWORDS ---
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Missing credentials"}), 400

    # Step: Hash the password before saving it
    # We never store plain text like "password123"
    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

    # Save the user with their SCRAMBLED password
    users_db[username] = {
        "username": username,
        "password": hashed_pw
    }

    return jsonify({"message": f"User {username} registered securely!"}), 201


# --- TASK: GENERATE JWT ON LOGIN ---
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = users_db.get(username)

    # Adding a check to ensure user exists before hashing
    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify({
            "message": "Login successful!",
            "token": access_token
        }), 200

    return jsonify({"message": "Invalid username or password"}), 401

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products), 200


# --- TASK: PROTECT ENDPOINTS ---
@app.route('/checkout', methods=['POST'])
@jwt_required()  # This makes the endpoint private; a valid token MUST be sent
def checkout():
    # Only users with a valid JWT can reach this code
    current_user = get_jwt_identity()
    return jsonify({
        "message": f"Order placed successfully for {current_user}!",
        "order_id": 999
    }), 201


@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    return jsonify({"message": f"Product {data.get('product_id')} added to cart!"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)