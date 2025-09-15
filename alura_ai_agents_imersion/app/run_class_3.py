from AgentState import AgentState
from Triagem import Triagem
from functions import perguntar_politica_RAG
from typing import Dict

def node_triagem(state: AgentState, triagem: Triagem) -> AgentState:
    print("Executando o nó de triagem...")
    return {"triagem": triagem.action(state["pergunta"])}

def node_resolver(
    state: AgentState, 
    retriever, 
    document_chain
) -> AgentState:
    print("Executando o nó de auto resolver...")
    resposta_rag: Dict = perguntar_politica_RAG(
        state['pergunta'], 
        retriever, 
        document_chain
    )
    
    update: AgentState = {
        "answer": resposta_rag["answer"],
        "citacoes": resposta_rag["citacoes"],
        "rag_sucesso": resposta_rag["contexto_encontrado"],
    }
    
    if resposta_rag["contexto_encontrado"]:
        update["acao_final"] = "AUTO_RESOLVER"
    
    return update

def node_pedir_info(state: AgentState) -> AgentState:
    print("Executando o nó de pedir informação...")
    faltantes = state["triagem"].get("campos_faltantes", [])
    detalhe = ", ".join(faltantes) if faltantes else "Tema e contexto específico"
    return {
        "resposta": f"Para avançar, preciso que detalhe: {detalhe}",
        "citacoes": [],
        "acao_final": "PEDIR_INFO"
    }
    
def node_abrir_chamado(state: AgentState) -> AgentState:
    print("Executando o nó de abrir chamado...")
    triagem = state["triagem"]
    return {
        "resposta": f"Abrindo chamado com a urgencia {triagem['urgencia']}. Descrição: {state['pergunta'][:140]}",
        "citacoes": [],
        "acao_final": "ABRIR_CHAMADO"
    }
    
KEYWORDS_ABRIR_TICKET = [
    "aprovação",
    "exceção",
    "liberação",
    "abrir ticket",
    "abrir chamado",
    "acesso especial"
]

def decidir_principal(state: AgentState) -> str:
    print("Decidindo após a triagem...")
    decisao = state["triagem"]["decisao"]
    
    opcoes = {
        "AUTO_RESOLVER": "Respondendo com as informação da IA.",
        "PEDIR_INFO": "Continuando o fluxo com conversa com usuário para pedir informação.",
        "ABRIR_CHAMADO": "Acionando a abertura de chamado."
    }
    
    return opcoes.get(decisao, "Decisão inválida ou não reconhecida.")

def decidir_depois_auto_resolver(state: AgentState) -> str:
    print("Decidindo após o auto resolver...")
    if state.get("rag_sucesso"):
        print("RAG com sucesso. Finalizando o fluxo...")
        return "Finalizando o fluxo com resposta da IA."
    
    state_da_pergunta = (state["pergunta"] or "").lower()
    
    if any(keyword in state_da_pergunta for keyword in KEYWORDS_ABRIR_TICKET):
        print("O RAG falhou, mas foram encontradas keywords de abertura de ticket. Abrindo...")
        return "Decidindo abrir chamado."
    
    print("RAG falhou e não foram encontradas keywords de abertura de ticket. Vou pedir mais informações...")
    
    return "Pedir info"