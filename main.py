import matplotlib.pyplot as plt
import numpy as np

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
    start = end = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "D":
                end = (r, c)
    return start, end


def dijkstra(grid):
    rows, cols = len(grid), len(grid[0])
    start, end = start_end(grid)
    if not start or not end:
        return None, float('inf')

    unvisted = set((r, c) for r in range(rows) for c in range(cols) if grid[r][c] != 'X')
    costs = {pos: float('inf') for pos in unvisted}
    parents = {}
    costs[start] = 0

    while unvisted:
        current = min(unvisted, key=lambda pos: costs[pos])
        if current == end:
            break

        unvisted.remove(current)
        r, c = current

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and neighbor in unvisted:
                cell = grid[nr][nc]
                move_cost = cost_map.get(cell, 1)

                if (dr, dc) == (-1, 0) or (dr, dc) == (0, -1):  # Up or Left directions
                    move_cost = 0.5

                new_cost = costs[current] + move_cost
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    parents[neighbor] = current

    path = []
    cur = end

    while cur in parents:
        path.append(cur)
        cur = parents[cur]

    if cur == start:
        path.append(start)
        path.reverse()
        return path, costs[end]
    else:
        return None, float('inf')


def grid_path_visualization(grid, path):
    cmap = {
        'S': 'green',
        'D': 'red',
        'X': 'black',
        '.': 'white',
        'P': 'blue'
    }

    plot_grid = np.zeros((len(grid), len(grid[0])))

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            cell = grid[r][c]
            if cell == 'S':
                plot_grid[r][c] = 2
            elif cell == 'D':
                plot_grid[r][c] = 3
            elif cell == 'X':
                plot_grid[r][c] = 1
            elif cell == 'P':
                plot_grid[r][c] = 0.5
            else:
                plot_grid[r][c] = 0

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(plot_grid, cmap='gray', interpolation='nearest')

    ax.set_xticks(np.arange(-0.5, len(grid[0]), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(grid), 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            cell = grid[r][c]
            if cell == 'S':
                ax.text(c, r, grid[r][c], ha='center', va='center', color='blue', fontsize=12) 
            elif cell == 'D':
                ax.text(c, r, grid[r][c], ha='center', va='center', color='blue', fontsize=12)  
            else:
                ax.text(c, r, grid[r][c], ha='center', va='center', color='white', fontsize=12)

    for (r, c) in path:
        ax.add_patch(plt.Rectangle((c - 0.5, r - 0.5), 1, 1, color='green', alpha=0.5))
        
    plt.show()


path, total_cost = dijkstra(warehouse_map)

if path:
    print("Path:", path)
    print("Cost:", total_cost)

    grid_path_visualization(warehouse_map, path)
else:
    print("No path found.")
