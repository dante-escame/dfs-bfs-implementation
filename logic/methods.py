from utils.show import showVertexList

def dfs(showVisited, visited, graph, vertex):
    if vertex not in visited:
        visited.add(vertex)
        showVisited.append(vertex)

        ### lista ordenada para visualizacao ###
        showVertexList(showVisited)
        ######################################

        for neighbour in vertex.edgeList:
            dfs(showVisited, visited, graph, neighbour, i)

def bfs(visited, queue, vertex):
    visited.append(vertex)
    queue.append(vertex)

    while queue:
        newVertex = queue.pop(0)
        
        for neighbour in newVertex.edgeList:
            showVertexList(visited, "Visitados: ")
            showVertexList(queue, "Fila: ")
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    print("\n")