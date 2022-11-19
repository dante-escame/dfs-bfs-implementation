from utils.show import showVertexList

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

def bfs(visited, queue, graph, vertex):
    visited.append(vertex)
    queue.append(vertex)

    while queue:
        newVertex = queue.pop(0)
        showVertexList(queue, "Fila: ")
        showVertexList(visited, "Visitados: ")

        for neighbour in newVertex.edgeList:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    print("\n")