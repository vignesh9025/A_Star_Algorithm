def ebf(nNodes, depth, precision = 0.000001):
	left = 1
	right = nNodes
	if nNodes == 0:
		return 0
	b = 1
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

def depthLimitedSearch(state, goalState, actionsF, takeActionF, depthLimit):
    
    # IF THE GOAL STATE IS FOUND, RETURN EMPTY LIST
    if state == goalState:
        return []
    
    # IF DEPTH LIMIT HAS BEEN REACHED, AND THE GOAL HASN'T BEEN FOUND YET, RETURN THE STRING 'CUTOFF'
    if depthLimit == 0:
        return 'cutoff'
    
    # A FLAG VARIABLE TO KEEP CHECK OF WHETHER CUTOFF HAS OCCURED
    cutoffOccurred = False
    
    # HERE WE USE THE actionsF FUNCTION TO OBTAIN THE POSSIBLE ACTIONS WE CAN APPLY ON 'state'. WE ITERATE THROUGH EACH ACTION
    for action in actionsF(state):
        
        # THEN, WE GENERATE CHILD NODE FOR action USING THE takeActionF FUNCTION
        childState, _ = takeActionF(state, action)
        
        # THE depthLimitedSearch FUNCTION IS RECURSIVELY CALLED, WITH THE NEWLY GENERATED childState AS THE state PARAMETER.
        # WE ALSO PASS depthLimit DECREMENTED BY ONE SO THAT WE KEEP TRACK OF HOW MANY LEVELS DEEP WE ARE IN THE TREE.
        result = depthLimitedSearch(childState, goalState, actionsF, takeActionF, depthLimit - 1)
        
        # IF cutoff IS RETURNED, THEN THE ALGORITHM COULDN'T FIND THE GOAL AT THE CURRENT DEPTH LIMIT. THE FLAG VARIABLE IS 
        # CHANGED TO True TO REFLECT THIS.
        if result == 'cutoff':
            cutoffOccurred = True
            
        
        elif result != 'failure':
            # ONCE WE GET TO THIS POINT PAST ALL THE ABOVE CONDITIONALS, THE GOAL HAS BEEN DISCOVERED, AND WE BEGIN BUILDING 
            # THE SOLUTION PATH. WE INSERT THE CHILD STATE TO THE FRONT OF THE PARTIAL SOLUTION PATH AND RETURN IT.
            # result KEEPS GETTING FILLED WITH THE STATES OF THE SOLUTION PATH AS IT GOES UP THE FUNCTION CALL STACK, TILL THE 
            # COMPLETE SOLUTION PATH IS RETURNED.
            result.insert(0, childState)
            return result 
    if cutoffOccurred:
        return 'cutoff' # RETURN 'cutoff' IF NO GOAL COULD BE FOUND WITHIN depthLimit
    else:
        return 'failure' # RETURN 'failure' IF NO GOAL STATE COULD BE FOUND IN THE ENTIRE SEARCH-TREE

# IN THIS FUNCTION, WE ITERATE THROUGH ALL POSSIBLE depth VALUES WITHIN THE MAXIMUM DEPTH, AND CALL depthLimitedSearch 
# FOR EACH ITERATION
def iterativeDeepeningSearch(startState, goalState, actionsF, takeActionF, maxDepth):
    # ITERATING THROUGH DEPTH VALUES
    for depth in range(maxDepth):
        # CALLING depthLimitedSearch FOR EACH DEPTH VALUE
        result = depthLimitedSearch(startState, goalState, actionsF, takeActionF, depth)
        if result == 'failure':
            return 'failure'
        if result != 'cutoff':
            # IF A GOAL EXISTS, THEN INSERT THE STARTING STATE TO THE FRONT OF SOLUTION PATH AND RETURN IT.
            result.insert(0, startState)
            return result
    return 'cutoff'


def printPath_8p(startState, goalState, path):
    
    if path == 'cutoff' or path == 'failure':
        print(path)
    else:
        # FIND PATH LENGTH
        l = len(path)
        #print("The path from %s to %s is %d nodes long." % (printState_8p(startState), printState_8p(goalState), l))
        print("The path from \n")
        printState_8p(startState)
        print("\nto\n")
        printState_8p(goalState)
        print("\nis %d nodes long." % l)
        print()
        print()
        for p in path:
            printState_8p(p)
            print()

def printState_8p(state):
    ctr = 0
    # PRINTING THE ELEMENTS OF THE STATE IN A READABLE, 2-DIMENSIONAL FORMAT
    for i in range(3):
        for j in range(3):
            if state[ctr] == 0:
                print(' ', end = ' ')
            else:
                print(state[ctr], end=' ')
            ctr += 1
        print()

# THIS FUNCTION TAKES IN X INDEX AND Y INDEX VALUES, AND RETURNS THE SIMPLE-LIST INDEX

def matrix_to_list_8p(x, y):
    counter = 0
    for i in range(3): # SINCE IT'S A 3 X 3 PUZZLE
        for j in range(3):
            if i == x and j == y:
                return counter
            counter += 1
    return 'Index does not exist!'

