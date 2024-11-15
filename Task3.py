from collections import deque
 
# Top Top-Right Right Bottom-Right Bottom Bottom-Left Left Top-Left
directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

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

# Convet to maze - dictionary holding square (key - coordinates)
def mazeData_to_maze (mazeData, m , n):
    maze = {}
    for y in range(m):
        for x in range(n):
            maze[(x, y)] = Square(x, y, mazeData[y][x])

    return maze

# Move in direction only if not bomb
def move_in_direction(x, y, direction, maze):
    dx, dy = direction
    newX, newY = x + dx, y + dy

    # Allow to exit maze to move out of bounds
    if newY == 5:
        return newX, newY

    # Return Square if (Square exists & not bomb)
    if (newX, newY) in maze and maze[(newX, newY)].cellType != CellType.BOMB:
        return newX, newY   
    
    return None

def bfs (start, maze, m , n):

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

        # Check if reached last col, (any x, n) 
        if y == n - 1:
            return path
        
        # Get neighbours that not bomb & not previous Square
        for direction in directions:
            neighbour = move_in_direction(x, y, direction, maze)

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

    # Print the maze
    for y in range(m):
        row = ""
        for x in range(n):
            row += f"{maze[(x, y)].cellType:<3}"  
        print(row)
    
if __name__ == "__main__":
    # Assuming Totchaka always enters from 0,0 and Ally follows behind him
    start = (0, 0)  

    # Maze
    mazeData = [
        [CellType.SAFE, CellType.SAFE, CellType.BOMB, CellType.BOMB, CellType.SAFE],
        [CellType.BOMB, CellType.BOMB, CellType.SAFE, CellType.BOMB, CellType.SAFE],
        [CellType.SAFE, CellType.BOMB, CellType.BOMB, CellType.SAFE, CellType.BOMB],
        [CellType.BOMB, CellType.SAFE, CellType.BOMB, CellType.SAFE, CellType.BOMB],
        [CellType.SAFE, CellType.BOMB, CellType.SAFE, CellType.BOMB, CellType.BOMB]
    ]

    # Specify size
    m, n = 5, 5

    # Convert mazeData to maze
    maze = mazeData_to_maze(mazeData, m , n)
    
    # Find Path
    path = bfs(start, maze, m, n)

    # Output
    if path:
        print(f"Path found: {path}\n")
        print("Maze with path:")
        print_maze_with_path(maze, path)
        print("\nSafe = 'O' | Bomb = 'X' | Path = '/'")
    else:
        print("No path found")