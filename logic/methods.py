from utils.show import showVertexList

def dfs(viewVisited, visited, graph, vertex):
    # parar o fluxo de chamadas recursivas se for folha
    if vertex not in visited:
        visited.add(vertex)
        viewVisited.append(vertex)

        ### lista ordenada para visualizacao ###
        print(showVertexList(viewVisited, "Visitados: "))
        ######################################

        # percorrer os filhos recursivamente
        for neighbour in vertex.edgeList: 
            print('Acessando filhos do vértice', vertex.alias)
            dfs(viewVisited, visited, graph, neighbour)
    else:
        print('Vértice', vertex.alias, 'já está na fila:')

def bfs(vertex):
    visited = []
    queue = []
    visited.append(vertex)
    queue.append(vertex)

    i = 0

    # enquanto a fila nao estiver vazia
    while queue:
        # tira o vertice mais velho
        newVertex = queue.pop(0)
        print(showVertexList(queue, "Fila: "), " | ", newVertex.alias, "foi removido")

        # para todos os vizinhos do vertice atual que ainda nao foram visitados
        for neighbour in newVertex.edgeList:
            if neighbour not in visited:
                visited.append(neighbour)
                print(showVertexList(visited, "Visitados: "), " | ", neighbour.alias, "foi adicionado")
                queue.append(neighbour)
                print(showVertexList(queue, "Fila: "), " | ", neighbour.alias, "foi adicionado")

    print("\n")