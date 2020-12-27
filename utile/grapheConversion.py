def adjToDict(l):
    for e in l:
        dictelt = {}
        for elt in l[e]:
            dictelt[elt] = 1
        l[e] = dictelt
    return l



def dictToAdjListe(d):
    l={}
    for k,v in d.items():
        l1=[]
        for f in v:
            l1.append(f)
        l[k] = l1
    return l

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


#----------matrix-------------

def graphToFlow(g):
    m=[]
    #print(m)
    vertices = g.vertices()
    for v in range(g.n()):
        m.append([0]*g.n())
        #print(m)
    for i,v in enumerate(vertices):
        neighbors = g.neighbors(v)
        for n in neighbors:
            m[i][vertices.index(n)] = (g.cost(v,n))
    return m

def listeToFlow(l, taille):
    m=[]
    #print(m)
    for _ in range(taille):
        m.append([0]*taille)
    for e in l:
        m[e[0]][e[1]] = e[2]
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
print(dictToAdjListe(g))