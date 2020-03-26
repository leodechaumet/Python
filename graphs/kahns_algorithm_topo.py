# Kahn's Algorithm is used to find Topological ordering of Directed Acyclic Graph using BFS
from structure import Graph
def topologicalSort(g):
    l=GraphToAdjListeInt(g)

    indegree = [0] * len(l)
    queue = []
    topo = []
    cnt = 0

    for key, values in l.items():
        for i in values:
            indegree[i] += 1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        vertex = queue.pop(0)
        cnt += 1
        topo.append(vertex)
        for x in l[vertex]:
            indegree[x] -= 1
            if indegree[x] == 0:
                queue.append(x)

    if cnt != len(l):
        return ("Cycle exists")
    else:
        return(topo)

def GraphToAdjListeInt(g):
    m={}
    vertices = g.vertices()
    for v in range(g.n()):
        m[v] = []
        #print(m)
    for i,v in enumerate(vertices):
        neighbors = g.neighbors(v)
        for j,n in enumerate(vertices):
            if n in neighbors:
                m[i].append(j)
    return m

G3 = {
    "B": {"C": 1},
    "C": {"D": 1},
    "D": {"F": 1},
    "E": {"B": 1, "G": 2},
    "F": {},
    "G": {"F": 1},
}
g = Graph(G3)
print(GraphToAdjListeInt(g))

# Adjacency List of Graph
#l = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []}
a=(topologicalSort(g))
r=[]
n=g.vertices()
for e in a:
    r.append(n[e])
print(r)