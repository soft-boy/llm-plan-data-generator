import random
from x_template import writeXDatum
from y_template import writeYDatum
from maze_options import get_random_option

def generate_maze(width, height, agent, goal, wall, empty, **args):
    # Create an empty grid
    maze = [[empty for _ in range(width)] for _ in range(height)]
    
    # Set walls around the perimeter
    for x in range(width):
        maze[0][x] = wall
        maze[height-1][x] = wall
    for y in range(height):
        maze[y][0] = wall
        maze[y][width-1] = wall
        
    # Place the agent in the upper left corner (excluding the wall)
    maze[1][1] = agent
    
    # Place the goal in the lower right corner (excluding the wall)
    maze[height-2][width-2] = goal
    
    # Randomly place additional walls inside the maze, if desired
    for _ in range(int((width * height) * 0.2)):  # Adjust the 0.2 value to add more or fewer walls
        x, y = random.randint(1, width-2), random.randint(1, height-2)
        if maze[y][x] == empty:
            maze[y][x] = wall

    return maze

def print_maze(maze):
    string = '[\n'
    for row in maze:
        string = string+'    '+str(row)+',\n'
    
    return string + ']'

for i in range(1000):
    options = get_random_option()

    width = random.randint(9, 15)
    height = random.randint(9, 15)

    maze = generate_maze(width, height, **options)
    writeXDatum(str(i), print_maze(maze), **options)
    writeYDatum(str(i), print_maze(maze), **options)
