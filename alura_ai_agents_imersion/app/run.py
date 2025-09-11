# from google.colab import userdata
from langchain_google_genai import ChatGoogleGenerativeAI
import os

GOOGLE_API_KEY = os.environ.get('GEMINI_KEY')

# modelo = "google/gemma-3-12b"
# modelo = "google/gemma-3-4b"
# modelo = "google/gemma-3-12b-it"
# modelo = "Gemma 3 4B"
# modelo = "Gemma 3 4B"
modelo = "models/gemma-3-4b-it"

llm = ChatGoogleGenerativeAI(
    model=modelo,
    temperature=0.5,
    api_key=GOOGLE_API_KEY
)

resposta_teste = llm.invoke("Qual a capital do Brasil?")

print(resposta_teste)

print("Hello world!")
