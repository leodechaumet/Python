class Graph(object):

    def __init__(self, graph_dict={}):
        self.__graph_dict = graph_dict
        
    def vertices(self):
        return list(self.__graph_dict.keys())
    def gDict(self):
        return self.__graph_dict
    def edges(self):
        return self.__generate_edges()
    def n(self):
        return len(self.__graph_dict)
    
    def weight(self, x, y):
        return min(self.__graph_dict[x][y])
    
    def neighbors(self, x):
        return self.__graph_dict[x].keys()
    def cost(self, x, y):
        return self.__graph_dict[x][y]

    def addVertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = {}
    def delVertex(self, vertex):
        if vertex in self.__graph_dict:
            self.__graph_dict.pop(vertex, None)
        for e in self.__graph_dict:
            if vertex in self.__graph_dict[e]:
                self.__graph_dict[e].pop(vertex, None)
            

    def addArc(self, x, y, poids = 1):
        arc = (str(x), str(y))
        (vertex1, vertex2) = tuple(arc)
        self.addVertex(vertex1)
        self.addVertex(vertex2)
        if vertex1 in self.__graph_dict:
            if vertex2 in self.__graph_dict[vertex1]:
                self.__graph_dict[vertex1][vertex2].append(poids)
            else:
                self.__graph_dict[vertex1][vertex2] = [poids]
        else:

            self.__graph_dict[vertex1][vertex2] = [poids]
    
    def delArc(self, x, y):
        if y in self.__graph_dict[x]:
            self.__graph_dict[x].pop(y, None)

    def addArrete(self, x, y, poids = 1):
        self.addArc(x,y , poids)
        self.addArc(y, x, poids)
    def delArrete(self, x, y):
        self.delArc(x,y)
        self.delArc(y, x)

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if (vertex, neighbour) not in edges:
                    edges.append((vertex, neighbour))
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

import heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def dijkstra(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far


G = {
    "A": {"B":2, "C":5},
    "B": {"A": 2, "D": 3, "E": 1, "F": 1},
    "C": {"A": 5, "F": 3},
    "D": {"B": 3},
    "E": {"B": 4, "F": 3},
    "F": {"C": 3, "E": 3},
}

G = Graph(G)

r"""
Layout of G2:

E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
 \                                         /\
  \                                        ||
    ----------------- 3 --------------------
"""
G2 = {
    "B": {"C": 1},
    "C": {"D": 1},
    "D": {"F": 1},
    "E": {"B": 1, "F": 3},
    "F": {},
}
G2 = Graph(G2)


r"""
Layout of G3:

E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
 \                                         /\
  \                                        ||
    -------- 2 ---------> G ------- 1 ------
"""
G3 = {
    "B": {"C": 1},
    "C": {"D": 1},
    "D": {"F": 1},
    "E": {"B": 1, "G": 2},
    "F": {},
    "G": {"F": 1},
}
G3 = Graph(G3)


shortDistance = dijkstra(G, "E", "C")
print(shortDistance)  # E -- 3 --> F -- 3 --> C == 6

shortDistance = dijkstra(G2, "E", "F")
print(shortDistance)  # E -- 3 --> F == 3

shortDistance = dijkstra(G3, "C", "E")

print(shortDistance)  # E -- 2 --> G -- 1 --> F == 3
print(reconstruct_path(shortDistance[0], "E", "F"))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
