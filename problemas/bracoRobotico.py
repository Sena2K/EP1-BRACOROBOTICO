import numpy as np
import random
from no import No
from problemas.problema import Problema
from problemas.caixas import caixas


class bracoRobotico(Problema):
    def __init__(self):

        c1 = caixas(10)
        c2 = caixas(30)
        c3 = caixas(10)
        c4 = caixas(40)

        self.estado_inicial = np.array([
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        ])

        self.estado_inicial[3][3] = c1.peso
        self.estado_inicial[3][5] = c2.peso
        self.estado_inicial[3][7] = c3.peso
        self.estado_inicial[3][0] = c4.peso

    def iniciar(self):
        self.no_raiz = No(self.estado_inicial)
        return self.no_raiz

    def imprimir(self, no):
        estado = no.estado
        return ''.join([f"\r{' '.join(estado[i:i + 8])}\n" for i in range(0, 64, 8)])

        print(labirinto)

    def gerar_sucessores(self, no):
        estado = no.estado
        nos_sucessores = []

        # encontra a posição do _
        posicao = np.where(estado == "I")[0][0]

        expansoes = [self._direita, self._esquerda, self._cima, self._baixo]
        random.shuffle(expansoes)
        for expansao in expansoes:
            no_sucessor = expansao(posicao, no)
            # self.custo(no, no_sucessor)
            if no_sucessor is not None: nos_sucessores.append(no_sucessor)

        return nos_sucessores

    def custo(self, estado_atual, estado_sucessor):
        posicao_atual, pilhas_atual, peso_atual = estado_atual
        posicao_sucessor, pilhas_sucessor, peso_sucessor = estado_sucessor
        custo_movimento = 1

        # A cada 10kg, o custo aumenta em 1 energia, assim uma caixa de 20 kg, custa 2.
        # Exemplo: Mover 2 casas uma caixa de 40kg: 2*0,75 + 40/10 = 5,5 de energia

    def heuristica(self, no):
        estado = no.estado
        resultado = [
            ["A", "A", ".", "#", ".", ".", ".", "I"],
            [".", "A", "A", ".", ".", "M", "#", "."],
            ["#", ".", "A", "#", ".", "M", "#", "#"],
            [".", "#", ".", "A", "A", "A", "A", "A"],
            [".", ".", ".", ".", "A", ".", ".", "."],
            [".", "M", "#", ".", "A", "#", ".", "."],
            [".", "M", ".", ".", ".", "A", "#", "."],
            [".", ".", ".", ".", "#", ".", "A", "."]
        ]
        estado_matriz = [estado[0:8], estado[8:16], estado[16:24], estado[24:32],
                         estado[32:40], estado[40:48], estado[48:56], estado[56:64]]

        soma = 0

        for i in range(len(resultado)):
            for j in range(len(resultado[i])):
                valor = resultado[i][j]
                soma = soma + self._distancia_manhattan(valor, estado_matriz, i, j)

        return soma

    def _distancia_manhattan(self, valor, estado, i, j):
        for k in range(len(estado)):
            for h in range(len(estado[k])):
                if valor == estado[k][h]: return abs(i - k) + abs(j - h)
