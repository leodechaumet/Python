""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
structure : 
    g = { "a" : {"d":[1,2,4]},
          "b" : {"c":[1]},
          "c" : {"b":[1], "c":[1], "d":[1], "e":[1]},
          "d" : {"a":[1], "c":[1]},
          "e" : {"c":[1]},
          "f" : {}
        }
"""


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
        return min(self.__graph_dict[x][y])

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

def listeToGraph(liste):
    g = Graph()
    for i in range(len(liste)):
        for j in range(len(liste)):
            g.addArrete(i,j,liste[i][j])
    return g

if __name__ == "__main__":

    g = { "a" : {"d":[1]},
          "b" : {"c":[1]},
          "c" : {"b":[1], "c":[1], "d":[1], "e":[1]},
          "d" : {"a":[1], "c":[1]},
          "e" : {"c":[1]},
          "f" : {}
        }


    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("del vertice")
    print(graph.delVertex("c"))

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.addVertex("z")

    print("Vertices of graph:")
    print(graph.vertices())
 
    print("Add an edge:")
    graph.addArc("a","z", 7)
    
    print("Vertices of graph:")
    print(graph.gDict())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.addArc("x","y")
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
    g2=Graph()
    print(g2.edges())
    print(graph.vertices())
    #print(graphToFlow(graph))
