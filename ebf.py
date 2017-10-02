# 1 + b + b^2 + ... + b^d

def ebf(nNodes, depth, precision = 0.000001):
	left = 1
	right = nNodes
	if nNodes == 0:
		return 0
	b = 1.0
	while(True):
		if abs(right - left) <= precision:
			break
		#print('left', left)
		#print('right', right)
		b = (left + right)/2
		#print('b', b)
		n = (pow(b, (depth+1)) - 1)/(b - 1)
		if nNodes < n:
			right = b - precision
		elif nNodes > n:
			left = b + precision
		else:
			return b
	return b

print(ebf(1, 0))

