from copy import deepcopy
import time as sysTime

class Node:
    def __init__(self):
        self.state = [[], [], [], [], [], [], [], [], []]  # Estado inicial com nove espaços vazios
        self.arm_position = 0  # Posição inicial do braço robótico (esquerda)
        self.nodeNumber = 0
        self.status = 'idle'
        self.neighbours = []
        self.parent = None
        self.children = []
        self.point = 10
        self.max_boxes_per_pile = 3  # Número máximo de caixas por pilha
        self.energy = 0  # Energia inicial do braço robótico

def evalFunc(node):
    node.point = 10  # Reiniciar os pontos

    # Calcular pontos com base na posição das caixas
    weights = [0, 3, 6]  # Pesos das caixas (mais pesado para o mais leve)

    for i, pile in enumerate(node.state):
        if len(pile) > 0:
            if pile[-1] != 0:  # Se a caixa não for vazia
                node.point -= weights[pile[-1] - 1]  # Subtrair pontos com base no peso da caixa

def move(node, source, target):
    new_node = Node()  # Criar uma nova instância de Node
    new_node.state = deepcopy(node.state)  # Copiar o estado atual

    if source != target:  # Verificar se a fonte e o destino são diferentes
        if len(new_node.state[target]) < new_node.max_boxes_per_pile or len(new_node.state[source]) > 0:
            # Verificar se o destino tem espaço vazio ou se a fonte tem caixas
            box = new_node.state[source].pop()  # Remover a caixa da fonte
            new_node.state[target].append(box)  # Adicionar a caixa ao destino

    return new_node


def moveBoxes(node):
    # Função para mover as caixas para empilhá-las do mais pesado para o mais leve
    for i in range(2, -1, -1):  # Loop reverso para começar com a caixa mais pesada
        for j, pile in enumerate(node.state):
            if len(pile) > 0 and pile[-1] == i + 1:  # Se a caixa for encontrada na pilha
                for k in range(2, -1, -1):  # Loop reverso para encontrar uma pilha vazia ou uma pilha com caixa mais leve
                    if len(node.state[k]) == 0 or node.state[k][-1] > i + 1:
                        new_node = move(node, j, k)  # Mover a caixa para a nova posição
                        return new_node  # Retorna o novo estado após o movimento

    return None  # Retorna None se não houver mais movimentos possíveis

def printState(state):
    for pile in state:
        print(pile)

def bestFS():
    global parentList, nodenumber, childList, targetFound

    leastPoint = 10
    for node in parentList:
        evalFunc(node)  # Avaliar o estado atual
        if node.point < leastPoint:
            leastPoint = node.point

    for node in parentList:
        if targetFound:
            break

        if node.point == leastPoint:
            print('\nNode Pai:', node.nodeNumber)
            printState(node.state)

            childnode = moveBoxes(node)  # Tentar mover as caixas para o próximo estado

            if childnode is not None:
                nodenumber += 1
                childnode.nodeNumber = nodenumber
                childnode.parent = node
                parentList.append(childnode)
                print('Node Filho:', childnode.nodeNumber)
                printState(childnode.state)

                if childnode.state == finalState:  # Verificar se o estado atual é o estado final
                    print('\nObjetivo final encontrado')
                    targetFound = True

def readState():
    print('Digite os detalhes do Estado Inicial')
    initial_state = [[], [], [], [], [], [], [], [], []]

    for i in range(3):
        while True:
            weight = int(input(f'Digite o peso da caixa {i + 1}: '))
            if 1 <= weight <= 3:
                initial_state[weight - 1].append(weight)
                break
            else:
                print('Peso inválido. Por favor, digite um peso entre 1 e 3.')

    return initial_state

# Definir o estado final
finalState = [[3], [2], [1], [], [], [], [], [], []]

# Definir o estado inicial
initialState = readState()

# Configurações iniciais
states = [initialState]
nodenumber = 1
targetFound = False

# Criar o nó raiz
root = Node()
root.state = initialState
root.nodeNumber = nodenumber
parentList = [root]

# Executar o algoritmo de busca
bestFS()
