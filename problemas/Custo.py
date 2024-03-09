import numpy as np


class Custo:
    def __init__(self):
        pass

    def calcular_custo(self, no, no_sucessor):
        # Calcula o custo de uma ação
        valor_custo = 1
        estado_atual = np.where(no.estado == "#")[0][0]  # Posição atual do braço
        estado_futuro = np.where(no_sucessor.estado == "#")[0][0]  # Posição futura do braço

        # Se a posição futura do braço for igual à posição atual, o custo é zero
        if estado_futuro == estado_atual:
            return 0

        # Calcula o custo baseado na distância percorrida pelo braço
        distancia = abs(estado_futuro - estado_atual)
        valor_custo += distancia * 0.75

        # Se o braço estiver segurando uma caixa, adiciona um custo adicional baseado no peso da caixa
        if no.estado[-1] != "0":
            peso_caixa = int(no.estado[-1]) / 10
            valor_custo += peso_caixa

        return valor_custo
