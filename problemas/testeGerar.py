import random
import numpy as np

class gerarEstado:
    def __init__(self):
        self.num_linhas = 6
        estado_inicial = []
        for i in range(self.num_linhas):
            for j in range(4):
                if i == 0 and j == 3:
                    estado_inicial.append("#")  # Inserindo o braço na posição inicial
                elif j == 3:
                    estado_inicial.append("|")  # Adicionando separadores de pilha
                else:
                    estado_inicial.append("0")  # Preenchendo com caixas vazias

        # Posições aleatórias para as caixas
        posicoes_disponiveis = [(i, j) for i in range(self.num_linhas) for j in range(3)]
        random.shuffle(posicoes_disponiveis)

        # Gerando uma quantidade aleatória de caixas (de 1 a 9)
        num_caixas = 6
        for _ in range(num_caixas):
            if posicoes_disponiveis:
                posicao = posicoes_disponiveis.pop()
                peso_caixa = random.randint(1, 6) * 10  # Peso da caixa aleatório entre 1 e 10
                estado_inicial[posicao[0] * 4 + posicao[1]] = peso_caixa  # Inserindo o peso da caixa na posição

        # Adicionando uma linha extra
        estado_inicial.extend([0])

        # Convertendo o estado inicial para um array numpy
        self.estado_inicial = np.array(estado_inicial)


# Criando uma instância da classe
instancia = gerarEstado()

# Imprimindo o estado inicial
print(instancia.estado_inicial)
