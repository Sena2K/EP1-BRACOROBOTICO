import numpy as np
import random
from no import No
from problemas.problema import Problema
from problemas.caixas import caixas


class bracoRobotico:
    def __init__(self, boxes=4, max_positions=9):
        self.max_boxes_stacked = 3

        # Definindo as posições iniciais das caixas
        box_position = [1, 4, 6, 8]

        # Convertendo para arrays numpy
        self.positions = np.array(box_position)
        self.boxes = np.array(boxes)

        # Concatenando as posições das caixas com a nova caixa
        self.estado_inicial = np.concatenate([
            self.positions,
            np.array([max_positions // 3, -1])  # Nova caixa na metade do tabuleiro com altura -1
        ])

    def iniciar(self):
        self.no_raiz = No(self.estado_inicial)
        while self.testeMaior():
            self.estado_inicial = np.concatenate([])
            break
        return self.no_raiz

    def testeMaior(self):
        # Verifica se o número máximo de caixas empilhadas é diferente de 3
        if self.max_boxes_stacked != 3:
            return True
        else:
            return False


    def imprimir(self, no):
        estado = no.estado
        return ''.join([f"\r{' '.join(estado[i:i + 8])}\n" for i in range(0, 64, 8)])
        #ainda não faco ideia


    def gerar_sucessores(self, no):
        nos_sucessores = []
        estado = no.estado
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
