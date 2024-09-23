import heapq
import queue
import numpy as np
from VALID_MOVES import valid_moves

def H_score(node, goal, n):
	'''
	Fill in this function to return the heuristic value of the current node.

	Compute heuristic as the Manhattan distance between the 
	current node and the goal state, divided by 
	the largest possible jump value.

	n is the dimensionality of the maze (n x n).

	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''

	nodex, nodey = node
	goalx, goaly = goal
	heuristic = ((abs(nodex - goalx) + abs(nodey - goaly)) / n - 1)

	return heuristic


def ASTAR(maze, start, goal):
	'''
	Fill in this function that uses A* search to find the shortest 
	path using the heuristic function H_score defined above.

	Return the length of the shortest path from the start state 
	to the goal state, and the path itself.

	Your return statement should be of the form:
	return len(path)-1, path

	where path is a list of tuples, corresponding to the 
	path and includes the start state.

	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''
	# I used edureka.co/blog/a-search-algorithm/ in order to 
	# understand the A* algorithm better in general 
	pq = []
	
	visited = set()
	
	heapq.heappush(pq, (H_score(start, goal, len(maze)), 0, (start, ())))
	while (pq):
		h, c, (v, path) = heapq.heappop(pq)
		if v not in visited:
			visited.add(v) 
			path = path + (v, ) 
			if v == goal:       
				return (len(path)-1, (path))   
			for w in valid_moves(maze, v):
				if w not in visited:
					g = c + 1
					heapq.heappush(pq, (g + H_score(w, goal, len(maze)), g, (w, path)))
					visited.add(v)
					
	return (len(path)-1, (path))




