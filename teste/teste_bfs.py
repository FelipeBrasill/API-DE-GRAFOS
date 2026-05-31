from grafo_estrutura.Grafo import Grafo
from algoritmos.bfs import BFS 

def exibir_resultados_bfs(grafo, pai, descoberta):
    """
    Formata e exibe os resultados do BFS em uma tabela limpa.
    """
    print("-" * 60)
    print("Vértice | Distância da Fonte (d) | Pai (Antecessor)")
    print("=" * 60)
    
    for v in sorted(grafo.obter_vertices()):
        dist = descoberta.get(v)
        dist_str = str(dist) if dist != float("inf") else "∞ (Inalcançável)"
        
        p = pai.get(v)
        pai_str = str(p) if p is not None else "None (Fonte)"
        
        print(f"   {v}    |           {dist_str:2}           | {pai_str}")
        
    print("=" * 60 + "\n")

def rodar_testes():
    print("=" * 60)
    print("       BATERIA DE TESTES: BUSCA EM LARGURA (BFS)")
    print("=" * 60)

    # Definição do grafo de teste (Grafo direcionado em camadas)
    # Fonte: A
    # Camada 1: B, C (Distância 1)
    # Camada 2: D    (Distância 2)
    # Camada 3: E    (Distância 3)
    vertices_teste = ["A", "B", "C", "D", "E"]
    arestas_teste = [
        ("A", "B"), 
        ("A", "C"), 
        ("B", "D"), 
        ("C", "D"), 
        ("D", "E")
    ]
    
    fonte = "A"

    # Testando as duas representações
    for rep in ["lista", "matriz"]:
        print(f"[*] Criando grafo utilizando representação: '{rep.upper()}'")
        
        try:
            grafo = Grafo.criar(
                representacao=rep,
                direcionado=True,
                ponderado=False,
                vertices=vertices_teste,
                arestas=arestas_teste
            )

            print(f"[✓] Grafo inicializado com sucesso!")
            print(f"[•] Vértices registrados: {grafo.obter_vertices()}")
            
            print(f"\n[➔] Executando BFS a partir da fonte '{fonte}' ({rep})...")
            pai, descoberta = BFS(grafo, inicio=fonte)
            
            # Exibe a tabela de distâncias por camadas e árvore de caminhos
            exibir_resultados_bfs(grafo, pai, descoberta)

        except Exception as e:
            print(f"[X] Erro ao testar a representação '{rep}': {e}\n")
            print("-" * 60 + "\n")

if __name__ == "__main__":
    rodar_testes()