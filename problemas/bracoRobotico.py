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

    def gerar_sucessores(self, no):
        estado = no.estado
        nos_sucessores = []


        posicao = np.where(estado == "R")[0][0]

        expansoes = [self._direita, self._esquerda, self._agarrar, self._soltar]
        random.shuffle(expansoes)
        for expansao in expansoes:
            no_sucessor = expansao(posicao, no)
            if no_sucessor is not None: nos_sucessores.append(no_sucessor)

        return nos_sucessores

    def _esquerda(self, posicao, no):
        # movimento para esquerda fazendo swap apenas na ultima coluna
        if posicao not in [0, 1, 2, 3] and no.estado[posicao - 4] == "|":

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

    def _mover_direita_2(self, posicao, no):
        # Movimento para a direita movendo 2 blocos
        if posicao not in [19, 23, 24] and no.estado[posicao + 8] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao + 8]
            sucessor[posicao + 8] = "R"

            posicao += 8  # Atualiza a posição após mover 2 blocos

            sucessor[posicao] = sucessor[posicao + 4]
            sucessor[posicao + 4] = "."

            return No(sucessor, no, "➡️")
        else:
            None

    def _mover_esquerda_2(self, posicao, no):
        # Movimento para a esquerda movendo 2 blocos
        if posicao not in [4, 0, 1] and no.estado[posicao - 8] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao - 8]
            sucessor[posicao - 8] = "R"

            posicao -= 8  # Atualiza a posição após mover 2 blocos

            sucessor[posicao] = sucessor[posicao - 4]
            sucessor[posicao - 4] = "."

            return No(sucessor, no, "⬅️")
        else:
            None

    def _mover_direita_3(self, posicao, no):
        # Movimento para a direita movendo 3 blocos
        if posicao not in [18, 19, 23, 24] and no.estado[posicao + 12] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao + 12]
            sucessor[posicao + 12] = "R"

            posicao += 12  # Atualiza a posição após mover 3 blocos

            sucessor[posicao] = sucessor[posicao + 8]
            sucessor[posicao + 8] = "."

            posicao += 8  # Atualiza a posição após mover 3 blocos

            sucessor[posicao] = sucessor[posicao + 4]
            sucessor[posicao + 4] = "."

            return No(sucessor, no, "➡️")
        else:
            None

    def _mover_esquerda_3(self, posicao, no):
        # Movimento para a esquerda movendo 3 blocos
        if posicao not in [5, 6, 1, 2] and no.estado[posicao - 12] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao - 12]
            sucessor[posicao - 12] = "R"

            posicao -= 12  # Atualiza a posição após mover 3 blocos

            sucessor[posicao] = sucessor[posicao - 8]
            sucessor[posicao - 8] = "."

            posicao -= 8  # Atualiza a posição após mover 3 blocos

            sucessor[posicao] = sucessor[posicao - 4]
            sucessor[posicao - 4] = "."

            return No(sucessor, no, "⬅️")
        else:
            None

    def _mover_direita_4(self, posicao, no):
        # Movimento para a direita movendo 4 blocos
        if posicao not in [17, 18, 22, 23, 24] and no.estado[posicao + 12] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao + 12]
            sucessor[posicao + 12] = "R"

            posicao += 12  # Atualiza a posição após mover 4 blocos

            sucessor[posicao] = sucessor[posicao + 8]
            sucessor[posicao + 8] = "."

            posicao += 8  # Atualiza a posição após mover 4 blocos

            sucessor[posicao] = sucessor[posicao + 4]
            sucessor[posicao + 4] = "."

            return No(sucessor, no, "➡️")
        else:
            None

    def _mover_esquerda_4(self, posicao, no):
        # Movimento para a esquerda movendo 4 blocos
        if posicao not in [4, 5, 1, 2, 3] and no.estado[posicao - 12] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao - 12]
            sucessor[posicao - 12] = "R"

            posicao -= 12  # Atualiza a posição após mover 4 blocos

            sucessor[posicao] = sucessor[posicao - 8]
            sucessor[posicao - 8] = "."

            posicao -= 8  # Atualiza a posição após mover 4 blocos

            sucessor[posicao] = sucessor[posicao - 4]
            sucessor[posicao - 4] = "."

            return No(sucessor, no, "⬅️")
        else:
            None

    def _agarrar(self, posicao, no):

        if no.estado[posicao - 3] != "." and no.estado[posicao - 2] != ".":
            sucessor = np.copy(no.estado)
            sucessor[-1] = no.estado[posicao - 1]
            sucessor[posicao - 1] = "."
            return No(sucessor, no, "Segurou")

        elif no.estado[posicao - 2] != ".":
            sucessor = np.copy(no.estado)
            sucessor[-1] = no.estado[posicao - 2]
            sucessor[posicao - 2] = "."
            return No(sucessor, no, "Segurou")

        elif no.estado[posicao - 3] != ".":
            sucessor = np.copy(no.estado)
            sucessor[-1] = no.estado[posicao - 3]
            sucessor[posicao - 3] = "."
            return No(sucessor, no, "Segurou")
        else:
            None


    def _soltar(self, posicao, no):

        if no.estado[posicao - 3] != "." and no.estado[posicao - 2] != ".":
            sucessor = np.copy(no.estado)
            sucessor[posicao - 1] = no.estado[-1]
            sucessor[-1] = "."
            return No(sucessor, no, "Soltou")

        elif no.estado[posicao - 3] != ".":
            sucessor = np.copy(no.estado)
            sucessor[posicao - 2] = no.estado[-1]
            sucessor[-1] = "."
            return No(sucessor, no, "Soltou")

        elif no.estado[posicao - 3] == ".":
            sucessor = np.copy(no.estado)
            sucessor[posicao - 3] = no.estado[-1]
            sucessor[-1] = "."
            return No(sucessor, no, "Soltou")
        else:
            None

    def custo(self, no, no_sucessor):
        valor_custo = 1
        estadoAtual = np.where(no.estado == "R")[0][0]
        estadoFuturo = np.where(no_sucessor.estado == "R")[0][0]

        # print(estadoAtual, estadoFuturo, estadoFuturo - estadoAtual)

        # ato de pegar uma caixa n tem custo
        if estadoFuturo - estadoAtual == 0:
            return 0

        # tem q arrumar -> np.where retorna os indices, algo usando mod talvez resolva
        # o braco so anda um por vez ainda entao talvez seja isso tbm
        # if(estadoFuturo - estadoAtual > 4)

        # esse if deve resolver caso o braco ande mais de um espaco
        if (estadoFuturo - estadoAtual) / 4 > 1:
            valor_custo = (estadoFuturo - estadoAtual) * 0.75

            # verifica se ta segurando uma caixa, se nao, custo 1
        # se sim calcula o custo baseado no peso da caixa
        if no.estado[-1] == ".":
            return valor_custo
        else:
            valor_custo += int(no.estado[-1]) / 10
            return valor_custo

    def heuristica(self, no):
        estado = no.estado
        resultado = [
            ["30", "20", "10", "R"],
            [".", ".", ".", "|"],
            [".", ".", ".", "|"],
            ["30", ".", ".", "|"],
            [".", ".", ".", "|"],
            [".", ".", ".", "|"],
            ["."]
        ]
        estado_matriz = [estado[0:4], estado[4:8], estado[8:12], estado[12:16],
                         estado[16:20], estado[20:24]]

        soma = 0

        for i in range(len(resultado)):
            for j in range(len(resultado[i])):
                valor = resultado[i][j]
                soma = soma + self._distancia_manhattan(valor, estado_matriz, i, j)

        return soma

    # Distância de Manhattan: d = |xi-xj| + |yi-yj|
    def _distancia_manhattan(self, valor, estado, i, j):
        for k in range(len(estado)):
            for h in range(len(estado[k])):
                if valor == estado[k][h]: return abs(i - k) + abs(j - h)
        return 0

