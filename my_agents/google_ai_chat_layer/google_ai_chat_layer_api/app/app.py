from flask import Flask, request, jsonify
from flask_cors import CORS
from ai import getAnswer

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def respondsQuestion():
    question = request.get_json()["question"]
    response = getAnswer(question)
    return {
        "answer": response.content
    }
