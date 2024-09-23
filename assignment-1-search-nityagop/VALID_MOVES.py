def valid_moves(maze, node):
	'''
	Fill in this function to return a list of "valid" neighbors 
	for the current node in the rook-jumping-maze.
	
	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''
	neighbors=[]
	row, col = node

	if row - maze[row][col] >= 0:
		neighbors.append((row - maze[row][col], col))
	if row + maze[row][col] < len(maze):
		neighbors.append((row + maze[row][col], col))
	if col - maze[row][col] >= 0:
		neighbors.append((row, col - maze[row][col]))
	if col + maze[row][col] < len(maze[0]):
		neighbors.append((row, col + maze[row][col]))
	
	return neighbors


