import copy
# This function must return the possible actions (a.k.a. the children). Each child should be returned along with it's f = hf + gf.
def successorsf(state):
	# Now, we compute the 'f' value using the FindF function, for each child node returned by 'successorsf'.
	# The 'f' values are joined to each child node in the form of (child, f) tuples, in c.
	children = copy.copy(successors.get(state, []))
	c =[]
	for child in children:
		f = findF(child)
		c.append((child, f))
	return c
