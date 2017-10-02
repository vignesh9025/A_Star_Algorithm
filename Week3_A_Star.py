# Define search tree
successors2 = { 'a': ['b','c','d'],
			   'b': ['e','f'],
			   'c': ['g','h'],
			   'd': ['i'],
			   'f': ['j'],
			   'j': ['z'],
			   'i': ['z'] }

successors = { 'a': ['b','c','d'],
			   'b': ['e','f'],
			   'c': ['g','h','a'],
			   'd': ['i'],
			   'f': ['b', 'j'],
			   'j': ['z'],
			   'i': ['z'] }

# Successors function
import copy
def successorsf(state):
    return copy.copy(successors.get(state, []))

# Define Node class
class Node:
	# The node class will contain the data items 'state', f, g, and h.
	def __init__(self, state, f=0, g=0, h=0):
		self.state = state
		self.f = f
		self.g = g
		self.h = h

	# The __repr__ function can be overridden to put in our own code to print the node in a readable format.
	def __repr__(self):
		return "Node(" + repr(self.state) + ", f=" + repr(self.f) + ", g=" + repr(self.g) + ", h=" + repr(self.h) + ")"

	def __lt__(self, other):
		return self.f > other.f

# Define hf (for testing)
def hf(state):
	h = 0
	return h
	if state == 'd':
		h = 2
	if state == 'c':
		h = 1
	if state == 'b':
		h = 3
	if h:
		return h
	return 10
	


# DFS 
def astar(startState, goalState, successorsf):
    
    # We firstly initialize expanded to an empty dictionary and 
    # unExpanded to be a list containing the tuple (startState, 'None'), which refers to the root node.
	expanded = {}
	h = hf(startState)
	g = 0
	f = g + h
	startNode = Node(state = startState, f=f, g=g, h=h)
	unExpanded = [(startNode, 'None')]

	# Next, we check if the goal specified is the same as the root node, in which case, the root node (*startState*) 
	# is returned as a list.

	#if not successorsf(startState):
	#    return 'No nodes are present'

	if(startState == goalState):
	    return [startState, startNode.f]

	# Then we begin iterating through *unExpanded* while it's not empty. This is done with a while loop.

	while(unExpanded):
		#print("unExpanded (before): ", unExpanded)
		statePair = unExpanded.pop()
		#print("unExpanded (after): ", unExpanded)
		# Add to expanded
		expanded[statePair[0]] = statePair[1]
		state = statePair[0]
		print("State: ", state)
		# Obtain children of state

		children = successorsf(state.state)
		childNodes = []

		# Remove children already present
		unexp = []
		for tup in unExpanded:
			unexp.append(tup[0])
		exp = list(expanded.keys())
		for x in exp:
			if x.state in children:
				children.remove(x.state)
		for x in unexp:
			if x.state in children:
				children.remove(x.state)

		# Create child node classes for each child. Compute the parameters for each child and add the to a list.
		for child in children:
			if child == goalState:
				solPath = [goalState, state.state]
				while(expanded[state] != 'None'):
					parentNew = expanded[state]
					solPath.append(parentNew.state)
					state = parentNew
				solPath.reverse()
				return solPath

			h = hf(child)
			g = state.g + 1 # Assuming step cost is 1
			f = g + h
			childNode = Node(state = child, f=f, g=g, h=h)
			childNodes.append(childNode)

		# Sort child nodes in descending order of f values.
		#childNodes.sort()

		# Append child nodes in unExpanded
		for c in childNodes:
			unExpanded.append((c, state))

		# Sort unExpanded in descending order
		unExpanded.sort(key = lambda x: -x[0].f)
	return "No goal"


if __name__ == '__main__':
	# test code
	print(astar('a', 'z', successorsf))
	

