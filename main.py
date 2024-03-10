from algoritmos.dfs import dfs
from algoritmos.bfs import bfs
from algoritmos.a_estrela import a_estrela
from algoritmos.dijkstra import dijkstra
from auxiliar.Visitados import vertice_caminho, no_caminho
from algoritmos.ganancioso import ganancioso

#from problemas.bracoRobotico import BracoRobotico
from problemas.bracoManual import BracoRobotico

if __name__ == "__main__":
    problema = BracoRobotico()

    # (qtd_estados_visitados, no_solucao) = dfs(problema)
    # (qtd_estados_visitados, no_solucao) = bfs(problema)

    # (qtd_estados_visitados, no_solucao) = ganancioso(problema)
    (qtd_estados_visitados, no_solucao) = a_estrela(problema)
    # (qtd_estados_visitados, no_solucao) = dijkstra(problema)

    if (no_solucao is None):
        print("Não houve solução ao problema")
    else:
        caminho = vertice_caminho(no_solucao)
        print("Solução:")
        print(caminho)

    print(f"Estados visitados: {qtd_estados_visitados}")
    print("Estado Inicial:")
    print(problema.imprimir(problema.no_raiz))
    print("\n")
    try:
        print(problema.imprimir(no_solucao))
        print(f"Custo: {no_solucao.custoTotal()}")
    except:
        print("Não foi possivel achar solução")

