from typing import overload
from .Grafo import Grafo


class GrafoLista(Grafo):
    """
    Implementação de grafo usando lista de adjacência.
    """

    def __init__(
        self,
        vertices: list | None = None,     # <-- Parâmetro opcional adicionado
        arestas: list | None = None,      # <-- Parâmetro opcional adicionado
        direcionado: bool = False,
        ponderado: bool = False
    ):
        super().__init__(direcionado=direcionado, ponderado=ponderado)
        
        self.adjacencia: dict = {}

        if vertices is not None:
            self.adicionar_vertice(vertices)

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

        if vertice in self.vertices:
            raise ValueError(f"Vértice '{vertice}' já existe no grafo.")

        self.vertices.add(vertice)
        self.adjacencia[vertice] = {}

    def remover_vertice(self, vertice: int | str):
        """
        Remove um vértice e todas as suas arestas do grafo.
        """
        if vertice not in self.vertices:
            raise ValueError(f"Vértice '{vertice}' não existe no grafo.")

        self._remover_arestas_do_vertice(vertice)
        del self.adjacencia[vertice]
        self.vertices.remove(vertice)

    def _remover_arestas_do_vertice(self, vertice):
        """
        Remove todas as arestas incidentes em um vértice.
        """
        if vertice in self.adjacencia:
            del self.adjacencia[vertice]

        for v in list(self.adjacencia.keys()):
            if vertice in self.adjacencia[v]:
                del self.adjacencia[v][vertice]

    # — arestas —

    @overload
    def adicionar_aresta(
        self,
        vertice1: int | str,
        vertice2: int | str,
        peso: float | None = None
    ) -> None: ...

    @overload
    def adicionar_aresta(
        self,
        arestas: list[tuple[int | str, int | str] | tuple[int | str, int | str, float | None]]
    ) -> None: ...

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
                    raise ValueError(
                        "Cada aresta deve ter 2 ou 3 elementos: "
                        "(v1, v2) ou (v1, v2, peso)."
                    )
                self.adicionar_aresta(v1, v2, p)
            return

        if vertice2 is None:
            raise ValueError("É necessário informar o vértice de destino.")

        if vertice1 not in self.vertices or vertice2 not in self.vertices:
            raise ValueError("Ambos os vértices devem existir no grafo.")

        if vertice1 not in self.adjacencia:
            self.adjacencia[vertice1] = {}
        if vertice2 not in self.adjacencia:
            self.adjacencia[vertice2] = {}

        if vertice2 in self.adjacencia[vertice1]:
            raise ValueError(f"Aresta '{vertice1} → {vertice2}' já existe no grafo.")

        self.adjacencia[vertice1][vertice2] = peso

        if not self.direcionado and vertice1 != vertice2:
            self.adjacencia[vertice2][vertice1] = peso

    @overload
    def remover_aresta(self, vertice1: int | str, vertice2: int | str) -> None: ...

    @overload
    def remover_aresta(
        self,
        arestas: list[tuple[int | str, int | str]]
    ) -> None: ...

    def remover_aresta(self, vertice1, vertice2=None):
        """
        Remove uma ou mais arestas do grafo.
        """
        if isinstance(vertice1, list):
            for aresta in vertice1:
                if len(aresta) != 2:
                    raise ValueError(
                        "Cada aresta deve ter 2 elementos: (v1, v2)."
                    )
                v1, v2 = aresta
                self.remover_aresta(v1, v2)
            return

        if vertice2 is None:
            raise ValueError("É necessário informar o vértice de destino.")

        if not self.tem_aresta(vertice1, vertice2):
            raise ValueError(f"Aresta '{vertice1} → {vertice2}' não existe no grafo.")

        del self.adjacencia[vertice1][vertice2]

        if not self.direcionado and vertice1 != vertice2:
            del self.adjacencia[vertice2][vertice1]

    def tem_aresta(self, vertice1: int | str, vertice2: int | str) -> bool:
        """
        Verifica se existe aresta entre dois vértices.
        """
        return vertice1 in self.adjacencia and vertice2 in self.adjacencia[vertice1]

    def obter_arestas(self) -> list[tuple[int | str, int | str, float | None]]:
        """
        Retorna todas as arestas do grafo como lista de tuplas (v1, v2, peso).
        """
        arestas = []
        visitados = set()

        for v1, vizinhos in self.adjacencia.items():
            for v2, peso in vizinhos.items():
                if self.direcionado:
                    chave = (v1, v2)
                else:
                    chave = frozenset((v1, v2))

                if chave not in visitados:
                    arestas.append((v1, v2, peso))
                    visitados.add(chave)

        return arestas

    def obter_vizinhos(self, vertice: int | str) -> list[int | str]:
        """
        Retorna os vizinhos de um vértice.
        """
        if vertice not in self.vertices:
            raise ValueError(f"Vértice '{vertice}' não existe no grafo.")
        return list(self.adjacencia.get(vertice, {}).keys())

    def obter_grau(self, vertice: int | str) -> int:
        """
        Retorna o grau de um vértice.
        Em grafos direcionados, retorna o grau de saída.
        """
        if vertice not in self.vertices:
            raise ValueError(f"Vértice '{vertice}' não existe no grafo.")
        return len(self.adjacencia.get(vertice, {}))

    def num_arestas(self) -> int:
        """
        Retorna o número de arestas do grafo.
        """
        return len(self.obter_arestas())

    def __repr__(self) -> str:
        return (
            f"GrafoLista(vertices={len(self.vertices)}, "
            f"arestas={self.num_arestas()}, "
            f"direcionado={self.direcionado}, "
            f"ponderado={self.ponderado})"
        )