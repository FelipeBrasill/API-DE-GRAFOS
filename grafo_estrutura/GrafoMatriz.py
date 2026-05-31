from typing import overload
import numpy as np
from .Grafo import Grafo


class GrafoMatriz(Grafo):
    """
    Implementação de grafo usando matriz de adjacência dinâmica.
    """

    def __init__(
        self, 
        vertices: list | None = None,    
        arestas: list | None = None,      
        direcionado: bool = False, 
        ponderado: bool = False
    ):
        # 1. Inicializa o estado básico na classe mãe
        super().__init__(direcionado=direcionado, ponderado=ponderado)
        
        # 2. Instancia as estruturas internas base
        self.adjacencia: np.ndarray = np.zeros((0, 0), dtype=float)
        self._ordem_vertices: list[int | str] = []
        self._indices: dict[int | str, int] = {}

        # 3. Se houver vértices iniciais vindos da factory, adiciona todos agora
        if vertices is not None:
            self.adicionar_vertice(vertices)

        # 4. Se houver arestas iniciais vindas da factory, adiciona todas agora
        if arestas is not None:
            self.adicionar_aresta(arestas)

    # — vértices —

    def adicionar_vertice(self, vertice: int | str | list):
        """
        Adiciona um ou mais vértices ao grafo.
        """
        if isinstance(vertice, list):
            for v in vertice:
                self.adicionar_vertice(v)
            return

        if hasattr(self, '_registrar_vertice'):
            self._registrar_vertice(vertice)
        else:
            if vertice in self.vertices:
                raise ValueError(f"Vértice '{vertice}' já existe no grafo.")
            self.vertices.add(vertice)
        
        self._ordem_vertices.append(vertice)
        self._indices[vertice] = len(self._ordem_vertices) - 1

        n = len(self._ordem_vertices)
        nova = np.zeros((n, n), dtype=float)
        if n > 1:
            nova[: n - 1, : n - 1] = self.adjacencia
        self.adjacencia = nova

    def remover_vertice(self, vertice: int | str):
        """
        Remove um vértice e todas as suas arestas do grafo.
        """
        if not self.tem_vertice(vertice):
            raise ValueError(f"Vértice '{vertice}' não existe no grafo.")

        self._remover_arestas_do_vertice(vertice)
        self.vertices.remove(vertice)

    def _remover_arestas_do_vertice(self, vertice):
        """
        Remove o vértice da matriz e atualiza os índices.
        """
        idx = self._obter_indice(vertice)

        self.adjacencia = np.delete(self.adjacencia, idx, axis=0)
        self.adjacencia = np.delete(self.adjacencia, idx, axis=1)

        del self._ordem_vertices[idx]
        del self._indices[vertice]

        for i in range(idx, len(self._ordem_vertices)):
            self._indices[self._ordem_vertices[i]] = i

    def _obter_indice(self, vertice: int | str) -> int:
        if vertice not in self._indices:
            raise ValueError(f"Vértice '{vertice}' não existe no grafo.")
        return self._indices[vertice]

    def _obter_vertice(self, indice: int) -> int | str:
        return self._ordem_vertices[indice]

    def _valor_aresta(self, peso):
        return float(peso) if self.ponderado else 1.0

    # — arestas —

    @overload
    def adicionar_aresta(self, vertice1: int | str, vertice2: int | str, peso: float | None = None) -> None: ...

    @overload
    def adicionar_aresta(self, arestas: list[tuple[int | str, int | str] | tuple[int | str, int | str, float | None]]) -> None: ...

    def adicionar_aresta(self, vertice1, vertice2=None, peso=None):
        """
        Adiciona uma ou mais arestas ao grafo.
        """
        if isinstance(vertice1, list):
            for aresta in vertice1:
                if len(aresta) == 3:
                    v1, v2, p = aresta
                elif len(aresta) == 2:
                    v1, v2 = aresta
                    p = None
                else:
                    raise ValueError("Cada aresta deve ter 2 ou 3 elementos.")
                self.adicionar_aresta(v1, v2, p)
            return

        if vertice2 is None:
            raise ValueError("É necessário informar o vértice de destino.")

        if not self.tem_vertice(vertice1) or not self.tem_vertice(vertice2):
            raise ValueError("Ambos os vértices devem existir no grafo.")

        idx1 = self._obter_indice(vertice1)
        idx2 = self._obter_indice(vertice2)

        if self.adjacencia[idx1][idx2] != 0:
            raise ValueError(f"Aresta '{vertice1} → {vertice2}' já existe no grafo.")

        valor = self._valor_aresta(peso)
        self.adjacencia[idx1][idx2] = valor

        if not self.direcionado:
            self.adjacencia[idx2][idx1] = valor

    @overload
    def remover_aresta(self, vertice1: int | str, vertice2: int | str) -> None: ...

    @overload
    def remover_aresta(self, arestas: list[tuple[int | str, int | str]]) -> None: ...

    def remover_aresta(self, vertice1, vertice2=None):
        """
        Remove uma ou mais arestas do grafo.
        """
        if isinstance(vertice1, list):
            for aresta in vertice1:
                if len(aresta) != 2:
                    raise ValueError("Cada aresta deve ter 2 elementos: (v1, v2).")
                v1, v2 = aresta
                self.remover_aresta(v1, v2)
            return

        if vertice2 is None:
            raise ValueError("É necessário informar o vértice de destino.")

        if not self.tem_aresta(vertice1, vertice2):
            raise ValueError(f"Aresta '{vertice1} → {vertice2}' não existe no grafo.")

        idx1 = self._obter_indice(vertice1)
        idx2 = self._obter_indice(vertice2)

        self.adjacencia[idx1][idx2] = 0.0

        if not self.direcionado:
            self.adjacencia[idx2][idx1] = 0.0

    def tem_aresta(self, vertice1: int | str, vertice2: int | str) -> bool:
        if not self.tem_vertice(vertice1) or not self.tem_vertice(vertice2):
            return False
        idx1 = self._obter_indice(vertice1)
        idx2 = self._obter_indice(vertice2)
        return self.adjacencia[idx1][idx2] != 0

    def obter_arestas(self) -> list[tuple[int | str, int | str, float | None]]:
        """
        Retorna todas as arestas de forma otimizada usando máscaras do NumPy.
        """
        # Extrai de uma vez só as coordenadas (i, j) onde o valor não é zero
        if self.direcionado:
            linhas, colunas = np.nonzero(self.adjacencia)
        else:
            linhas, colunas = np.nonzero(np.triu(self.adjacencia))

        return [
            (self._obter_vertice(i), self._obter_vertice(j), self.adjacencia[i][j])
            for i, j in zip(linhas, colunas)
        ]

    def obter_vizinhos(self, vertice: int | str) -> list[int | str]:
        """
        Retorna os vizinhos usando localização direta de índices não nulos.
        """
        if not self.tem_vertice(vertice):
            raise ValueError(f"Vértice '{vertice}' não existe no grafo.")

        idx = self._obter_indice(vertice)
        # Encontra instantaneamente os índices da coluna que possuem conexões
        indices_vizinhos = np.flatnonzero(self.adjacencia[idx])
        return [self._obter_vertice(j) for j in indices_vizinhos]

    def obter_grau(self, vertice: int | str) -> int:
        """
        Retorna o grau de forma vetorizada com np.count_nonzero.
        """
        if not self.tem_vertice(vertice):
            raise ValueError(f"Vértice '{vertice}' não existe no grafo.")

        idx = self._obter_indice(vertice)
        # Conta a quantidade de elementos diferentes de zero na linha desejada
        return int(np.count_nonzero(self.adjacencia[idx]))

    def num_arestas(self) -> int:
        if self.direcionado:
            return int(np.count_nonzero(self.adjacencia))
        return int(np.count_nonzero(np.triu(self.adjacencia)))