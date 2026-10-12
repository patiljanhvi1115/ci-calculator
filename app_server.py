from flask import Flask, request, jsonify
from calculator import add, divide

app = Flask(__name__)

@app.route("/")
def home():
    return "Calculator App is running!"

@app.route("/add", methods=["GET"])
def addition():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify({"result": add(a, b)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/divide", methods=["GET"])
def division():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify({"result": divide(a, b)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
