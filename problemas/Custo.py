import numpy as np

class Custo:
    """
    Classe para calcular o custo de uma ação
    """

    DISTANCIA_BASE = 0.75  # Fator de multiplicação da distância
    PESO_CAIXA_BASE = 0.1  # Peso base de cada unidade da caixa

    def calcular_custo(self, no, no_sucessor):
        """
        Calcula o custo de uma ação.

        Args:
            no (object): Nó atual.
            no_sucessor (object): Nó sucessor.

        Returns:
            float: Custo da ação.
        """

        estado_atual = np.where(no.estado == '#')[0]
        estado_futuro = np.where(no_sucessor.estado == '#')[0]

        if len(estado_atual) == 0 or len(estado_futuro) == 0:
            raise ValueError("Estado do braço inválido.")

        estado_atual = estado_atual[0]
        estado_futuro = estado_futuro[0]

        # Se a posição futura do braço for igual à posição atual, o custo é zero
        if estado_futuro == estado_atual:
            return 0

        # Calcula o custo baseado na distância percorrida pelo braço
        distancia = abs(estado_futuro - estado_atual)
        valor_custo = distancia * self.DISTANCIA_BASE

        # Se o braço estiver segurando uma caixa, adiciona um custo adicional baseado no peso da caixa
        if no.estado[-1] != '0':
            peso_caixa = int(no.estado[-1]) * self.PESO_CAIXA_BASE
            valor_custo += peso_caixa

        return valor_custo
