import graphetest

def findPath(g, start_vertex, end_vertex, poids = 0, path=None):
    """ find a path from start_vertex to end_vertex in graph """
    if path == None:
        path = []
    graph = g.gDict()
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return (path,poids)
    if start_vertex not in graph:
        return None
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_path = findPath(g,vertex, 
                                           end_vertex, 
                                           poids + g.poids(start_vertex, vertex), 
                                           path)
            if extended_path: 
                return extended_path
    return None

def findAllPaths(g, start_vertex, end_vertex,poids=0, path=[]):
    """ find all paths from start_vertex to 
        end_vertex in graph """
    graph = g.gDict() 
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return [(path,poids)]
    if start_vertex not in graph:
        return []
    paths = []
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_paths = findAllPaths(g,vertex, 
                                                 end_vertex, poids+g.poids(start_vertex, vertex),
                                                 path)
            for p in extended_paths: 
                paths.append(p)
    return paths

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

def dijkstra_search(graph, start, goal):
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

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path

g = { "a" : {"d":[2]},
      "b" : {"c":[1]},
      "c" : {"b":[3], "c":[1], "d":[1], "e":[1]},
      "d" : {"a":[1], "c":[1]},
      "e" : {"c":[1]},
    }

graph = graphetest.Graph(g)

graph.addArc("a","f", 4)
graph.addArc("f","d")
graph.addArrete("x","y", 3)
graph.addArrete("x","y", 5)

print(graph.gDict())
graph.delVertex("a")

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())


print('The path from vertex "a" to vertex "b":')
path = findPath(graph,"a", "b")
print(path)

print('The path from vertex "a" to vertex "f":')
path = findPath(graph,"a", "f")
print(path)

print('The path from vertex "c" to vertex "c":')
path = findPath(graph,"c", "c")
print(path)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())


print('All paths from vertex "a" to vertex "b":')
path = findAllPaths(graph,"a", "b")
print(path)

print('All paths from vertex "a" to vertex "f":')
path = findAllPaths(graph,"a", "f")
print(path)

print('All paths from vertex "c" to vertex "c":')
path = findAllPaths(graph,"c", "c")
print(path)
