from collections import deque
from grafo_estrutura.Grafo import Grafo

def BFS(grafo: Grafo, inicio: int | str):
    """
    Executa a Busca em Largura (BFS) no grafo a partir de um vértice fonte.
    Retorna os mapeamentos de antecessores (pai) e distâncias (descoberta).
    """
    # Verifica se a fonte realmente existe no grafo para evitar erros logo de cara
    if inicio not in grafo.obter_vertices():
        raise ValueError(f"A fonte '{inicio}' não pertence ao grafo.")

    cor = {}
    descoberta = {}
    pai = {}


    for u in grafo.obter_vertices():
        cor[u] = "BRANCO"
        descoberta[u] = float("inf")  # d[u] = ∞
        pai[u] = None                 # π[u] = NULO


    cor[inicio] = "CINZA"
    descoberta[inicio] = 0        # d[s] = 0
    pai[inicio] = None            # π[s] = NULO

    fila = deque([inicio])


    while fila:                      # enquanto (Q ≠ vazio)
        u = fila.popleft()           # u = DESENFILEIRAR(Q)

        for v in grafo.obter_vizinhos(u):
            if cor[v] == "BRANCO":   
                cor[v] = "CINZA"    
                descoberta[v] = descoberta[u] + 1  # d[v] = d[u] + 1
                pai[v] = u          
                fila.append(v)       # ENFILEIRAR(Q, v)

        # Após visitar todos os vizinhos de u, ele está totalmente explorado
        cor[u] = "PRETO"             

    return pai, descoberta