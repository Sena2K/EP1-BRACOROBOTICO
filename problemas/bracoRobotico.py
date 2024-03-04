import random
import numpy as np
from no import No
from problemas.problema import Problema


class Braco(Problema):
    def __init__(self):

        self.estado_objetivo = np.array(["30", "20", "10", "R",
                                         ".", ".", ".", "|",
                                         ".", ".", ".", "|",
                                         "30", ".", ".", "|",
                                         ".", ".", ".", "|",
                                         ".", ".", ".", "|",
                                         "."])
        self.estado_inicial = np.array([".", ".", ".", "|",
                                        "30", ".", ".", "|",
                                        "20", ".", ".", "|",
                                        "10", ".", ".", "R",
                                        "30", ".", ".", "|",
                                        ".", ".", ".", "|",
                                        "."])

    def iniciar(self):
        self.no_raiz = No(self.estado_inicial)
        return self.no_raiz

    # Função auxiliar para imprimir
    def imprimir(self, no):
        estado = no.estado
        maquina = ""

        for i in range(6):
            for j in range(4):
                index = i * 4 + j
                maquina += estado[index] + " "
            maquina += "\n"

        maquina += estado[-1]
        return maquina


    def testar_objetivo(self, no):
        return np.array_equal(no.estado, self.estado_objetivo)

    def calcular_custo_energia(self, acao, posicao, no):
        custo = 0
        if acao == "⬅️" or acao == "➡️":
            distancia = abs(posicao - np.where(no.estado == "R")[0][0])  # Calcula a distância percorrida
            if distancia == 1:
                custo += 1  # Movimento de uma casa custa 1 de energia
            elif distancia > 2:
                custo += int(distancia * 0.75)  # Movimento de mais de 2 casas custa 75% do movimento
                if no.estado[posicao] != ".":  # Verifica se há uma caixa na posição atual
                    peso_caixa = int(no.estado[posicao])  # Peso da caixa na posição atual
                    custo += int(peso_caixa / 10)  # Cada 10kg aumenta o custo em 1 energia
        elif acao == "Segurou":
            if no.estado[posicao] != ".":  # Verifica se há uma caixa na posição atual
                peso_caixa = int(no.estado[posicao])  # Peso da caixa na posição atual
                custo += int(peso_caixa / 10)  # Cada 10kg aumenta o custo em 1 energia
        return custo

    def gerar_sucessores(self, no):
        estado = no.estado
        nos_sucessores = []

        # encontra a posição do R (Braco)
        posicao = np.where(estado == "R")[0][0]

        expansoes = [self._direita, self._esquerda, self._agarrar, self._soltar]
        random.shuffle(expansoes)
        for expansao in expansoes:
            no_sucessor = expansao(posicao, no)
            if no_sucessor is not None: nos_sucessores.append(no_sucessor)

        return nos_sucessores


    def _esquerda(self, posicao, no):
        # movimento para esquerda fazendo swap apenas na ultima coluna
        if posicao not in [0, 1, 2] and no.estado[posicao - 4] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao - 4]
            sucessor[posicao - 4] = "R"
            return No(sucessor, no, "⬅️")
        else:
            None

    def _direita(self, posicao, no):
        # movimento para direita fazendo swap apenas na ultima coluna
        if posicao not in [21, 22, 23, 24] and no.estado[posicao + 4] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao + 4]
            sucessor[posicao + 4] = "R"
            return No(sucessor, no, "➡️")
        else:
            None

    # funcao de agarrar feia q funciona
    # ta tudo feio e com certeza tem um jeito melhor de fazer isso
    # o "." representa um espaco vazio
    def _agarrar(self, posicao, no):
        # Verifica se há caixas para pegar
        if no.estado[posicao - 1] != ".":
            # Pega a caixa com base no peso
            caixa_superior = None
            caixa_inferior = no.estado[posicao - 1]

            # Verifica se há uma caixa inferior na pilha
            if no.estado[posicao - 2] != ".":
                caixa_superior = no.estado[posicao - 2]

            # Verifica se há uma caixa no meio da pilha
            if no.estado[posicao - 3] != ".":
                caixa_do_meio = no.estado[posicao - 3]

            # Compara os pesos das caixas para determinar qual pegar
            if caixa_superior is not None and caixa_superior > caixa_inferior:
                caixa_superior, caixa_inferior = caixa_inferior, caixa_superior
            if caixa_do_meio is not None and caixa_do_meio > caixa_inferior:
                caixa_do_meio, caixa_inferior = caixa_inferior, caixa_do_meio

            # Atualiza o estado para refletir a caixa sendo agarrada
            sucessor = np.copy(no.estado)
            sucessor[-1] = caixa_inferior
            sucessor[posicao - 1] = "."
            return No(sucessor, no, "Segurou")
        else:
            return None

    def _soltar(self, posicao, no):
        # Verifica se o braço está segurando uma caixa
        if no.estado[-1] != ".":
            # Determina a posição onde a caixa será solta
            if no.estado[posicao - 1] != ".":
                posicao_soltar = posicao - 1
            elif no.estado[posicao - 2] != ".":
                posicao_soltar = posicao - 2
            elif no.estado[posicao - 3] != ".":
                posicao_soltar = posicao - 3
            else:
                posicao_soltar = posicao - 3

            # Atualiza o estado para refletir a caixa sendo solta
            sucessor = np.copy(no.estado)
            sucessor[posicao_soltar] = no.estado[-1]
            sucessor[-1] = "."
            return No(sucessor, no, "Soltou")
        else:
            return None
