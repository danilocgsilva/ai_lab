from AgentState import AgentState
from Triagem import Triagem
from functions import perguntar_politica_RAG, salvar_imagem_grafo
from typing import Dict
from langgraph.graph import StateGraph, START, END
from IPython.display import display, Image

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

def decidir_pos_triagem(state: AgentState) -> str:
    print("Decidindo após a triagem...")
    decisao = state["triagem"]["decisao"]
    
    opcoes = {
        "AUTO_RESOLVER": "auto",
        "PEDIR_INFO": "info",
        "ABRIR_CHAMADO": "chamado"
    }
    
    return opcoes.get(decisao, "Decisão inválida ou não reconhecida.")

def decidir_depois_auto_resolver(state: AgentState) -> str:
    print("Decidindo após o auto resolver...")
    if state.get("rag_sucesso"):
        print("RAG com sucesso. Finalizando o fluxo...")
        return "ok"
    
    state_da_pergunta = (state["pergunta"] or "").lower()
    
    if any(keyword in state_da_pergunta for keyword in KEYWORDS_ABRIR_TICKET):
        print("O RAG falhou, mas foram encontradas keywords de abertura de ticket. Abrindo...")
        return "chamado"
    
    print("RAG falhou e não foram encontradas keywords de abertura de ticket. Vou pedir mais informações...")
    
    return "info"

workflow = StateGraph(AgentState)

workflow.add_node("triagem", node_triagem)
workflow.add_node("auto_resolver", node_resolver)
workflow.add_node("pedir_info", node_pedir_info)
workflow.add_node("abrir_chamado", node_abrir_chamado)

workflow.add_edge(START, "triagem")
workflow.add_conditional_edges("triagem", decidir_pos_triagem, {
    "auto": "auto_resolver",
    "info": "pedir_info",
    "chamado": "abrir_chamado"
})
workflow.add_conditional_edges("auto_resolver", decidir_depois_auto_resolver, {
    "info": "pedir_info",
    "chamado": "abrir_chamado",
    "ok": END
})

workflow.add_edge("pedir_info", END)
workflow.add_edge("abrir_chamado", END)

grafo = workflow.compile()

graph_bytes = grafo.get_graph().draw_mermaid_png()
salvar_imagem_grafo(graph_bytes)
