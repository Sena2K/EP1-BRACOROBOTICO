from problemas.problema import Problema
from algoritmos.a_estrela import a_estrela
from problemas.bracoRobotico import bracoRobotico



if __name__ == "__main__":
    problema = bracoRobotico()

    (qtd_estados_visitados, no_solucao) = a_estrela(problema)

    if (no_solucao is None):
        print("Não houve solução ao problema")
    else:
        # caminho = no_caminho(no_solucao)
        caminho = vertice_caminho(no_solucao)
        print("Solução:")
        print(caminho)

    print(f"Estados visitados: {qtd_estados_visitados}")
    print("Estado Inicial:")
    print(problema.imprimir(problema.no_raiz))

    custo = no_solucao.custoTotal()

    print(custo)
