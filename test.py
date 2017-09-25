# Recursive Best First Search (Figure 3.26, Russell and Norvig)
#  Recursive Iterative Deepening form of A*, where depth is replaced by f(n)
import time
class Node:
    def __init__(self, state, f=0, g=0 ,h=0):
        self.state = state
        self.f = f
        self.g = g
        self.h = h
    def __repr__(self):
        return "Node(" + repr(self.state) + ", f=" + repr(self.f) + \
               ", g=" + repr(self.g) + ", h=" + repr(self.h) + ")"

def aStarSearch(startState, actionsF, takeActionF, goalTestF, hF):
    h = hF(startState)
    startNode = Node(state=startState, f=0+h, g=0, h=h)
    return aStarSearchHelper(startNode, actionsF, takeActionF, goalTestF, hF, 5)

# Global variable declaration



def aStarSearchHelper(parentNode, actionsF, takeActionF, goalTestF, hF, fmax):
	#time.sleep(0.2)
	#print(parentNode)
	if goalTestF(parentNode.state):
		return ([parentNode.state], parentNode.g)
	## Construct list of children nodes with f, g, and h values
	actions = actionsF(parentNode.state)
	if not actions:
	    return ("failure", float('inf'))
	children = []
	for action in actions:
	    (childState,stepCost) = takeActionF(parentNode.state, action)
	    h = hF(childState)
	    g = parentNode.g + stepCost
	    f = max(h+g, parentNode.f)
	    childNode = Node(state=childState, f=f, g=g, h=h)
	    children.append(childNode)
	    #print(children)
	comb = []
	while True:
	    # find best child
	    #print(children)
	    children.sort(key = lambda n: n.f) # sort by f value
	    #if children in comb:
	    #    return ("nope", float('inf'))
	    #comb.append(children)
	    # If f values of all children become fmax, then break.
	    '''
	    flag = 0
	    for c in children:
	        if c.f != float('inf'):
	            flag = 1
	    if flag == 0:
	        return ("Not found", float('inf'))
		'''
	    bestChild = children[0]
	    if bestChild.f > fmax:
	        return ("failure",bestChild.f)
	    # next lowest f value
	    alternativef = children[1].f if len(children) > 1 else float('inf')
	    # expand best child, reassign its f value to be returned value
	    result,bestChild.f = aStarSearchHelper(bestChild, actionsF, takeActionF, goalTestF, hF, min(fmax,alternativef))
	    if result is not "failure" and result is not "Not found":               
	        result.insert(0,parentNode.state)     
	        return (result, bestChild.f)
						                           
if __name__ == "__main__":                          
                                                 
    successors = {'a': ['b','c'],                 
                  'b': ['d','e'],                       
                  'c': ['f'],                     
                  'd': ['g', 'h'],                
                  'f': ['i','j']} 

    successors2 = {'a': ['b', 'c'],
    			  'c': ['a', 'd'],
    			  'd': ['c'] }

    successors3 = {'a': ['b','c'],                 
                  'b': ['d','e'],                       
                  'c': ['f', 'a'],                     
                  'd': ['g', 'h'],                
                  'f': ['i','j']} 

    def actionsF(s):                               
        try:                                      
            ## step cost of each action is 1
            return [(succ,1) for succ in successors[s]]
        except KeyError:
            return []
    def takeActionF(s,a):
        return a
    def goalTestF(s):
        return s == goal
    def h1(s):
        return 0
    start = 'a'
    goal = 'l'
    result = aStarSearch(start,actionsF,takeActionF,goalTestF,h1)
    #print('Path from a to g is', result[0], 'for a cost of', result[1])
    print(result)