#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys


def sortT(l, i):
    return sorted(l, reverse=True, key=lambda tup: tup[i])

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
	return [tuple(splitT(e)) for e in l]

lines=[(1, 1, 10), (919, 2), (19, 10)]
f = lines.pop(0)

pis = lines[:f[0]]
pos = lines[f[1]:]
lines = sortT(pos, 0) + pis

n = f[0] + f[1]
c = f[2]


def sac(n,cap, l, mem, f):
    print("cap :: " ,cap, n)
    if n == 0 or cap == 0:
        return 0
    if n<=f:
        print("ok :: ", cap, n, f)
        qte = min(cap, l[n-1][1])
        res =  sac(n-1, cap-qte, l, mem, f) +qte * l[n-1][0]
        mem[n-1][cap-1] = res
        return res
    if mem[n-1][cap-1] != -1:
        return mem[n-1][cap-1]
    print(n, l, l[n-1])
    
    if l[n-1][1] > cap:
        return sac(n-1, c, l,mem, f)


    a = sac(n-1, cap, l, mem, f)
    b = sac(n-1, cap-l[n-1][1], l, mem, f) +l[n-1][0]
    m = max(a,b)
    mem[n-1][cap-1] = m
    return m

mem = [[-1] * c for i in range(n)]
print(lines)
valMax = sac(n, c, lines, mem, f[1])

print(valMax)
print("coucou")
