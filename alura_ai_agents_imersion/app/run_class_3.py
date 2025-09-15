from AgentState import AgentState
from Triagem import Triagem

def node_triagem(state: AgentState, triagem: Triagem) -> AgentState:
    print("Executando o nó de triagem...")
    return {"triagem": triagem.action(state["mensagem"])}
