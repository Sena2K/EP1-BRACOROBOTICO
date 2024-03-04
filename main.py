from algoritmos.dfs import dfs
from auxiliar.Visitados import vertice_caminho, no_caminho
from problemas.bracoRobotico import Braco

if __name__ == "__main__":
    problema = Braco()

    (qtd_estados_visitados, no_solucao) = dfs(problema)


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