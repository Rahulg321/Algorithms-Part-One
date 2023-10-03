class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def remove_edge(self, vertex, edge):
        # remove the link
        if vertex in self.adjacency_list.keys() and edge in self.adjacency_list.keys():
            self.adjacency_list[vertex].remove(edge)
            self.adjacency_list[edge].remove(vertex)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for edge in self.adjacency_list[vertex]:
                if edge in self.adjacency_list.keys():
                    self.adjacency_list[edge].remove(vertex)

            del self.adjacency_list[vertex]
        else:
            return False

    def add_edge(self, vertex, edge):
        # first check if both vertices exist or not
        if vertex in self.adjacency_list.keys() and edge in self.adjacency_list.keys():
            self.adjacency_list[vertex].append(edge)
            self.adjacency_list[edge].append(vertex)
            return True

        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])


customGraph = Graph()

customGraph.add_vertex("A")
customGraph.add_vertex("B")
customGraph.add_vertex("C")
customGraph.add_vertex("D")


customGraph.add_edge("A", "B")
customGraph.add_edge("A", "C")

customGraph.add_edge("B", "C")
customGraph.add_edge("A", "D")
customGraph.add_edge("D", "C")


# customGraph.remove_edge("A", "C")


customGraph.print_graph()

print("removing vertex D")
customGraph.remove_vertex("D")
customGraph.print_graph()
