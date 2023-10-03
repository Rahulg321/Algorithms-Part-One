# graph traversal
# using BFS

# deque => combines properties of both stacks and queue
from collections import deque  



class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def remove_edge(self, vertex, edge):
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
        if vertex in self.adjacency_list.keys() and edge in self.adjacency_list.keys():
            self.adjacency_list[vertex].append(edge)
            self.adjacency_list[edge].append(vertex)
            return True

        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def bfs(self, vertex):
        # set => collection of unique elements
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)

            for edge in self.adjacency_list[current_vertex]:
                if edge not in visited:
                    visited.add(edge)
                    queue.append(edge)


customGraph = Graph()

# add all vertices first

customGraph.add_vertex("A")
customGraph.add_vertex("B")
customGraph.add_vertex("C")
customGraph.add_vertex("D")
customGraph.add_vertex("E")


customGraph.add_edge("A", "B")
customGraph.add_edge("A", "C")
customGraph.add_edge("C", "D")
customGraph.add_edge("D", "E")
customGraph.add_edge("E", "B")

print("printing the entire graph")
customGraph.print_graph()

print("using breadth first search")
customGraph.bfs("A")
