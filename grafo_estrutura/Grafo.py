from abc import ABC, abstractmethod


class Grafo(ABC):
    """
    Classe base para representação de grafos G = (V, A).
    """

    def __init__(self,
                 direcionado: bool = False,
                 ponderado: bool = False):
        self.vertices = set()
        self.direcionado = direcionado
        self.ponderado = ponderado

    # — vértices —


    def adicionar_vertice(self, vertice: int | list | str):
        """
        Adiciona um ou mais vértices ao grafo.

        Args:
            vertice: identificador único ou lista de identificadores.

        Raises:
            ValueError: se o vértice já existir no grafo.
        """
        if isinstance(vertice, list):
            for v in vertice:
                if v in self.vertices:
                    raise ValueError(f"Vértice '{v}' já existe no grafo.")
                self.vertices.add(v)
        else:
            if vertice in self.vertices:
                raise ValueError(f"Vértice '{vertice}' já existe no grafo.")
            self.vertices.add(vertice)

    def remover_vertice(self, vertice: int | str):
        """
        Remove um vértice e todas as suas arestas do grafo.

        Args:
            vertice: identificador do vértice a ser removido.

        Raises:
            ValueError: se o vértice não existir no grafo.
        """
        if vertice not in self.vertices:
            raise ValueError(f"Vértice '{vertice}' não existe no grafo.")
        self._remover_arestas_do_vertice(vertice)
        self.vertices.remove(vertice)

    def tem_vertice(self, vertice: int | str) -> bool:
        """Verifica se um vértice existe no grafo."""
        return vertice in self.vertices

    def obter_vertices(self) -> set:
        """Retorna o conjunto de vértices do grafo."""
        return self.vertices

    def __len__(self) -> int:
        """Retorna o número de vértices do grafo."""
        return len(self.vertices)

    def __iter__(self):
        """Permite iterar sobre os vértices do grafo."""
        return iter(self.vertices)

    def __repr__(self) -> str:
        return (f"Grafo(vertices={len(self.vertices)}, "
                f"direcionado={self.direcionado}, "
                f"ponderado={self.ponderado})")
    @staticmethod
    def criar(representacao="lista",
              direcionado=False,
              ponderado=False,
              vertices=None,    
              arestas=None):   
        from ._GrafoFactory import GrafoFactory
        return GrafoFactory.criar(
            representacao=representacao,
            direcionado=direcionado,
            ponderado=ponderado,
            vertices=vertices,
            arestas=arestas
        )
    # — arestas (dependem da representação) —

    @abstractmethod
    def _remover_arestas_do_vertice(self, vertice):
        """Remove todas as arestas associadas a um vértice."""
        pass

    @abstractmethod
    def adicionar_aresta(self, vertice1, vertice2, peso=None):
        """Adiciona uma aresta entre dois vértices."""
        pass

    @abstractmethod
    def remover_aresta(self, vertice1, vertice2):
        """Remove a aresta entre dois vértices."""
        pass

    @abstractmethod
    def tem_aresta(self, vertice1, vertice2) -> bool:
        """Verifica se existe aresta entre dois vértices."""
        pass

    @abstractmethod
    def obter_arestas(self):
        """Retorna todas as arestas do grafo."""
        pass

    @abstractmethod
    def obter_vizinhos(self, vertice) -> list:
        """Retorna os vizinhos de um vértice."""
        pass

    @abstractmethod
    def obter_grau(self, vertice) -> int:
        """Retorna o grau de um vértice."""
        pass

    @abstractmethod
    def num_arestas(self) -> int:
        """Retorna o número de arestas do grafo."""
        pass
