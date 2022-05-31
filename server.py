from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect
from functions import F1

csrf = CSRFProtect()
f = F1()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "OK", "msg": "HOME!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)