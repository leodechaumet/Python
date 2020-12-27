# floyd_warshall.py
"""
    The problem is to find the shortest distance between all pairs of vertices in a weighted directed graph that can
    have negative edge weights.
"""


def _print_dist(dist, v):
    print("\nThe shortest path matrix using Floyd Warshall algorithm\n")
    for i in range(v):
        for j in range(v):
            if dist[i][j] != float("inf"):
                print(int(dist[i][j]), end="\t")
            else:
                print("INF", end="\t")
        print()


def floyd_warshall(graph):
    """
    :param graph: 2D array calculated from weight[edge[i, j]]
    :type graph: List[List[float]]
    :param v: number of vertices
    :type v: int
    :return: shortest distance between all vertex pairs
    distance[u][v] will contain the shortest distance from vertex u to v.

    1. For all edges from v to n, distance[i][j] = weight(edge(i, j)).
    3. The algorithm then performs distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]) for each
    possible pair i, j of vertices.
    4. The above is repeated for each vertex k in the graph.
    5. Whenever distance[i][j] is given a new minimum value, next vertex[i][j] is updated to the next vertex[i][k].
    """
    v = g.n()

    dist = [[float("inf") for _ in range(v)] for _ in range(v)]

    for i,e in enumerate(graph.vertices()):
        for j,f in enumerate(graph.vertices()):
            if f in graph.neighbors(e):dist[i][j] = graph.cost(e,f)

            # check vertex k against all other vertices (i, j)
    for k in range(v):
        # looping through rows of graph array
        for i in range(v):
            # looping through columns of graph array
            for j in range(v):
                if (
                    dist[i][k] != float("inf")
                    and dist[k][j] != float("inf")
                    and dist[i][k] + dist[k][j] < dist[i][j]
                ):
                    dist[i][j] = dist[i][k] + dist[k][j]
    n = graph.vertices()
    d={}

    for i in range(v):
        d[n[i]] = {}
        for j in range(v):
            d[n[i]][n[j]]=dist[i][j]
    return d

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



if __name__ == "__main__":

    G = {
    "A": {"B":2, "C":5},
    "B": {"A": 2, "D": 3, "E": 1, "F": 1},
    "C": {"A": 5, "F": 3},
    "D": {"B": 3},
    "E": {"B": 4, "F": 3},
    "F": {"C": 3, "E": 3},
    }

    print("-------G----------")

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


    shortDistance = floyd_warshall(G, G.n())
    print(shortDistance)  # E -- 3 --> F -- 3 --> C == 6

    print("--------G2------------")
    shortDistance = floyd_warshall(G2,G2.n())

    print(shortDistance)  # E -- 3 --> F == 3
    print("--------G3------------")

    shortDistance = floyd_warshall(G3, G3.n())
    print(shortDistance)


    # # Expected Output from the vertice, edge and src, dst, weight inputs!!
    # 0		INF	INF
    # INF	0	2
    # INF	1	0
