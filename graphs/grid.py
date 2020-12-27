class grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.neighborsPlus
    
    def vertices(self):
        v = []
        for i in range(self.width):
            for j in range(self.height):
                v.append((i,j))
        return v
    def n(self):
        return self.width*self.height
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    def cost(self, x, y):
        return 1
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]#, (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)
        if (x + y) % 2 == 0: results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

def gridCoordonne(w,h,chaine, mur):
    g=[]
    for i, s in enumerate(chaine):
        for j in range(w):
            if s[j] == mur:
                g.append((j,i))
    return g

def modifCase(coord, char):
	global lines
	lines[coord[1]][coord[0]] = char

def getCase(coord):
	return lines[coord[1]][coord[0]]
def listToGrid(liste,mur):
	w = len(liste[0])
	h = len(liste)
	g=grid(w,h)
	g.wall = gridCoordonne(w,h,liste,mur)
	return g
