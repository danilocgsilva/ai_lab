from typing import TypeDict, Optional, Dict, List

class AgentState(TypeDict, total = False):
    mensagem: str
    triagem: dict
    resposta: Optional[str]
    citacoes: List[dict]
    rag_sucesso: bool
    acao_final: str
    
    