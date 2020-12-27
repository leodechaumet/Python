
#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import math
import sys
import time
start_time = time.time()

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
    
    def poids(self, x, y):
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

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
def splitT(l):
	l = l.split(" ")
	for i,e in enumerate(l):
		try:
			val = int(e)
		except ValueError:
			val = e
		l[i] = val
	return l

def strToTupple(l):
	return [tuple(splitT(e)) if len(tuple(splitT(e))) != 1 else splitT(e)[0] for e in l]


lines = strToTupple(lines)

f = lines.pop(0)

def distance (t1,t2):
    s=0
    for i in range(len(t1)):
        s+=(t1[i] - t2[i])**2
    return math.sqrt(s)

l=[]
def sortT(l, i):
    return sorted(l, key=lambda tup: tup[i])
lines = sortT(lines, 1)

for i in range(0, f-1):
    for j in range(i+1, f):
        l.append(((lines[i][1], lines[j][1]), distance(lines[i], lines[j])))

def findAllPaths(g, start_vertex, end_vertex,poids=0, path=[]):
    """ find all paths from start_vertex to 
        end_vertex in graph """
    start_vertex = str(start_vertex)
    end_vertex = str(end_vertex)
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

def addPlusArc(g, l):
    for e in l:
        g.addArc(e[0][0], e[0][1], e[1])

g = Graph()
addPlusArc(g, l)
def gDup(g):
    d = dict(g.gDict())
    for e in d:
        d[e] = dict(d[e])
    return Graph(d)

def gInv(g):
    gI = Graph({})
    for (x,y) in g.edges():
        gI.addArc(y, x, g.poids(x,y))
    return gI
def cheminToArc(l):
    e=[]
    for i in range(1, len(l)):
        e.append((l[i-1], l[i]))
    return e
def delPlusArc(g, l):
    for e in l:
        g.delArc(e[0], e[1])
        
def poidsChemin(g,chemin):
    s=0
    for i in range(1, len(chemin)):
        s+=g.poids(chemin[i-1], chemin[i])
    return s

import itertools
def findsubsets(S):
    l = []
    S = S[1:] + S[:-1]
    for i in range(1, len(S)):
        l+=set(itertools.combinations(S, i))
    return l
    

#print(findsubsets(g.vertices()))
somme = []
#print(l)
#sys.stderr.write(str(g.edges()))
#print(g.gDict())
#print(g.n())
#g2 = gDup(g)
#gi = gInv(g2)
mem = {}
v = g.vertices()
print(v)
p=g.vertices()[0]
d=g.vertices()[-1]
for e in findsubsets(g.vertices()):
    e=list(e)
    if e[0] != p:
        e=[p]+e
    if e[-1] != d:
        e.append(d)
    visite = 0
    t=0

    #g2 = gDup(gi)
    v2 = list(v)
    #print("e",e)
    for i in range(1, len(e)-1):
        v2.remove(e[i])
    #print("v2,",v2)


    
    #print(g2.gDict())

    
    visite += len(e)
    t=poidsChemin(g, e)
    t += poidsChemin(g,v2)

    # y = -1
    # try:
    #     somme.append(mem[str(g2.vertices())])
    # except:
    #     for x in sorted([int(v) for v in g2.vertices()]):
    #         x=str(x)
    #         if int(y)>=0:
    #             t+=g2.poids(x,y)
    #             #print(x,y)
    #         y=x
    #     #print("s:",t)
    somme.append(t)
    #     #mem[str(g2.vertices())] = t

print(int(min(somme)))
    
print("--- %s seconds ---" % (time.time() - start_time))