#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:51:52 2020

@author: kangourou
"""


def poidsChemin(g,chemin):
    s=0
    for i in range(1, len(chemin)):
        s+=g.poids(i-1, i)
    return s

#Format : [ ((x,y), poids), (...]
def arcVal(l):
    return [(e,1) for e in l]
def addPlusArc(g, l):
    for e in l:
        g.addArc(e[0][0], e[0][1], e[1])

def addPlusArrete(g, l):
    for e in l:
        g.addArrete(e[0][0], e[0][1], e[1])

#Format : [ (x,y), (...]
def delPlusArc(g, l):
    for e in l:
        g.delArc(e[0], e[1])

def delPlusArrete(g, l):
    for e in l:
        g.delArrete(e[0], e[1])
        
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

def maxInDict(d):
	for e in d.values():
	    for i in e.values():
		if i!=float("inf"):
		    m.append(i)



from ford_fulkerson import *
from structure import *
from edmonds_karp_multiple_source_and_sink import *
g = { "a" : {"d":[2]},
      "b" : {"c":[1]},
      "c" : {"b":[3], "c":[1], "d":[1], "e":[1]},
      "d" : {"a":[1], "c":[1]},
      "e" : {"c":[1], "a":[12]},
    }

graph = Graph(g)

#graph.addArc("yx", "xiue")
#graph.delArrete("a","d")
print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

print( graphToFlow(graph))
#print(graph.n())

flowNetwork = FlowNetwork(graph, ["b", "d"], ["a"])
# set algorithm
flowNetwork.setMaximumFlowAlgorithm(PushRelabelExecutor)
# and calculate
f = flowNetwork.findMaximumFlow()

print("flot: ",f)
