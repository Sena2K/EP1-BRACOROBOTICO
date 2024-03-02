def no_caminho(no):
    caminho = [no.estado]
    while no.no_pai is not None:
        caminho.append(no.estado)
        no = no.no_pai
    caminho.reverse()
    return caminho


def vertice_caminho(no):
    caminho = []
    while no.no_pai is not None:
        if no.aresta is not None: caminho.append(no.aresta)
        no = no.no_pai
    caminho.reverse()
    return caminho


class Visitados:
    def __init__(self):
        self.visitados = set({})

    def adicionar(self, no):
        self.visitados.add(tuple(no.estado))

    def foi_visitado(self, no):
        return tuple(no.estado) in self.visitados

    def tamanho(self):
        return len(self.visitados)