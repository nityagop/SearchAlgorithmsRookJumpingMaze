import random
import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR
from HILLDESCENT import energyfunction
from VALID_MOVES import valid_moves

def SIMULATED_ANNEALING(maze, start_cell, goal_state, iterations, T, decay):

	'''
	Fill in this function to implement Simulated Annealing.

	The energy function is the same as used for Hill Descent
	and is already imported here for it to be used directly
	(see the energyfunction() function in HILLDESCENT.py).

	With an input temperature 'T' and a decay rate 'decay',
	you should run the algorithm for 'iterations' steps.

	At each step, you should randomly select a valid move,
	and move to that state with probability 1 if the energy
	of the new state is less than the energy of the current state,
	or with probability exp((current_energy - new_energy)/T)
	if the energy of the new state is greater than the current energy.

	After each step, decrease the temperature by 
	multiplying it by the decay rate.

	Your function should return the best solution found,
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''
	# I used chatGPT to solve a NoneType error that was occuring 
	# when generating the neighbors 

	# I also used chatGPT to figure out how to generate 
	# the probability number 
	original_maze = maze.copy()
	current = start_cell
	current_energy = energyfunction(maze, start_cell, goal_state)
	best_solution = (original_maze, current_energy)
		
	for i in range(iterations):
		neighbors = valid_moves(maze, current)
		probability = np.random.uniform(0.0, 1.0, size=None)
		if (len(neighbors) >= 1):
			neighbor = random.choice(neighbors)
		else:
			return (best_solution, energyfunction(maze, current, goal_state))
		
		random_jump_val = random.randint(1, len(maze) - 1)
		current_val = (random.randint(0, len(maze) - 1), random.randint(0, len(maze) - 1))

		if(original_maze[current_val] != 0):
			cell = original_maze[current_val]
			original_maze[current_val] = random_jump_val
		
		if energyfunction(maze, neighbor, goal_state) <= energyfunction(maze, current, goal_state):
			current = neighbor
			current_energy = energyfunction(maze, neighbor, goal_state)
			best_solution = neighbor
			probability = 1
		else:
			if probability < np.exp((current_energy - energyfunction(maze, neighbor, goal_state))/T):
				start_cell = current_val
				current_energy =  energyfunction(maze, neighbor, goal_state)
				
			T = T * decay
		
		return (best_solution, energyfunction(maze, current, goal_state))

