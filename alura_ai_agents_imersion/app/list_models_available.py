import google.generativeai as genai
from functions import format_module_info, format2, configure_genai
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--only-gemma',
    '-o',
    action='store_true',
    help='Show only Gemma models'
)

args = parser.parse_args()

configure_genai()

models = genai.list_models()

index = 1
for model in models:
    string_returned = format2(index, model)
    index += 1
    if args.only_gemma and not re.search(r'gemma', string_returned, re.IGNORECASE):
        continue
    print("-" * 40)
    print(
        format_module_info(index, model)
    )



