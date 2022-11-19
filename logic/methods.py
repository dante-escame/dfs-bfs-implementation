from utils.show import showVertexList
import collections

def dfs(showVisited, visited, graph, vertex, i):
    if vertex not in visited:
        # adiciona o vertice na lista de visitados
        visited.add(vertex)

        # printa a iteracao
        print('iteracao: ', i)
        i = i + 1
        showVisited.append(vertex)

        ### lista ordenada para visualizacao ###
        showVertexList(showVisited)
        ######################################

        # percorre os vizinhos do vertice atual recursivamente
        for neighbour in vertex.edgeList:
            dfs(showVisited, visited, graph, neighbour, i)