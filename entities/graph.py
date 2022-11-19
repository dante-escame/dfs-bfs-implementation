class Graph:
    def __init__(self, alias):
        self.alias = alias
        self.vertexList = []
    
    def get_vertex_by_alias(self, alias):
        return next((x for x in self.vertexList if x.alias == alias), None)

    def get_index_by_alias(self, alias):
        i = 0
        for vertex in self.vertexList:
            if (vertex.alias == alias):
                return i
            i = i + 1

    def add_vertex(self, vertex = None):
        self.vertexList.append(vertex)

    def print_details(self):
        print(self.alias)

    def set_alias(self, alias):
        self.alias = alias