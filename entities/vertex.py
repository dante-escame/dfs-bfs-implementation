class Vertex:
    def __init__(self, alias):
        self.alias = alias
        self.edgeList = []
    
    def add_edge(self, vertex):
        self.edgeList.append(vertex)