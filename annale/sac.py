#(val, poids)
def sac(n,cap, l, mem):
    if mem[n-1][cap-1] != -1:
        return mem[n-1][cap-1]
    if n == 0 or cap == 0:
        return 0
    if l[n-1][1] > cap:
        return sac(n-1, cap, l,mem)
    a = sac(n-1, cap, l, mem)
    b = sac(n-1, cap+l[n-1][1], l, mem) +1
    m = max(a,b)
    mem[n-1][cap-1] = m
    return m

mem = [[-1] * c for i in range(n)]
valMax = sac(n-1, c, lines, mem)
#a test (normallement ok)
