import numpy as np
import random

import no
from algoritmos.dijkstra import dijkstra, FilaPrioridade
from no import No
from problemas.problema import Problema
from problemas.caixas import caixas


class Box:
    def __init__(self, weight):
        self.weight = weight


class bracoRobotico:
    def __init__(self, num_caixas, space_size):
        self.initial_state = self.generate_initial_state(num_caixas, space_size)


def is_goal_state(self, state):
    # Verifica se todas as pilhas têm no máximo três caixas
    for stack in state.stacks:
        if len(stack) > 3:
            return False
    # Verifica se as caixas estão ordenadas por peso em cada pilha
    for stack in state.stacks:
        previous_weight = float('-inf')
        for box in stack:
            if box.weight < previous_weight:
                return False
            previous_weight = box.weight
    return True


def generate_initial_state(self, num_boxes, tamanho_espacos):
    # Aqui vamos criar um estado inicial representando as pilhas de caixas
    initial_state = []

    # Iteramos sobre o número de pilhas desejadas
    for _ in range(num_boxes):
        # Para cada pilha, criamos uma lista vazia para representar as caixas
        stack = []
        # Adicionamos o número correto de caixas à pilha
        for _ in range(3):  # Limite de 3 caixas por pilha
            # Aqui você pode criar uma caixa com um peso aleatório ou com um peso específico, conforme necessário
            box = Box(weight=random.randint(1, 80))  # Exemplo: peso aleatório de 1 a 80
            stack.append(box)
        # Adicionamos a pilha ao estado inicial
        initial_state.append(stack)

    return initial_state


def generate_successors(self, node):
    successors = []

    # Obtém o estado atual do nó
    current_state = node.state

    # Lista de ações possíveis
    actions = ["move_left", "move_right", "stretch_one_step", "stretch_four_steps"]

    for action in actions:
        # Copia o estado atual para que possamos modificá-lo
        new_state = current_state.copy()

        # Aplica a ação ao estado atual e obtém o novo estado
        if action == "move_left":
            new_state.move_left()  # Suponha que você tenha um método definido para mover o braço para a esquerda
        elif action == "move_right":
            new_state.move_right()  # Suponha que você tenha um método definido para mover o braço para a direita
        elif action == "stretch_one_step":
            new_state.stretch_one_step()  # Suponha que você tenha um método definido para mover o braço para a frente
        elif action == "stretch_four_steps":
            new_state.stretch_four_steps()  # Suponha que você tenha um método definido para esticar o braço quatro casas para trás

        # Adiciona o novo estado à lista de sucessores
        successors.append(new_state)

    return successors


def greedy_search(self):
    # Implementação do algoritmo Greedy Search
    current_state = self.initial_state
    visited_states = set()

    while not self.is_goal_state(current_state):
        visited_states.add(current_state)
        successors = self.get_successors(current_state)
        # Escolhe o próximo estado com base apenas no custo imediato
        current_state = min(successors, key=lambda s: s.cost)

    return visited_states


def imprimir(self, no):
    estado = no.estado
    print("Estado atual:")
    print(''.join([f"\r{' '.join(estado[i:i + 8])}\n" for i in range(0, 64, 8)]))


def print_progress(self, current_state):
    print("Progresso do algoritmo:")
    print("Estado atual:")
    print(' '.join(current_state))

resultado_dijkstra = dijkstra(bracoRobotico)
print("Resultado do Dijkstra:", resultado_dijkstra)
fila = FilaPrioridade()
fila.push(0, no)