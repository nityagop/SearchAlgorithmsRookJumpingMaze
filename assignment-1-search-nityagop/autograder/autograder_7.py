import numpy as np
import sys

sys.path.append('./')
sys.path.append('../')

from ASTAR import ASTAR
from BFS import BFS
from HILLDESCENT import energyfunction
from SIMULATED_ANNEALING import SIMULATED_ANNEALING

'''
MAKE ABSOLUTELY NO CHANGES TO THIS FILE OR YOUR CODE WILL FAIL THE AUTOGRADER.

Evaluates Simulated Annealing search against test inputs.
'''

lines = list(sys.stdin)

i=0

while i<len(lines):
	k=int(lines[i].rstrip('\n'))
	maze=np.zeros((k,k),dtype=int)
	for j in range(i+1,i+k+1):
		maze[j-i-1]=np.fromstring(lines[j].rstrip('\n'), sep=",", dtype=int)
	start=tuple(int(x) for x in lines[i+k+1].rstrip('\n').split(','))
	goal=tuple(int(x) for x in lines[i+k+2].rstrip('\n').split(','))
	i=i+k+3
	
	energy = energyfunction(maze, start, goal)

	print(energy >= SIMULATED_ANNEALING(maze,start,goal,500,1000,0.9855)[1])