# FUNCTION WHICH TAKES IN A SIMPLE-LIST INDEX AND RETURNS X, Y VALUES

def list_to_matrix_8p(x):
    counter = 0
    for i in range(3):
        for j in range(3):
            if counter == x:
                return i, j # RETURNS A TUPLE CONTAINING X AND Y INDEX VALUES
            counter += 1
    return 'Index does not exist!'

# FUNCTION TO SWAP TWO POSITIONS IN A 2D MATRIX

def swap(state, x1, y1, x2, y2):
    temp = state[matrix_to_list_8p(x1, y1)] # ASSIGN FIRST INDEX VALUE TO TEMPORARY VARIABLE
    state[matrix_to_list_8p(x1, y1)] = state[matrix_to_list_8p(x2, y2)] # ASSIGN SECOND INDEX VALUE TO FIRST POSITION
    state[matrix_to_list_8p(x2, y2)] = temp # ASSIGN TEMPORARY VARIABLE'S VALUE TO SECOND POSITION
    return state

# FUNCTION TO FIND THE BLANK IN A GIVEN STATE

def findBlank_8p(state):
    ctr = 0
    for i in state: # ITERATE THROUGH 'STATE' LIST AND ONCE BLANK IS FOUND, RETURN IT'S 2-DIMENSIONAL INDEX.
        if i == 0:
            return list_to_matrix_8p(ctr)
        ctr += 1
    return 'Blank not found!'

# THE ACTIONSF FUNCTION GENERATES ALL POSSIBLE VALID ACTIONS FROM A GIVEN STATE.

def actionsF_8p(state):

    # FIRSTLY, WE DETERMINE WHERE THE BLANK IS LOCATED
    blank = findBlank_8p(state)
    
    # LET'S INITIALIZE THE VALID ACTIONS LIST
    validActions = []

    # NOW WE USE A SET OF CONDITIONALS AND KEEP APPENDING TO validActions
    
    # FOR GOING LEFT, CONDITION IS (Y != 0)
    if blank[1] != 0:
        validActions.append(('left', 1))
    # FOR GOING RIGHT, CONDITION IS (Y != 2)
    if blank[1] != 2:
        validActions.append(('right', 1))
    # FOR GOING UP, CONDITION IS (X != 0)
    if blank[0] != 0:
        validActions.append(('up', 1))
    # FOR GOING DOWN, CONDITION IS (X != 2)
    if blank[0] != 2:
        validActions.append(('down', 1))

    return validActions

# This function takes in a state and an action, and applies this action to the state. Returns the new state and a step cost to get to state (1).
import copy
def takeActionF_8p(state, action):
    # DETERMINE BLANK LOCATION
    blank = findBlank_8p(state)
    state2 = copy.copy(state)
    # MOVING LEFT - SWAP BLANK WITH ELEMENT TO THE LEFT.
    if action[0] == 'left':
        swap(state2, blank[0], blank[1], blank[0], blank[1] - 1)

    # MOVING RIGHT - SWAP BLANK WITH ELEMENT TO THE RIGHT.
    if action[0] == 'right':
        swap(state2, blank[0], blank[1], blank[0], blank[1] + 1)

    # MOVING UP - SWAP BLANK WITH ELEMENT ABOVE.
    if action[0] == 'up':
        swap(state2, blank[0], blank[1], blank[0] - 1, blank[1])

    # MOVING DOWN - SWAP BLANK WITH ELEMENT BELOW.
    if action[0] == 'down':
        swap(state2, blank[0], blank[1], blank[0] + 1, blank[1])

    return state2, 1

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
    return aStarSearchHelper(startNode, actionsF, takeActionF, goalTestF, hF, float('inf'))

def aStarSearchHelper(parentNode, actionsF, takeActionF, goalTestF, hF, fmax):
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
    while True:
        # find best child
        children.sort(key = lambda n: n.f) # sort by f value
        bestChild = children[0]
        if bestChild.f > fmax:
            return ("failure",bestChild.f)
        # next lowest f value
        alternativef = children[1].f if len(children) > 1 else float('inf')
        # expand best child, reassign its f value to be returned value
        result,bestChild.f = aStarSearchHelper(bestChild, actionsF, takeActionF, goalTestF,
                                            hF, min(fmax,alternativef))
        if result is not "failure":             
            result.insert(0,parentNode.state)     
            return (result, bestChild.f)

# H1 - Heuristic function definition
def hf(state, goalState):
	return 0

# H2 - Heuristic function which computes the Manhattan distance of the blank
def hf2(state, goalState):
	x1, y1 = findBlank_8p(state)
	x2, y2 = findBlank_8p(goalState)
	x = abs(x1 - x2)
	y = abs(y1 - y2)
	return x + y

