class Vertex:
    def __init__(self, alias):
        self.alias = alias
        self.edgeList = []

    def print_details(self):
        print(self.alias)
    
    def add_edge(self, vertex):
        self.edgeList.append(vertex)

    def get_alias(self):
        return self.alias
    
    def edge_list(self):
        return self.edgeList