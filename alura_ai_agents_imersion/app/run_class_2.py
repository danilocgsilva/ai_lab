from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from functions import getArguments, perguntar_politica_RAG
from formatadores import formatar_citacoes
from Factory import Factory

args = getArguments()
docs = []

factory = Factory()

for n in Path("documents").glob("*.pdf"):
    try:
        loader = PyMuPDFLoader(str(n))
        docs.extend(loader.load())
        print(f"Carregado o arquivo com sucesso {n.name}")
    except Exception as e:
        print(f"Erro ao carregar o arquivo {n.name}: {e}")
        
print(f"Total de documentos carregados: {len(docs)}")

chunk_size = 300
chunk_overlap = 30

# chunk_size = 100
# chunk_overlap = 0

# spliter = RecursiveCharacterTextSplitter(
#     chunk_size=chunk_size,
#     chunk_overlap=chunk_overlap,
#     length_function=len,
#     is_separator_regex=False,
# )

splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
)

chunks = splitter.split_documents(docs)

chunks_number = 0
for chunk in chunks:
    print(f"Chunk: .{chunks_number}")
    print(chunk.page_content)
    print("---")
    chunks_number += 1
    
GOOGLE_API_KEY = os.environ.get('GEMINI_KEY')


prompt_rag = ChatPromptTemplate.from_messages(
    [
        ("system",
        "Você é um Assistente de Políticas Internas (RH/IT) da empresa Carraro Desenvolvimento. "
        "Responda SOMENTE com base no contexto fornecido. "
        "Se não houver base suficiente, responda apenas 'Não sei'."),

        ("human", "Pergunta: {input}\n\nContexto:\n{context}")
    ]
)

llm = ChatGoogleGenerativeAI(
    model=args.model,
    temperature=args.temperature,
    api_key=GOOGLE_API_KEY
)
llm_triagem = ChatGoogleGenerativeAI(
    model=args.model,
    temperature=args.temperature,
    api_key=GOOGLE_API_KEY
)

document_chain = create_stuff_documents_chain(
    llm=llm_triagem,
    prompt=prompt_rag
)

testes = [
    "Posso reembolsar a internet?",
    "Quero mais 5 dias de trabalho remoto. Como faço?",
    "Posso reembolsar recursos ou treinamento da Alura?",
    "Quantas capivaras tem no rio Pinheiros?",
    "Você é um agente de qual empresa?",
    "Você é você?",
]

retriever = factory.getRetriever(chunks)

for msg_teste in testes:
    resposta = perguntar_politica_RAG(msg_teste, retriever, document_chain)
    print(f"PERGUNTA: {msg_teste}")
    print(f"RESPOSTA: {resposta['answer']}")
    
    if resposta["contexto_encontrado"]:
        print("CITAÇÕES")
        for c in resposta['citacoes']:
        #     print(f" - Documento: {c['documento']}, Página: {c['pagina']}")
        #     print(f"   Trecho: {c['trecho']}")
            print(c)
        # print(resposta['citacoes'])
        print("Citações:")
        print("-" * 40)
    