import numpy as np
from problemas.problema import Problema
from problemas.Custo import Custo
from no import No

class BracoRobotico(Problema):
    def __init__(self):
        self.num_linhas = 6
        self.caixas = 6
        self.pilhaMaxima = 3
        self.estado_inicial = np.array([40, "0", "0", "#",
                                        10, "0", "0", "|",
                                        30, 50, "0", "|",
                                        30, "0", "0", "|",
                                        55, "0", "0", "|",
                                        "0", "0", "0", "|",
                                        "0", "0", "0", "|",
                                        "0"])
        self.custo_calculator = Custo()

    def iniciar(self):
        self.no_raiz = No(self.estado_inicial)
        self.procurar_caixa(self.no_raiz.estado)
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

    def procurar_caixa(self, estado_atual):
        caixas = []
        for i in range(3, len(estado_atual)):
            caixa_peso = estado_atual[i]
            # Skip separators and empty spaces
            if caixa_peso != "0" and caixa_peso != "#" and caixa_peso != "|":
                caixas.append((i, int(caixa_peso)))  # Convert the weight to int
        return caixas

    def testar_objetivo(self, no):
        # Obtém o estado atual do nó
        estado = no.estado
        # Inicializa a contagem de pilhas completas
        count_pilhas = 0
        # Calcula o número total de pilhas completas necessárias
        qtd_pilhas_maximas = np.ceil(self.caixas / 3)

        # Itera sobre as linhas da configuração do braço robótico
        for i in range(self.num_linhas):
            # Inicializa uma lista para representar a pilha atual
            pilha_atual = []
            # Itera sobre as colunas da configuração do braço robótico
            for j in range(4):
                # Calcula o índice correspondente à posição atual
                index = i * 4 + j
                # Verifica se o elemento na posição atual não é um espaço vazio ou um separador
                if estado[index] not in ["0", "#", "|"]:
                    # Adiciona a altura da caixa à pilha atual
                    pilha_atual.append(int(estado[index]))
                # Verifica se a pilha atual atingiu o limite de altura (3 caixas)
                if len(pilha_atual) == 3:
                    # Verifica se as caixas na pilha atual estão em ordem decrescente
                    if pilha_atual[0] >= pilha_atual[1] >= pilha_atual[2]:
                        # Incrementa a contagem de pilhas completas
                        count_pilhas += 1
                    # Reinicia a lista da pilha atual para processar a próxima pilha
                    pilha_atual = []

        # Retorna True se o número de pilhas completas for igual ao número necessário, caso contrário, False
        return count_pilhas == qtd_pilhas_maximas

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
        # Verifica se há uma caixa na garra do braço robótico
        if no.estado[-1] != "0":
            # Encontra a próxima posição disponível para empilhar a caixa na mesma coluna da posição atual
            nova_posicao = posicao
            while nova_posicao >= 0 and no.estado[nova_posicao] != "|":
                nova_posicao -= 1

            # Verifica se há espaço disponível para empilhar a caixa na posição encontrada
            if nova_posicao >= 0:
                # Cria uma cópia do estado atual
                sucessor = np.copy(no.estado)
                # Move a caixa da garra do braço robótico para a posição encontrada
                while sucessor[nova_posicao] != "0":
                    nova_posicao -= 1
                sucessor[nova_posicao] = no.estado[-1]
                # Libera a garra do braço robótico
                sucessor[-1] = "0"
                # Retorna o novo nó representando o estado resultante
                return No(sucessor, no)

        # Retorna None se não for possível empilhar a caixa
        return None

    def custo(self, no, no_sucessor):
        return self.custo_calculator.calcular_custo(no, no_sucessor)

    def heuristica(self, no):
        estado = no.estado
        numeros = [int(num) for num in estado if num.isdigit()]
        soma = sum(abs(a - b) for a, b in zip(numeros, sorted(numeros, reverse=True)))

        return soma
