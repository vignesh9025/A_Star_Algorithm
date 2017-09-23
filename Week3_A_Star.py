# ---------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------- A* Algorithm ------------------------------------------------------------------------------------------------
# ------------------------------- Author: Vignesh M. Pagadala ---------------------------------------------------------------------------------
# --------------------------------File: Week3_A_Star.py ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------

# To synthesize the Pythonic implementation of A*, we proceed from the same way we built the BFS and DFS functions. We do this by the iterative way first.
# Firstly, let's define the function.

successors = { a: ['b','c'],
			   b: ['d','e'],
			   c: ['f','g'],
			   d: ['i','j'],
			   f: ['g'],
			   j: ['g'] }

import copy
# This function must return the possible actions (a.k.a. the children). Each child should be returned along with it's f = hf + gf.
#E
def successorsf(state):
	
	return copy.copy(successors.get((state, f), []))

def hf(state):
	return 0

def findF(children):
	h = hf(state)
	g = gf(state)
	f = g + h
	return f


def gf(state):
	g = 0;
	kys = successors.keys()

	for i in kys:
		



def AStarSearch(startState, goalState, successorsf, hf):
	if startState == goalState:
		return startState

	unExpanded = [(startState, None)]
	expanded = {}

	while(unExpanded):
		state = unExpanded.pop()
		children = successorsf(state)

















