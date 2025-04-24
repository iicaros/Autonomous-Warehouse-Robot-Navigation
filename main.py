import heapq

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
