from grafo_estrutura.Grafo import Grafo
from algoritmos.componente_conexa import DFS_Componentes 

def exibir_resultados_componentes(grafo, componentes):
    """
    Formata e exibe o mapeamento de componentes em uma tabela limpa.
    """
    print("-" * 45)
    print("Vértice | Componente Conectado (ID)")
    print("=" * 45)
    
    for v in sorted(grafo.obter_vertices()):
        print(f"   {v}    |            {componentes[v]}")
        
    print("=" * 45)
    
    # Calcula o total de componentes únicos encontrados
    total_componentes = len(set(componentes.values()))
    print(f"[➔] Total de componentes identificados: {total_componentes}\n")

def rodar_testes():
    print("=" * 55)
    print("    BATERIA DE TESTES: COMPONENTES CONECTADOS (DFS)")
    print("=" * 55)

    # Configuração de um grafo propositalmente dividido:
    # Bloco Conectado: A, B, C, D
    # Bloco Isolado: E
    vertices_teste = ["A", "B", "C", "D", "E"]
    arestas_teste = [
        ("A", "B"), 
        ("B", "C"), 
        ("C", "D"), 
        ("D", "B")
    ]

    # Valida o algoritmo tanto na representação por Lista quanto por Matriz
    for rep in ["lista", "matriz"]:
        print(f"[*] Criando grafo utilizando representação: '{rep.upper()}'")
        
        try:
            grafo = Grafo.criar(
                representacao=rep,
                direcionado=False,  # Componentes conectados EXIGEM grafos não-direcionados
                ponderado=False,
                vertices=vertices_teste,
                arestas=arestas_teste
            )

            print(f"[✓] Grafo inicializado com sucesso!")
            print(f"[•] Vértices registrados: {grafo.obter_vertices()}")
            print(f"[•] Total de Arestas: {grafo.num_arestas()}")
            
            print(f"\n[➔] Executando DFS_Componentes ({rep})...")
            componentes = DFS_Componentes(grafo)
            
            # Exibe os resultados na tela
            exibir_resultados_componentes(grafo, componentes)

        except Exception as e:
            print(f"[X] Erro ao testar a representação '{rep}': {e}\n")
            print("-" * 55 + "\n")

if __name__ == "__main__":
    rodar_testes()