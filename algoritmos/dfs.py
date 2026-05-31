from grafo_estrutura.Grafo import Grafo

def DFS(grafo: Grafo):
    """
    Executa a Busca em Profundidade (DFS) usando funções puras.
    Retorna (pai, descoberta, finalizacao)
    """
    pai = {}
    descoberta = {}
    finalizacao = {}
    cor = {v: "BRANCO" for v in grafo.obter_vertices()}
    tempo = {"valor": 0}

    def DFS_visit(u):
        cor[u] = "CINZA"
        
        tempo["valor"] += 1
        descoberta[u] = tempo["valor"]

        # Explora as arestas adjacentes
        for v in grafo.obter_vizinhos(u):
            if cor[v] == "BRANCO":
                pai[v] = u
                DFS_visit(v) # Chamada recursiva para o próximo vértice

        cor[u] = "PRETO"
        
        tempo["valor"] += 1
        finalizacao[u] = tempo["valor"]

    for u in grafo.obter_vertices():
        if cor[u] == "BRANCO":
            pai[u] = None
            DFS_visit(u)

    return pai, descoberta, finalizacao