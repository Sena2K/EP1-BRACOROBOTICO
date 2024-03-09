import numpy as np

from problemas.Custo import Custo
from problemas.problema import Problema
from no import No


class BracoRobotico(Problema):
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

        self.custo_calculator = Custo()

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

    def testar_objetivo(self, no):
        # Testa se o objetivo foi alcançado (todas as pilhas corretamente empilhadas)
        estado = no.estado
        count_pilhas = 0
        pilhas_possiveis = np.ceil(self.box_number(no) / 3)  # Calcula o número de pilhas possíveis

        for i in range(self.num_linhas):
            pilha_atual = []
            for j in range(4):
                index = i * 4 + j
                if estado[index] != "0" and estado[index] != "#" and estado[index] != "|":
                    pilha_atual.append(int(estado[index]))
                if len(pilha_atual) == 3:  # Se tivermos 3 caixas, verifique se estão empilhadas corretamente
                    if pilha_atual[0] >= pilha_atual[1] and pilha_atual[1] >= pilha_atual[2]:
                        count_pilhas += 1
                    pilha_atual = []  # Reinicie a pilha para a próxima
        return count_pilhas == pilhas_possiveis

    def box_number(self, no):
        # Função para contar o número de caixas na configuração atual
        count = 0
        for index, estado in enumerate(no.estado):
            if estado != "0" and estado != "#" and estado != "|":
                count += 1
        return count

    def gerar_sucessores(self, no):
        # Função para gerar os sucessores válidos a partir de um estado atual
        estado = no.estado
        nos_sucessores = []

        # Encontra a posição do braço robótico (R)
        posicao = np.where(estado == "#")[0][0]

        # Define as operações possíveis (movimentos do braço)
        expansoes = [self._direita, self._esquerda, self._agarrar, self._soltar, self._esquerda2, self._direita2]
        np.random.shuffle(expansoes)  # Embaralha as operações para tornar a busca menos determinística
        for expansao in expansoes:
            no_sucessor = expansao(posicao, no)
            if no_sucessor is not None:
                nos_sucessores.append(no_sucessor)

        return nos_sucessores

    def _mover_braco(self, posicao, no, direcao, passos):
        # Movimento do braço (troca de posição com o elemento na direção especificada)
        nova_posicao = posicao + passos
        if 0 <= nova_posicao < len(no.estado) and no.estado[nova_posicao] == "|":
            sucessor = np.copy(no.estado)
            sucessor[posicao] = sucessor[nova_posicao]
            sucessor[nova_posicao] = "#"
            return No(sucessor, no, direcao)
        else:
            return None

    def _esquerda(self, posicao, no):
        # Movimento para a esquerda (troca de posição com o elemento à esquerda)
        return self._mover_braco(posicao, no, "←", -4)

    def _esquerda2(self, posicao, no):
        # Movimento para a esquerda (troca de posição com o elemento à esquerda)
        return self._mover_braco(posicao, no, "←←", -8)

    def _direita(self, posicao, no):
        # Movimento para a direita (troca de posição com o elemento à direita)
        return self._mover_braco(posicao, no, "→", 4)

    def _direita2(self, posicao, no):
        # Movimento para a direita (troca de posição com o elemento à direita)
        return self._mover_braco(posicao, no, "→→", 8)

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
        return None

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
        # Chama o método calcular_custo da instância de Custo
        return self.custo_calculator.calcular_custo(no, no_sucessor)

    def heuristica(self, no):
        # Função heurística para estimar o custo de alcançar o objetivo
        estado = no.estado

        # Filtra os números no estado (removendo '#')
        numeros = [int(num) for num in estado if num.isdigit()]

        # Calcula a soma das diferenças entre os números e suas classificações ordenadas reversamente
        soma = sum(abs(a - b) for a, b in zip(numeros, sorted(numeros, reverse=True)))

        return soma