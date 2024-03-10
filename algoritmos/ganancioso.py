from auxiliar.Visitados import Visitados
from queue import PriorityQueue


class FilaPrioridade:
    def __init__(self):
        self.fila = PriorityQueue()

    def push(self, valor, item):
        self.fila.put((valor, item))

    def pop(self):
        if self.esta_vazio():
            return None
        else:
            (_, no) = self.fila.get()
            return no

    def esta_vazio(self):
        return self.fila.empty()


def ganancioso(problema):
    """
    Implementa o algoritmo de busca gananciosa (best-first search) para resolver um problema.

    Args:
        problema: O problema a ser resolvido.

    Returns:
        Uma tupla contendo o tamanho da lista de visitados e o nó final.
    """
    no_inicial = problema.iniciar()

    fila_prioridade = FilaPrioridade()
    fila_prioridade.push(0, no_inicial)

    visitados = Visitados()
    visitados.adicionar(no_inicial)

    while not fila_prioridade.esta_vazio():
        no = fila_prioridade.pop()
        visitados.adicionar(no)

        resultado = problema.testar_objetivo(no)
        if resultado:
            return visitados.tamanho(), no
        sucessores = problema.gerar_sucessores(no)
        for sucessor in sucessores:
            if not visitados.foi_visitado(sucessor):
                sucessor.heuristica = problema.heuristica(sucessor)
                sucessor.custo = no.custo + problema.custo(no, sucessor)
                fila_prioridade.push(sucessor.heuristica, sucessor)

    return visitados.tamanho(), None
