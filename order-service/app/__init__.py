from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
@app.route("/health")
def health():
    return jsonify(status="up")

