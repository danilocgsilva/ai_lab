import os
import google.generativeai as genai

GOOGLE_API_KEY = os.environ.get("GEMINI_KEY")   # <-- make sure this is set

if not GOOGLE_API_KEY:
    raise RuntimeError("Please export GEMINI_KEY before running")

genai.configure(api_key=GOOGLE_API_KEY)

# The call returns a list of `genai.types.Model` objects
models = genai.list_models()          # ← This is the function you asked for
models_list = list(models)

print(f"Found {len(models_list)} model(s)")

print(type(models_list[0]).__name__)

print(models_list[0])

index = 0

for m in models_list:
    print("-" * 40)
    print(f"{index}.")
#     # print(f"id:          {m.model_id}")           # e.g. "gemma-2"
#     print(f"displayName: {m.display_name}")
#     print(f"description: {m.description}")
#     print(f"supportedMethods: {m.supported_methods}")   # ["generateContent", ...]
    print(f"base_model_id: {m.base_model_id}")
    print(f"version: {m.version}")
    print(f"display_name: {m.display_name}")
    index += 1