from typing import TypeDict, Optional, Dict, List

class AgentState(TypeDict, total = False):
    pergunta: str
    triagem: dict
    resposta: Optional[str]
    citacoes: List[dict]
    rag_sucesso: bool
    acao_final: str
    
    