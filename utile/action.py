def sortT(l, i):
    return sorted(l, key=lambda tup: tup[i])

import itertools
def touteComb(l):
    res = []
    for i in range(len(l)+1):
        res += list(itertools.permutations(l, i))
    return res
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def is_subseq(x, y):
    it = iter(y)
    return all(any(c == ch for c in it) for ch in x)


def distance (t1,t2):
    s=0
    for i in range(len(t1)):
        s+=(t1[i] - t2[i])**2
    return math.sqrt(s)

def supList(l,i):
    return l[:i] + l[i+1:]

zip(T[:-1],T[1:])

import sys
sys.setrecursionlimit(10000)

from functools import lru_cache
@lru_cache(maxsize=None)
