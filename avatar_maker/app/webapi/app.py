from flask import Flask
from flask_cors import CORS
from domain.Model import Model
from domain.models import models_names
from webapi.ModelToDict import ModelToDict

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    models_return = list(map(lambda x: ModelToDict.convert(Model(x['name'], x['suggestion'])), models_names))
    return models_return
