import numpy as np

from problemas.Custo import Custo
from problemas.problema import Problema
from no import No


class BracoRobotico(Problema):
    def __init__(self):
        self.num_linhas = 6
        self.caixas = 6
        self.estado_inicial = np.array([40, "0", "0", "#",
                                        10, "0", "0", "|",
                                        30, 50, "0", "|",
                                        30, "0", "0", "|",
                                        55, "0", "0", "|",
                                        "0", 33, 11, "|",
                                        44, "0", "0", "|",
                                        "0"])
        self.custo_calculator = Custo()

    def iniciar(self):
        self.no_raiz = No(self.estado_inicial)
        return self.no_raiz

    def imprimir(self, no):
        estado = no.estado
        maquina = ""

        for i in range(self.num_linhas):
            for j in range(4):
                index = i * 4 + j
                maquina += estado[index] + " "
            maquina += "\n"

        maquina += estado[-1]
        return maquina

    def testar_objetivo(self, no):
        estado = no.estado
        count_pilhas = 0
        qtd_pilhas = np.ceil(self.caixas / 3)

        for i in range(self.num_linhas):
            pilha_atual = []
            for j in range(4):
                index = i * 4 + j
                if estado[index] not in ["0", "#", "|"]:
                    pilha_atual.append(int(estado[index]))
                if len(pilha_atual) == 3:
                    if pilha_atual[0] >= pilha_atual[1] >= pilha_atual[2]:
                        count_pilhas += 1
                    pilha_atual = []
        return count_pilhas == qtd_pilhas
    def gerar_sucessores(self, no):
        estado = no.estado
        nos_sucessores = []

        posicao = np.where(estado == "#")[0][0]

        expansoes = [self._direita, self._esquerda, self._agarrar, self._empilhar, self._esquerda2, self._direita2]
        np.random.shuffle(expansoes)
        for expansao in expansoes:
            no_sucessor = expansao(posicao, no)
            if no_sucessor is not None:
                nos_sucessores.append(no_sucessor)

        return nos_sucessores

    def _mover_braco(self, posicao, no, direcao, passos):
        nova_posicao = posicao + passos
        if 0 <= nova_posicao < len(no.estado) and no.estado[nova_posicao] == "|":
            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[nova_posicao]
            sucessor[nova_posicao] = "#"
            return No(sucessor, no, direcao)
        else:
            return None

    def _esquerda(self, posicao, no):
        return self._mover_braco(posicao, no, "←", -4)

    def _esquerda2(self, posicao, no):
        return self._mover_braco(posicao, no, "←←", -8)

    def _direita(self, posicao, no):
        return self._mover_braco(posicao, no, "→", 4)

    def _direita2(self, posicao, no):
        return self._mover_braco(posicao, no, "→→", 8)

    def _agarrar(self, posicao, no):
        if no.estado[-1] == "0":
            if no.estado[posicao - 3] != "0" and no.estado[posicao - 2] == "0" and no.estado[posicao - 1] == "0":
                sucessor = np.copy(no.estado)
                sucessor[-1] = no.estado[posicao - 3]
                sucessor[posicao - 3] = "0"
                return No(sucessor, no)
            elif no.estado[posicao - 3] != "0":
                sucessor = np.copy(no.estado)
                sucessor[-1] = no.estado[posicao - 2]
                sucessor[posicao - 2] = "0"
                return No(sucessor, no)
        return None

    def _empilhar(self, posicao, no):
        if no.estado[-1] != "0":
            if no.estado[posicao - 3] != "0" and no.estado[posicao - 2] != "0" and no.estado[posicao - 1] == "0":
                sucessor = np.copy(no.estado)
                sucessor[posicao - 1] = no.estado[-1]
                sucessor[-1] = "0"
                return No(sucessor, no)
            elif no.estado[posicao - 3] != "0" and no.estado[posicao - 2] == "0":
                sucessor = np.copy(no.estado)
                sucessor[posicao - 2] = no.estado[-1]
                sucessor[-1] = "0"
                return No(sucessor, no)
            elif no.estado[posicao - 3] == "0":
                sucessor = np.copy(no.estado)
                sucessor[posicao - 3] = no.estado[-1]
                sucessor[-1] = "0"
                return No(sucessor, no)
        return None

    def custo(self, no, no_sucessor):
        return self.custo_calculator.calcular_custo(no, no_sucessor)

    def heuristica(self, no):
        estado = no.estado

        numeros = [int(num) for num in estado if num.isdigit()]

        soma = sum(abs(a - b) for a, b in zip(numeros, sorted(numeros, reverse=True)))

        return soma