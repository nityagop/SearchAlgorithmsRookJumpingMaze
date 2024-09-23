from collections import deque
from queue import Queue
import numpy as np
from VALID_MOVES import valid_moves

def BFS(maze, start):
    
    '''
    Fill in this function that uses Breadth First Search to find the shortest path 
    from the start state to the goal state.
    
    Return the matrix (a 2-dimensional numpy array) of shortest path 
    distances from the start cell to each cell. 
    
    If no path exists from the start state to a given cell, that cell should be assigned -1.
    
    The start state should be assigned a path lenght of 0.
    
    If using print statements to debug, please make sure 
    to remove them before your final submisison.
    

    '''
    # I used chatGPT to fix some of the errors in the 
    # autograder 
    rows, cols = maze.shape
    queue = Queue()
    visited = []
    path_matrix = np.full((rows, cols), -1, dtype=int)

    queue.put((start, 0))  
    path_matrix[start[0]][start[1]] = 0 
    visited.append(start)
    while not queue.empty():
        v, distance = queue.get()
        
        for w in valid_moves(maze, v):
            if w not in visited:
                queue.put((w, distance + 1)) 
                visited.append(w)
                path_matrix[w[0]][w[1]] = distance + 1  

    return path_matrix

    



