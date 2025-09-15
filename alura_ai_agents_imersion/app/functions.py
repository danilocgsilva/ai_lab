import google.generativeai as genai
import os
import argparse
from typing import Dict

def format_module_info(index, m):
  """Formats module information into a single string.

  Args:
    index: The index of the module (for numbering).
    m: The module object containing the data to be formatted.

  Returns:
    A single string containing the formatted module information.
  """
  return (
      f"{index}.\n" +
      f"Name: {m.name}\n" +
      f"displayName: {m.display_name}\n" +
      f"description: {m.description}\n" +
      f"supportedMethods: {m.supported_generation_methods}\n" +
      f"version: {m.version}\n" +
      f"display_name: {m.display_name}"  # Added the duplicate line as requested
  )

def format2(index, m):
    return (
        f"{index}. displayName: {m.display_name}, description: {m.description}, "
    )

def configure_genai():
    GOOGLE_API_KEY = os.environ.get("GEMINI_KEY")

    if not GOOGLE_API_KEY:
        raise RuntimeError("Please export GEMINI_KEY before running")

    genai.configure(api_key=GOOGLE_API_KEY)

def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--model',
        '-m',
        type=str,
        required=False,
        help='The model to be used',
        default='gemini-2.5-flash'
    )
    parser.add_argument(
        '--temperature',
        '-t',
        type=float,
        required=False,
        help='Temperature to be used',
        default=0.5
    )
    parser.add_argument(
        '--question',
        '-q',
        type=str,
        required=False,
        help='Question to be done',
    )
    parser.add_argument(
        '--use-system-prompt',
        '-s',
        action='store_true',
        required=False,
        help='If should I use the system prompt',
        default=False
    )
    
    return parser.parse_args()

def perguntar_politica_RAG(pergunta: str, retriever, document_chain) -> Dict:
    docs_relacionados = retriever.invoke(pergunta)
    if not docs_relacionados:
        return {
            "answer": "Não sei.",
            "citacoes": [],
            "contexto_encontrado": False
        }
    answer = document_chain.invoke(
        {
            "input": pergunta,
            # "context": formatar_citacoes(docs_relacionados, pergunta)
            "context": docs_relacionados
        }
    )
    txt = (answer or "").strip()
    if txt.rstrip(".!?") == "Não sei":
        return {
            "answer": "Não sei.",
            "citacoes": [],
            "contexto_encontrado": False
        }
    return {
        "answer": txt,
        # "citacoes": formatar_citacoes(docs_relacionados, pergunta),
        "citacoes": docs_relacionados,
        "contexto_encontrado": True
    }
