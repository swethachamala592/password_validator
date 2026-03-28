from flask import Flask, request, jsonify
from flask_cors import CORS
from password import validate_password

app = Flask(__name__)
CORS(app)  # 👈 ADD THIS

@app.route("/validate", methods=["POST"])
def validate():
    data = request.json
    password = data.get("password")

    result = validate_password(password)

    return jsonify({"is_valid": result})

if __name__ == "__main__":
    app.run(debug=True)