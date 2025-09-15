from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

class Factory:
    @staticmethod
    def getRetriever(chunks):
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=os.environ.get('GEMINI_KEY')
        )
        vectorstore = FAISS.from_documents(chunks, embeddings)
        
        retriever = vectorstore.as_retriever(
            search_type="similarity_score_threshold", 
            search_kwargs={
                "score_threshold": 0.3,
                "k": 4
            }
        )
        
        return retriever
