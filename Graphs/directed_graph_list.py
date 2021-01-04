class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, source, destination):
        if self.adjacency_list.get(source) is None:
            self.adjacency_list[source] = set()
        self.adjacency_list[source].add(destination)

    def print(self):
        print(self.adjacency_list)
        for i in self.adjacency_list:
            for j in self.adjacency_list[i]:
                print("Vertex: " + str(i) + " -> " + str(j))

    def dfs(self):
        print("dfs")


