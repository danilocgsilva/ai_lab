from langchain_google_genai import ChatGoogleGenerativeAI
from ResponseData import ResponseData
import os

def getAnswer(question: str, model: str = None) -> ResponseData:
    DEFAULT_MODEL = "models/gemma-3-4b-it"
    GOOGLE_API_KEY = os.environ.get('GEMINI_KEY')

    if not model:
        model = DEFAULT_MODEL

    llm = ChatGoogleGenerativeAI(
        model=model,
        temperature=0.5,
        api_key=GOOGLE_API_KEY
    )

    resposta = llm.invoke(question)

    return resposta
