from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

docs = []

for n in Path("documents").glob("*.pdf"):
    try:
        loader = PyMuPDFLoader(str(n))
        docs.extend(loader.load())
        print(f"Carregado o arquivo com sucesso {n.name}")
    except Exception as e:
        print(f"Erro ao carregar o arquivo {n.name}: {e}")
        
print(f"Total de documentos carregados: {len(docs)}")
        