from collections import deque

# For displaying Maze output
class CellType:
    BOMB = "X"
    SAFE = "O"
    PATH = "/"

# Represent each seuqre
class Square:
    def __init__ (self, x, y, cellType):
        self.x = x
        self.y = y
        self.cellType = cellType

# Maze data - can store in database - or randomly generate
mazeData = [
    ((0,0), CellType.SAFE), ((1,0), CellType.SAFE), ((2,0), CellType.BOMB), ((3,0), CellType.BOMB), ((4,0), CellType.SAFE),
    ((0,1), CellType.BOMB), ((1,1), CellType.BOMB), ((2,1), CellType.SAFE), ((3,1), CellType.BOMB), ((4,1), CellType.SAFE),
    ((0,2), CellType.SAFE), ((1,2), CellType.BOMB), ((2,2), CellType.BOMB), ((3,2), CellType.SAFE), ((4,2), CellType.BOMB),
    ((0,3), CellType.BOMB), ((1,3), CellType.SAFE), ((2,3), CellType.BOMB), ((3,3), CellType.SAFE), ((4,3), CellType.BOMB),
    ((0,4), CellType.SAFE), ((1,4), CellType.BOMB), ((2,4), CellType.SAFE), ((3,4), CellType.BOMB), ((4,4), CellType.BOMB),
]

# Convert to dictionary
maze = {}
for (coord, cellType) in mazeData:
    x, y = coord
    maze[(x, y)] = Square(x, y, cellType)

# Top Top-Right Right Bottom-Right Bottom Bottom-Left Left Top-Left
directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

# Move in direction only if not bomb
def move_in_direction(x, y, direction):
    dx, dy = direction
    newX, newY = x + dx, y + dy

    # Allow to exit maze to move out of bounds
    if newY == 5:
        return newX, newY

    # Return Square if (Square exists & not bomb)
    if (newX, newY) in maze and maze[(newX, newY)].cellType != CellType.BOMB:
        return newX, newY   
    
    return None

def get_maze_length(maze):
    length = max(y for x, y in maze.keys()) + 1

    return length

def get_maze_width(maze):
    width = max(x for x, y in maze.keys()) + 1

    return width


def bfs (start, maze):

    # Length for goal test
    mazeLength = get_maze_length(maze)

    # Position, Path
    queue = deque([(start, [start])])

    visited = set()

    while queue:
        (current, path) = queue.popleft()
        x, y = current

        # Skip if visited
        if (current) in visited:
            continue

        # Add to visited
        visited.add((x,y))

        # Check if reached last col, (any x, mazeLength) 
        if y == mazeLength - 1:
            return path
        
        # Get neighbours that not bomb & not previous Square
        for direction in directions:
            neighbour = move_in_direction(x, y, direction)

            if neighbour and neighbour not in visited:
                new_path = path + [neighbour]
                queue.append((neighbour, new_path))

    return None

# Function to print the maze with the path filled in
def print_maze_with_path(maze, path):
 
    # Mark the path on the maze
    for (x, y) in path:
        if maze[(x, y)].cellType != CellType.BOMB:
            maze[(x, y)].cellType = CellType.PATH  

    # Get width and height for loop
    length = get_maze_length(maze)
    width = get_maze_width(maze)

    # Print the maze
    for y in range(length):
        row = ""
        for x in range(width):
            row += f"{maze[(x, y)].cellType:<3}"  
        print(row)
    

if __name__ == "__main__":
    # Assuming Totchaka always enters from 0,0 and Ally follows behind him
    start = (0, 0)  
    
    # Find Path
    path = bfs(start, maze)

    # Output
    if path:
        print(f"Path found: {path}\n")
        print("Maze with path:")
        print_maze_with_path(maze, path)
        print("\nSafe = 'O' | Bomb = 'X' | Path = '/'")
    else:
        print("No path found")