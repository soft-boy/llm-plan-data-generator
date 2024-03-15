
import numpy as np

maze=[
    ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
    ['^', 'S', '*', '*', '*', '*', '^', '^', '*', '^'],
    ['^', '^', '*', '*', '^', '*', '*', '*', '*', '^'],
    ['^', '*', '*', '^', '*', '^', '*', '^', '*', '^'],
    ['^', '*', '*', '*', '*', '^', '*', '*', '*', '^'],
    ['^', '*', '*', '*', '*', '*', '*', '^', '^', '^'],
    ['^', '*', '*', '^', '*', '^', '*', '*', '^', '^'],
    ['^', '*', '*', '*', '*', '*', '*', '^', 'H', '^'],
    ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
]

def value_iteration(maze, gamma=0.9):
    rows = len(maze)
    cols = len(maze[0])
    
    # Initialize the value function
    V = np.zeros((rows, cols))
    
    # Define actions:
    actions = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 2), (2, 0), (0, -2), (-2, 0)]
    
    # Helper function to check if a cell is valid to move into
    def is_valid_move(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] != '^'
    
    # Perform value iteration
    for i in range(1000):
        for i in range(rows):
            for j in range(cols):
                if maze[i][j] == 'H':
                    V[i][j] = 3
                    continue
                if maze[i][j] == '^':
                    continue  # Walls or obstacles have no value
                
                max_value = float('-inf')
                for action in actions:
                    new_i, new_j = i + action[0], j + action[1]
                    if is_valid_move(new_i, new_j):
                        max_value = max(max_value, V[new_i][new_j])
                V[i][j] = gamma * max_value
    
    return V

np.set_printoptions(precision=2)
print(value_iteration(maze))