# H3 - Actual Manhattan distance
def hf3(state, goalState):
	dist = 0
	for i in range(9):
		if state[i] == 0:
			continue
		# Find element at position i in state
		element = state[i]
		# Find x and y of this element
		x1, y1 = list_to_matrix_8p(i)
		# Index of same element in goalState
		xg, yg = list_to_matrix_8p(goalState.index(element))
		# Compute sum
		x = abs(x1 - xg)
		y = abs(y1 - yg)
		#print(x, y)
		s = x + y
		#print(s)
		dist = s + dist
	return dist

#startState = [2,1,3,5,4,0,6,7,8]
#goalState = [1,2,3,4,5,6,7,8,0]

#startState = [1,2,3,4,0,5,6,7,8]
#goalState = [3,5,0,2,1,8,4,7,6]
#startState = [1,2,3,4,5,0,6,7,8]
#goalState = [0,2,3,4,5,1,6,7,8]

#def runExperiment(goalState1, goalState2, goalState3, [h1, h2, h3]):


#print(aStarSearch(startState, actionsF_8p, takeActionF_8p, goalTestF, lambda s: hf2(s, [1,0,3,4,5,8,2,6,7])))
#print(aStarSearch(startState, actionsF_8p, takeActionF_8p, goalTestF, hf))
#print(actionsF_8p(startState))
#print(takeActionF_8p([1, 2, 3, 4, 5, 6, 7, 0, 8], ('up', 1)))
#print(hf3(startState, goalState))
#print(iterativeDeepeningSearch(startState, goalState, actionsF_8p, takeActionF_8p, 20))

# 1 + b + b^2 + ... + b^d

# Note to self: depth = number of nodes in sol path, for nodes, use global var
import pandas as pd 
import numpy as np 
from tabulate import tabulate

# GLOBAL !!! -------GLOBAL !!! -------GLOBAL !!! -------GLOBAL !!! -------GLOBAL !!! -------GLOBAL !!! -------
nodes = 0
# GLOBAL !!! -------GLOBAL !!! -------GLOBAL !!! -------GLOBAL !!! -------GLOBAL !!! -------GLOBAL !!! -------



def runExperiment(goalState1, goalState2, goalState3):
	n2 = np.array([['IDS', ' ', ''],
				  ['A*h1', ' ', ''],
				  ['A*h2', ' ', ''],
				  ['A*h3', ' ', '']])

	p = pd.DataFrame(n2, index = ['', '', '', ''], columns = ['Algorithm', '', ''])
	#p = p.to_string(header = False)
	startState = [1,2,3,4,0,5,6,7,8]
	goalStateList = [goalState1, goalState2, goalState3]
	r2 = ['Depth', 'Nodes', 'EBF', ' ']
	l = pd.DataFrame()
	print(p)
	for goalState in goalStateList:
		r3 = []
		r4 = []
		r5 = []
		r6 = []
		ids = iterativeDeepeningSearch(startState, goalState, actionsF_8p, takeActionF_8p, 20)
		dids = len(ids)
		n = nodes
		ebfids = ebf(n, dids)
		r3.append(dids)
		r3.append(n)
		r3.append(ebfids)
		r3.append(' ')

		ah1 = aStarSearch(startState, actionsF_8p, takeActionF_8p, lambda s: goalTestF_8p(s, goalState), lambda s: hf(s, goalState))
		d1 = len(ah1)
		n1 = nodes
		ebf1 = ebf(n1, d1)
		r4.append(d1)
		r4.append(n1)
		r4.append(ebf1)
		r4.append(' ')

		ah2 = aStarSearch(startState, actionsF_8p, takeActionF_8p, lambda s: goalTestF_8p(s, goalState), lambda s: hf2(s, goalState))
		d2 = len(ah2)
		n2 = nodes
		ebf2 = ebf(n2, d2)
		r5.append(d2)
		r5.append(n2)
		r5.append(ebf2)
		r5.append(' ')


		ah3 = aStarSearch(startState, actionsF_8p, takeActionF_8p, lambda s: goalTestF_8p(s, goalState), lambda s: hf3(s, goalState))
		d3 = len(ah3)
		n3 = nodes
		ebf3 = ebf(n3, d3)
		r6.append(d3)
		r6.append(n3)
		r6.append(ebf3)
		r6.append(' ')

		nu = np.array([r3,r4,r5,r6])
		un = pd.DataFrame(nu, columns = r2)
		print(un.to_string(index = False, justify = 'center'))
		#pd.concat([p,un], axis = 1)
		#ld = pd.concat([ld,un], axis = 1)


def goalTestF_8p(state, goalState):
	return state == goalState


if __name__ == "__main__":
	goalState1 = [1,2,3,4,0,5,6,7,8]
	goalState2 = [1,2,3,4,5,8,6,0,7]
	#goalState3 = [1,0,3,4,5,8,2,6,7]
	goalState3 = [1,2,3,4,0,5,6,7,8]
	startState = [1,2,3,4,0,5,6,7,8]

	runExperiment(goalState1, goalState2, goalState3)

	#print(aStarSearch(startState, actionsF_8p, takeActionF_8p, lambda s: goalTestF_8p(s, goalState1), lambda s: hf(s, goalState1)))









	






                                                  
