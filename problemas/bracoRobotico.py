import random
import numpy as np
from no import No
from problemas.problema import Problema


class bracoRobotico(Problema):
    def __init__(self):
        # Inicializa o problema do braço robótico
        # Define o número de linhas na configuração do braço
        self.num_linhas = 6

        # Define o estado inicial do problema
        # Cada linha representa uma etapa do braço robótico, com valores para posição, peso e status
        self.estado_inicial = np.array([40, "0", "0", "#",  # Exemplo de configuração inicial do braço
                                        10, "0", "0", "|",
                                        30, 50, "0", "|",
                                        30, "0", "0", "|",
                                        55, "0", "0", "|",
                                        "0", "0", "0", "|",
                                        "0", "0", "0", "|",
                                        "0"])

    def iniciar(self):
        # Inicia o problema retornando o nó raiz com o estado inicial
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
    def box_number(self, no):
        # Função para contar o número de caixas na configuração atual
        count = 0
        for index, estado in enumerate(no.estado):
            if self.verificar_numero(no, index) and estado != "0":
                count += 1
        return count

    def testar_objetivo(self, no):
        # Testa se o objetivo foi alcançado (todas as pilhas corretamente empilhadas)
        estado = no.estado
        count_pilhas = 0
        pilhas_possiveis = np.ceil(self.box_number(no) / 3)  # Calcula o número de pilhas possíveis
        for i in range(self.num_linhas):
            for j in range(4):
                index = i * 4 + j
                if self.verificar_numero(no, index):
                    if self.verificar_numero(no, index + 1) and self.verificar_numero(no, index + 2):
                        # Verifica se é possível empilhar corretamente
                        if int(estado[index]) >= int(estado[index + 1]) and int(estado[index + 1] >= estado[index + 2]):
                            count_pilhas += 1
        return count_pilhas == pilhas_possiveis

    def verificar_numero(self, no, index):
        # Verifica se o elemento na posição index é um número válido
        estado = no.estado
        if estado[index] != "0" and estado[index] != "#" and estado[index] != "|":
            return True

    def gerar_sucessores(self, no):
        # Função para gerar os sucessores válidos a partir de um estado atual
        estado = no.estado
        nos_sucessores = []

        # Encontra a posição do braço robótico (R)
        posicao = np.where(estado == "#")[0][0]

        # Define as operações possíveis (movimentos do braço)
        expansoes = [self._direita, self._esquerda, self._agarrar, self._soltar, self._esquerda2, self._direita2]
        random.shuffle(expansoes)  # Embaralha as operações para tornar a busca menos determinística
        for expansao in expansoes:
            no_sucessor = expansao(posicao, no)
            if no_sucessor is not None: nos_sucessores.append(no_sucessor)

        return nos_sucessores

    def _esquerda(self, posicao, no):
        # Movimento para a esquerda (troca de posição com o elemento à esquerda)
        if posicao not in [0, 1, 2, 3] and no.estado[posicao - 4] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao - 4]
            sucessor[posicao - 4] = "#"
            return No(sucessor, no, "⬅️")
        else:
            None

    def _esquerda2(self, posicao, no):

        if posicao not in [3, 7] and no.estado[posicao - 8] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao - 8]
            sucessor[posicao - 8] = "#"
            return No(sucessor, no, "⬅️⬅️")
        else:
            None

    def _direita(self, posicao, no):
        # Movimento para a direita (troca de posição com o elemento à direita)
        if posicao not in [21, 22, 23, 24] and no.estado[posicao + 4] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao + 4]
            sucessor[posicao + 4] = "#"
            return No(sucessor, no, "➡️")
        else:
            None

    def _direita2(self, posicao, no):
        # Movimento para a direita (troca de posição com o elemento à direita)
        if posicao not in [23, 19] and no.estado[posicao + 8] == "|":

            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[posicao + 8]
            sucessor[posicao + 8] = "#"
            return No(sucessor, no, "➡️➡️")
        else:
            None

    def _agarrar(self, posicao, no):
        # Função para agarrar uma caixa
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

        # Se não houver caixa para agarrar, retorna None
        return None

        None

    def _soltar(self, posicao, no):
        # Função para soltar uma caixa
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
        # Calcula o custo de uma ação
        valor_custo = 1
        estadoAtual = np.where(no.estado == "#")[0][0]  # Posição atual do braço
        estadoFuturo = np.where(no_sucessor.estado == "#")[0][0]  # Posição futura do braço

        # Se a posição futura do braço for igual à posição atual, o custo é zero
        if estadoFuturo == estadoAtual:
            return 0

        # Calcula o custo baseado na distância percorrida pelo braço
        distancia = abs(estadoFuturo - estadoAtual)
        valor_custo += distancia * 0.75

        # Se o braço estiver segurando uma caixa, adiciona um custo adicional baseado no peso da caixa
        if no.estado[-1] != "0":
            peso_caixa = int(no.estado[-1]) / 10
            valor_custo += peso_caixa

        return valor_custo

    def heuristica(self, no):
        # Função heurística para estimar o custo de alcançar o objetivo
        estado = no.estado

        # Filtra os números no estado (removendo '#')
        numeros = [int(num) for num in estado if num.isdigit()]

        # Calcula a soma das diferenças entre os números e suas classificações ordenadas reversamente
        soma = sum(abs(a - b) for a, b in zip(numeros, sorted(numeros, reverse=True)))

        return soma
