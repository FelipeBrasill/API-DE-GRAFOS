import numpy as np
from grafo_estrutura.Grafo import Grafo

def fecho_transitivo_produto(grafo: Grafo):
    """
    Calcula o fecho transitivo de um grafo usando o produto booleano de matrizes.
    Retorna a matriz final do fecho transitivo e o dicionário de mapeamento de índices.
    """
    # 1. Mapeia os vértices para posições fixas na matriz (Garante sempre estar na mesma ordem)
    vertices = sorted(list(grafo.obter_vertices()))
    n = len(vertices)
    
    if n == 0:
        return np.zeros((0, 0), dtype=int), {}
        
    indice = {v: i for i, v in enumerate(vertices)}
    
    # 2. Constrói a Matriz de Adjacência Inicial (A^1) como Booleana
    A_inicial = np.zeros((n, n), dtype=bool)
    for v in vertices:
        for vizinho in grafo.obter_vizinhos(v):
            A_inicial[indice[v], indice[vizinho]] = True

    # 3. Inicializa o Fecho Transitivo acumulado (R) com a própria matriz inicial
    Fecho = A_inicial.copy()
    
    # Matriz que vai sendo multiplicada a cada iteração (A^1, A^2, A^3...)
    A_potencia = A_inicial.copy()

    # 4. Multiplica as matrizes até (n-1) vezes
    # Para caminhos de até n vértices, o maior caminho sem ciclos tem n-1 arestas
    for _ in range(1, n):
        # Produto Booleano de Matrizes: (A_potencia @ A_inicial) usando lógica True/False
        # Em termos booleanos: produto_ponto(linha, coluna) usando AND e depois reduzindo com OR
        A_potencia = np.dot(A_potencia, A_inicial) > 0
        
        # Adiciona os novos caminhos encontrados ao nosso Fecho Acumulado (Operação OR)
        Fecho = Fecho | A_potencia

    # Retorna a matriz convertida para 0 e 1 (inteiros) para ficar bonita na tela
    return Fecho.astype(int), indice