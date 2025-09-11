import google.generativeai as genai
from functions import format_module_info, format2, configure_genai
import re

configure_genai()

models = genai.list_models()

index = 1
for model in models:
    string_returned = format2(index, model)
    if re.search(r'gemma', string_returned, re.IGNORECASE):
        print("-" * 40)
        print(
            format_module_info(index, model)
        )
    # print(
    #     format_module_info(index, model)
    # )

    index += 1


