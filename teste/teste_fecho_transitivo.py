import numpy as np
from grafo_estrutura.Grafo import Grafo
from algoritmos.fecho_transitivo import fecho_transitivo_produto

def rodar_teste_fecho():
    print("=" * 55)
    print("      TESTE: FECHO TRANSITIVO (PRODUTO BOOLEANO)")
    print("=" * 55)

    # Grafo em linha: A -> B -> C
    vertices = ["A", "B", "C"]
    arestas = [("A", "B"), ("B", "C")]

    grafo = Grafo.criar(
        representacao="lista",
        direcionado=True,
        ponderado=False,
        vertices=vertices,
        arestas=arestas
    )

    print("[*] Matriz original de conexões diretas:")
    for v in sorted(vertices):
        print(f"Vizinhos de {v}: {grafo.obter_vizinhos(v)}")

    # Executa algoritmo de produto
    matriz_fecho, mapa_indices = fecho_transitivo_produto(grafo)

    print("\n[✓] Matriz do Fecho Transitivo Computada:")
    print("     ", "  ".join(sorted(vertices)))
    
    ordem_vertices = sorted(vertices, key=lambda x: mapa_indices[x])
    for v in ordem_vertices:
        idx = mapa_indices[v]
        print(f" {v} | {matriz_fecho[idx]}")
        
    print("=" * 55)

if __name__ == "__main__":
    rodar_teste_fecho()