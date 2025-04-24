
# Basic test case
warehouse_map = [
    ['S', '.', '.', '.', '.'],
    ['X', 'X', '.', 'X', '.'],
    ['.', 'P', 'P', '.', '.'],
    ['.', 'X', '.', '.', 'D'],
    ['.', '.', '.', 'X', '.']
]

# Movement directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

cost_map = {
    '.': 1,
    'P': 0.5,
    'S': 0,
    'D': 1
}

def start_end(grid):
    """
    Finds the positions of the start and end of the path.
    """
    start = end = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "D":
                end = (r, c)
    return start, end


start, end = start_end(warehouse_map)
print("Start:", start)
print("End:", end)

def dijkstra(grid):
    rows, cols = len(grid), len(grid[0])
    start, end = start_end(grid)
    if not start or not end:
        return None, float('inf')

    unvisted = set((r,c) for r in range(rows) for c in range(cols) if grid[r][c] != 'X')
    costs = {pos: float('inf') for pos in unvisted}
    parents = {}
    costs[start] = 0

    while unvisted:
        current = min(unvisted, key=lambda pos: costs[pos])         #key lambda returns the cost of a position using the costs dictionary we defined earlier. Using min(key lambda) we get the lowest cost neighbor 
        