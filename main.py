from entities.graph import Graph 
from entities.vertex import Vertex

from logic.methods import dfs
#from logic.methods import bfs

from utils.show import showVertexList

import sys

g = Graph("Padrão")

def reset_graph(graph):
    graphName = input("Digite o nome do grafo: ")
    graph = Graph(graphName)

def insert_vertex(graph):
    vertexName = input("Digite o nome do vértice: ")
    v = Vertex(vertexName)
    graph.add_vertex(v)

def add_edge_to_vertex(graph):
    vertex1 = input("Digite o nome do primeiro vértice:")
    vertex2 = input("Digite o nome do segundo vértice:")
    v1 = graph.get_index_by_alias(vertex1)
    v2 = graph.get_index_by_alias(vertex2)
    graph.vertexList[v1].add_edge(graph.vertexList[v2])
    print(graph.vertexList[v1].edgeList[0])

def show_graph(graph):
    for vertex in graph.vertexList:
        print('Vértice', vertex.alias)
        showVertexList(vertex.edgeList)

reset_graph(g)
while(1):
    print("0 - Mostra o Grafo\n1 - Insere um vértice novo no Grafo\n2 - Insere uma aresta nova no Grafo\n3 - Executa DFS\n4 - Executa BFS.")
    opcao = input("Digite a opção:")
    if opcao == '0':
        show_graph(g)
    elif opcao == '1':
        insert_vertex(g)
    elif opcao == '2':
        add_edge_to_vertex(g)
    elif opcao == '3':
        visited = set() # lista nao ordenada
        showVisited = [] # lista ordenada
        dfs(showVisited, visited, g, g.vertexList, 0)
    else:
        print("Fim do programa")
        sys.exit()

