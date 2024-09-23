import random
import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR
from VALID_MOVES import valid_moves


def energyfunction(maze, start, goal):
	'''
	Compute the energy as the sum of the shortest path length 
	from the start state to the goal state (computed using A*)
	and the number of cells that are not reachable from the 
	start state (computed using BFS).

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''
	# I used chatGPT find the number of cells that are not reachable 
	energy =  (ASTAR(maze, start, goal)[0] + 1) + np.count_nonzero(BFS(maze, start) == -1)
	return energy



def HILLDESCENT(maze, start_cell, goal_state, iterations):
	'''
	Fill in this function to implement Hill Descent local search.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze 
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''
	# I used chatGPT to ask for an explanation of what the psuedocode 
	# in the notes meant 
	original_maze = maze.copy()
	current_energy = energyfunction(maze, start_cell, goal_state)
	best_solution = (original_maze, current_energy)

	for i in range(iterations):
		neighbors = valid_moves(maze, start_cell)
		
		if (len(neighbors) >= 1):
			neighbor = random.choice(neighbors)
		else:
			return (best_solution, current_energy)
		
		random_jump_val = random.randint(1, len(maze) - 1)
		current_val = (random.randint(0, len(maze) - 1), random.randint(0, len(maze) - 1))

		if(original_maze[current_val] != 0):
			original_maze[current_val] = random_jump_val
		
		if energyfunction(maze, neighbor, goal_state) <= current_energy:
			start_cell = current_val
			current_energy = energyfunction(maze, neighbor, goal_state)
			best_solution = neighbor
	return best_solution

	

def HILLDESCENT_RANDOM_RESTART(maze, start_cell, goal_state, iterations, num_searches):
	'''
	Fill in this function to implement Hill Descent local search with Random Restarts.

	For a given number of searches (num_searches), run hill descent search.

	Keep track of the best solution through all restarts, and return that.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze 
	before making any changes to it.

	You will also need to keep a separate copy of the original maze
	to use when restarting the algorithm each time.

	If using print statements to debug, please make sure
	to remove them before your final submisison.

	'''

	# I used chatGPT to understand the different between 
	# random restart and the normal hill descent 
	original_maze = maze.copy()
	current_energy = energyfunction(maze, start_cell, goal_state)
	best_solution = (original_maze, current_energy)
	for i in range(num_searches):
		for j in range(iterations):
			neighbors = valid_moves(maze, start_cell)
			
			if (len(neighbors) >= 1):
				neighbor = random.choice(neighbors)
			else:
				return (best_solution, current_energy)
			random_jump_val = random.randint(1, len(maze) - 1)
			current_val = (random.randint(0, len(maze) - 1), random.randint(0, len(maze) - 1))

			if(original_maze[current_val] != 0):
				original_maze[current_val] = random_jump_val
			
			if energyfunction(maze, neighbor, goal_state) <= current_energy:
				start_cell = current_val
				current_energy = energyfunction(maze, neighbor, goal_state)
				best_solution = neighbor

	return best_solution


def HILLDESCENT_RANDOM_UPHILL(maze, start_cell, goal_state, iterations, probability):
	'''
	Fill in this function to implement Hill Descent local search with Random uphill steps.

	At each iteration, with probability specified by the probability
	argument, allow the algorithm to move to a worse state.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''

	# I also used chatGPT to figure out how to generate 
	# the probability number 

	original_maze = maze.copy()
	current_energy = energyfunction(maze, start_cell, goal_state)
	best_solution = (original_maze, current_energy)

	for i in range(iterations):
		neighbors = valid_moves(maze, start_cell)
		
		if (len(neighbors) >= 1):
			neighbor = random.choice(neighbors)
		else:
			return best_solution
		
		random_jump_val = random.randint(1, len(maze) - 1)
		current_val = (random.randint(0, len(maze) - 1), random.randint(0, len(maze) - 1))

		if(original_maze[current_val] != 0):
			cell = original_maze[current_val]
			original_maze[current_val] = random_jump_val

			if energyfunction(maze, neighbor, goal_state) < current_energy:
				start_cell = current_val
				current_energy = energyfunction(maze, neighbor, goal_state)
			
			random_probablity = np.random.uniform(0.0, 1.0, size=None)
			if (random_probablity < probability):
				start_cell = current_val
				current_energy = energyfunction(maze, neighbor, goal_state)
			else:
				original_maze[current_val] = cell
	return best_solution
	
	



	








