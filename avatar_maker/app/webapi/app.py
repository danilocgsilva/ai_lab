from flask import Flask
from flask_cors import CORS
from domain.Models.Entry import Entry
from domain.models import models_names
from webapi.ModelToDict import ModelToDict

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    models_return = list(map(lambda x: ModelToDict.convert_model(Entry(x['name'], x['suggestion'])), models_names))
    return models_return
