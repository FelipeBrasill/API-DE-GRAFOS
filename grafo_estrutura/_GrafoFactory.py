from .GrafoMatriz import GrafoMatriz
from .GrafoLIsta import GrafoLista

class GrafoFactory:
    @staticmethod
    def criar(representacao="lista", vertices=None, arestas=None, direcionado=False, ponderado=False):
        if representacao == "lista":
            return GrafoLista(vertices, arestas, direcionado, ponderado)
        if representacao == "matriz":
            return GrafoMatriz(vertices, arestas, direcionado, ponderado)
        raise ValueError("Representação inválida")