import sys

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    shortest_path = {}
 
    previous_nodes = {}
 
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
 
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        return self.graph[node1][node2]


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print(", ".join(reversed(path)))

nodes = ["Oradea","Zerind","Arad","Sibiu","Fagaras","Timisoara","Lugoj","Mehadia","Dobreta","Craiova","Rimnicu Vilcea","Pitesti","Bucharest","Girgiu","Urziceni","Hirsova","Vaslui","Eforie","Iasi","Neamt",]
 
init_graph = {}
for node in nodes:
    init_graph[node] = {}
    
init_graph["Oradea"]["Zerind"] = 71
init_graph["Oradea"]["Sibiu"] = 151

init_graph["Zerind"]["Arad"] = 75
init_graph["Zerind"]["Oradea"] = 71

init_graph["Sibiu"]["Oradea"] = 150
init_graph["Sibiu"]["Arad"] = 140
init_graph["Sibiu"]["Fagaras"] = 99
init_graph["Sibiu"]["Rimnicu Vilcea"] = 80

init_graph["Arad"]["Timisoara"] = 118
init_graph["Arad"]["Zerind"] = 175
init_graph["Arad"]["Sibiu"] = 140

init_graph["Timisoara"]["Lugoj"] = 111
init_graph["Timisoara"]["Arad"] = 118

init_graph["Lugoj"]["Mehadia"] = 70
init_graph["Lugoj"]["Timisoara"] = 111

init_graph["Mehadia"]["Dobreta"] = 75
init_graph["Mehadia"]["Lugoj"] = 70

init_graph["Dobreta"]["Craiova"] = 120
init_graph["Dobreta"]["Mehadia"] =75

init_graph["Craiova"]["Dobreta"] = 120
init_graph["Craiova"]["Rimnicu Vilcea"] = 146
init_graph["Craiova"]["Pitesti"] = 138

init_graph["Pitesti"]["Bucharest"] = 101
init_graph["Pitesti"]["Rimnicu Vilcea"] = 97
init_graph["Pitesti"]["Craiova"] = 138

init_graph["Bucharest"]["Girgiu"] = 90
init_graph["Bucharest"]["Pitesti"] = 101
init_graph["Bucharest"]["Fagaras"] = 211
init_graph["Bucharest"]["Urziceni"] = 85

init_graph["Fagaras"]["Bucharest"] = 211
init_graph["Fagaras"]["Sibiu"] = 99

init_graph["Rimnicu Vilcea"]["Pitesti"] = 97
init_graph["Rimnicu Vilcea"]["Sibiu"] = 80
init_graph["Rimnicu Vilcea"]["Craiova"] = 146

init_graph["Urziceni"]["Bucharest"] = 85
init_graph["Urziceni"]["Vaslui"] = 142
init_graph["Urziceni"]["Hirsova"] = 98

init_graph["Hirsova"]["Eforie"] = 86
init_graph["Hirsova"]["Urziceni"] = 98

init_graph["Vaslui"]["Iasi"] = 92
init_graph["Vaslui"]["Urziceni"] = 142

init_graph["Iasi"]["Neamt"] = 87
init_graph["Iasi"]["Vaslui"] = 92

init_graph["Neamt"]["Iasi"] = 87


graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Iasi")
print_result(previous_nodes, shortest_path, start_node="Iasi", target_node="Hirsova")
