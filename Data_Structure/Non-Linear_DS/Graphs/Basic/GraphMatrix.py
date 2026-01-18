class GraphMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight=1, directed=False):
        self.matrix[u][v] = weight
        if not directed:
            self.matrix[v][u] = weight
    
    def display(self):
        for row in self.matrix:
            print(row)

# Example
g = GraphMatrix(4)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 2)
g.add_edge(0, 3, 3)
g.display()
