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
sys.stderr.write(str(lines))

f = lines.pop(0)

