import numpy as np
from no import No
from bracoRobotico.problema import Problema


class bracoRobotico(Problema):
    def __init__(self):
        self.estado_objetivo = np.array([

        ])
        self.estado_inicial = np.array([

        ])

    def iniciar(self):
        self.no_raiz = No(self.estado_inicial)
        return self.no_raiz

    def imprimir(self, no):
        estado = no.estado
        labirinto = ""

        for linha in estado:
            labirinto += " ".join(linha) + "\n"

        return labirinto
