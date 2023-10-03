"""
    sorts action in such a way if there is a dependency of one action over another
    then the dependent action always comes later than parent action
    Topological sorting is primarily used in scenarios where tasks or activities have dependencies, and you want to determine a valid order in which these tasks can be performed without violating any dependencies.   
"""


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
            # self.adjacency_list[edge].append(vertex)
            return True

        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
            
    
    def topologicalSortUtil(self, visited, vertex, stack):
        visited.add(vertex)
        
        for edge in self.adjacency_list[vertex]:
            if edge not in visited:
                self.topologicalSortUtil(visited, edge, stack)
        
        stack.insert(0, vertex)
    
    def topologicalSort(self):
        
        visited = set()
        stack = []
        
        for vertex in self.adjacency_list:
            if vertex not in visited:
                self.topologicalSortUtil(visited, vertex, stack)
            
        
        print(stack)
                


customGraph = Graph()

customGraph.add_vertex("A")
customGraph.add_vertex("B")
customGraph.add_vertex("C")
customGraph.add_vertex("D")
customGraph.add_vertex("E")
customGraph.add_vertex("F")
customGraph.add_vertex("G")
customGraph.add_vertex("H")


customGraph.add_edge("A", "C")
customGraph.add_edge("B", "C")
customGraph.add_edge("B", "D")
customGraph.add_edge("C", "E")
customGraph.add_edge("E", "F")
customGraph.add_edge("E", "H")
customGraph.add_edge("F", "G")
customGraph.add_edge("D", "F")


customGraph.print_graph()
customGraph.topologicalSort()