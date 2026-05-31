from grafo_estrutura.Grafo import Grafo

def DFS_Componentes(grafo: Grafo):
    """
    Executa a Busca em Profundidade (DFS) modificada para encontrar
    os componentes conectados de um grafo.
    Retorna um dicionário mapeando {vértice: ID_do_componente}
    """
    pai = {}
    descoberta = {}
    finalizacao = {}
    componentes = {}  
    
    cor = {v: "BRANCO" for v in grafo.obter_vertices()}
    tempo = {"valor": 0}
    id_atual = 0      

    def DFS_visit(u, id_comp):  
        cor[u] = "CINZA"
        componentes[u] = id_comp  
        
        tempo["valor"] += 1
        descoberta[u] = tempo["valor"]

        # Explora as arestas adjacentes
        for v in grafo.obter_vizinhos(u):
            if cor[v] == "BRANCO":
                pai[v] = u
                DFS_visit(v, id_comp) 

        cor[u] = "PRETO"
        
        tempo["valor"] += 1
        finalizacao[u] = tempo["valor"]

    for u in sorted(grafo.obter_vertices()):
        if cor[u] == "BRANCO":
            id_atual += 1  # 6. ALTERAÇÃO: Se achou um vértice BRANCO no laço principal, novo componente detectado!
            pai[u] = None
            DFS_visit(u, id_atual)

    # Retorna o dicionário de componentes exigido pelo seu trabalho
    return componentes