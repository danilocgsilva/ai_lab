from langchain_google_genai import ChatGoogleGenerativeAI
import os
import sys
from pydantic import BaseModel, Field
from typing import Literal, List, Dict
from functions import getArguments
from TriagemOut import TriagemOut
from langchain_core.messages import SystemMessage, HumanMessage

args = getArguments()

question = args.question

temperature = args.temperature

GOOGLE_API_KEY = os.environ.get('GEMINI_KEY')

TRIAGEM_PROMPT = (
    "Você é um triador de Service Desk para políticas internas da empresa Carraro Desenvolvimento. "
    "Dada a mensagem do usuário, retorne SOMENTE um JSON com:\n"
    "{\n"
    '  "decisao": "AUTO_RESOLVER" | "PEDIR_INFO" | "ABRIR_CHAMADO",\n'
    '  "urgencia": "BAIXA" | "MEDIA" | "ALTA",\n'
    '  "campos_faltantes": ["..."]\n'
    "}\n"
    "Regras:\n"
    '- **AUTO_RESOLVER**: Perguntas claras sobre regras ou procedimentos descritos nas políticas (Ex: "Posso reembolsar a internet do meu home office?", "Como funciona a política de alimentação em viagens?").\n'
    '- **PEDIR_INFO**: Mensagens vagas ou que faltam informações para identificar o tema ou contexto (Ex: "Preciso de ajuda com uma política", "Tenho uma dúvida geral").\n'
    '- **ABRIR_CHAMADO**: Pedidos de exceção, liberação, aprovação ou acesso especial, ou quando o usuário explicitamente pede para abrir um chamado (Ex: "Quero exceção para trabalhar 5 dias remoto.", "Solicito liberação para anexos externos.", "Por favor, abra um chamado para o RH.").'
    "Analise a mensagem e decida a ação mais apropriada."
)

modelo = args.model
llm = ChatGoogleGenerativeAI(
    model=modelo,
    temperature=temperature,
    api_key=GOOGLE_API_KEY
)
llm_triagem = ChatGoogleGenerativeAI(
    model=modelo,
    temperature=temperature,
    api_key=GOOGLE_API_KEY
)

triagem_chain = llm_triagem.with_structured_output(TriagemOut)

def triagem(mensagem: str) -> Dict:
    saida: TriagemOut = triagem_chain.invoke([
        SystemMessage(content=TRIAGEM_PROMPT),
        HumanMessage(content=mensagem)
    ])
    
    return saida.model_dump()

testes = [
    "Posso reembolsar a internet?",
    "Quero mais 5 dias de trabalho remoto. Como faço?",
    "Posso reembolsar recursos ou treinamento da Alura?",
    "Quantas capivaras tem no rio Pinheiros?"
]

for mensagem_teste in testes:
    print(f"Pergunta: {mensagem_teste}\n -> Resposta: {triagem(mensagem_teste)}\n{'-'*50}")

# resposta_teste = llm.invoke(question)
# print(resposta_teste)
# print("Hello world!")


