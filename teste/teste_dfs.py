from grafo_estrutura.Grafo import Grafo
from algoritmos.dfs import DFS 

def exibir_resultados_dfs(grafo, descoberta, finalizacao):
    """
    Formata e exibe os resultados do DFS em uma tabela limpa.
    """
    print("-" * 55)
    print("Vértice | Tempo Descoberta (d) | Tempo Finalização (f)")
    print("=" * 55)
    
    for v in sorted(grafo.obter_vertices()):
        print(f"   {v}    |          {descoberta[v]:2}          |          {finalizacao[v]:2}")
        
    print("=" * 55 + "\n")

def rodar_testes():
    print("=" * 55)
    print("       BATERIA DE TESTES: BUSCA EM PROFUNDIDADE (DFS)")
    print("=" * 55)

    # Definição dos dados do grafo de teste (Grafo direcionado com ciclos)
    vertices_teste = ["A", "B", "C", "D", "E"]
    arestas_teste = [
        ("A", "B"), 
        ("B", "C"), 
        ("C", "D"), 
        ("D", "B"), # Ciclo entre B, C, D
        ("A", "E")
    ]

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

            print(f"Grafo inicializado com sucesso!")
            print(f"Vértices registrados: {grafo.obter_vertices()}")
            print(f"Total de Arestas: {grafo.num_arestas()}")
            
            print(f"\nExecutando DFS no Grafo ({rep})...")
            
            # Captura o retorno do DFS ignorando o primeiro valor (pai) com o caractere '_'
            _, descoberta, finalizacao = DFS(grafo)
            
            # Exibe a tabela de tempos d/f 
            exibir_resultados_dfs(grafo, descoberta, finalizacao)

        except Exception as e:
            print(f"[X] Erro ao testar a representação '{rep}': {e}\n")
            print("-" * 55 + "\n")

if __name__ == "__main__":
    rodar_testes()