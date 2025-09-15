from TriagemOut import TriagemOut
from langchain_core.messages import SystemMessage, HumanMessage

class Triagem:
    def __init__(self, llm_triagem, prompt):
        self._chain = llm_triagem.with_structured_output(TriagemOut)
        self._prompt = prompt
        
    def execute(self, mensagem):
        saida: TriagemOut = self._chain.invoke([
            SystemMessage(content=self._prompt),
            HumanMessage(content=mensagem)
        ])
        
        return saida.model_dump()