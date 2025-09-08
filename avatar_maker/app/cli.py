from domain.models import models_names
import sys
import argparse
from domain.Model import Model

parser = argparse.ArgumentParser()
parser.add_argument('--picked-models', '-p', action='store_true', help='List just the author selected models')
parser.add_argument('--get-url', '-r', action='store_true', help='Tries to guess the model url in Hugging Face')
args = parser.parse_args()

models_objs = map(lambda x: Model(x['name'], x['suggestion']), models_names)
if args.get_url:
    models_objs = map(lambda x: x.withUrl(), models_objs)

if args.picked_models:
    for model in models_objs:
        if model.suggestion == 'picked':
            print(model.get)
    sys.exit(0)

for model in models_objs:
    print(model.get)
