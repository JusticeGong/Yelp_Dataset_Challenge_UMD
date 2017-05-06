def strtoint(s):
	return abs(hash(s)) % (10 * 8)

