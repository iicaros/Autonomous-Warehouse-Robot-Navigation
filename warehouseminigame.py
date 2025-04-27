import random
import os
import matplotlib.pyplot as plt
import numpy as np

class DijkstraPathfinder:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.cost_map = {
            '.': 1,
            'P': 0.5,
            'S': 0,
            'D': 1
        }

    def get_cost(self, current, neighbor, direction):
        r, c = neighbor
        cell = self.grid[r][c]
        move_cost = self.cost_map.get(cell, 1)
        # Reduce cost if moving up or left
        if direction in [(-1, 0), (0, -1)]:
            move_cost = 0.5
        return move_cost

    def get_neighbors(self, r, c):
        for dr, dc in self.directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] != 'X':
                yield (nr, nc), (dr, dc)

    def dijkstra(self, start, destination):
        unvisited = {
            (r, c)
            for r in range(self.rows)
            for c in range(self.cols)
            if self.grid[r][c] != 'X'
        }
        costs = {pos: float('inf') for pos in unvisited}
        parents = {}
        costs[start] = 0

        while unvisited:
            current = min(unvisited, key=lambda pos: costs[pos])
            if current == destination:
                break

            unvisited.remove(current)
            r, c = current

            for neighbor, direction in self.get_neighbors(r, c):
                if neighbor not in unvisited:
                    continue
                new_cost = costs[current] + self.get_cost(current, neighbor, direction)
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    parents[neighbor] = current

        # reconstruct path
        path = []
        cur = destination
        while cur in parents:
            path.append(cur)
            cur = parents[cur]
        if cur == start:
            path.append(start)
            path.reverse()
            return costs[destination], path
        else:
            return float('inf'), []

def find_start_end(grid):
    start = end = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'D':
                end = (r, c)
    return start, end

def print_grid_with_path(grid, path):
    grid_with_path = [row.copy() for row in grid]
    for (r, c) in path:
        if grid_with_path[r][c] not in ('S', 'D'):
            grid_with_path[r][c] = '*'
    print("Grid with Path:")
    for row in grid_with_path:
        print(' '.join(row))
    print()

def generate_game_grid(rows, cols, obstacle_prob=0.2, slow_prob=0.1):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    # randomly place obstacles and slow tiles
    for r in range(rows):
        for c in range(cols):
            if (r, c) in [(0,0), (rows-1, cols-1)]:
                continue
            rnd = random.random()
            if rnd < obstacle_prob:
                grid[r][c] = 'X'
            elif rnd < obstacle_prob + slow_prob:
                grid[r][c] = 'P'
    # start & destination
    grid[0][0] = 'S'
    grid[rows-1][cols-1] = 'D'
    return grid

def print_grid(grid, player_pos):
    os.system('cls' if os.name == 'nt' else 'clear')
    for r, row in enumerate(grid):
        line = ""
        for c, cell in enumerate(row):
            if (r, c) == player_pos:
                line += '☺ '
            else:
                line += f"{cell} "
        print(line)
    print()
    # Legend
    print("Legend:")
    print("  S = Start")
    print("  D = Destination (Goal)")
    print("  X = Wall (obstacle)")
    print("  P = Slow zone")
    print("  . = Open floor")
    print("  ☺ = You")
    print("  R = Regenerate grid (if impossible)")
    print("  Q = Quit game\n")

def play_game(rows=10, cols=10, move_limit=30):
    while True:
        grid = generate_game_grid(rows, cols)
        start, dest = find_start_end(grid)
        pf_check = DijkstraPathfinder(grid)
        cost_check, path_check = pf_check.dijkstra(start, dest)

        if not path_check:
            print_grid(grid, (0,0))
            print("⚠️  No possible path on this grid!")
            choice = input("Press R to regenerate grid, or Q to quit: ").strip().upper()
            if choice == 'R':
                continue
            else:
                print("Goodbye!")
                return
        else:
            break

    player = start
    moves = 0

    # initial display
    print_grid(grid, player)
    input("Press Enter to start...")

    while moves < move_limit:
        print_grid(grid, player)
        print(f"Moves left: {move_limit - moves}")
        move = input("Move (W/A/S/D), R regenerate, Q quit: ").strip().upper()

        if move == 'Q':
            print("You quit the game. Goodbye!")
            return
        if move == 'R':
            return play_game(rows, cols, move_limit)  # restart
        dirs = {'W': (-1, 0), 'S': (1, 0), 'A': (0, -1), 'D': (0, 1)}
        if move not in dirs:
            continue

        dr, dc = dirs[move]
        nr, nc = player[0] + dr, player[1] + dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            continue
        if grid[nr][nc] == 'X':
            continue

        player = (nr, nc)
        moves += 1

        if grid[nr][nc] == 'D':
            print_grid(grid, player)
            print(f"🎉 You reached the destination in {moves} moves!")
            break
    else:
        print_grid(grid, player)
        print("😢 Move limit reached! You failed to escape.")

    # show optimal path
    start, dest = find_start_end(grid)
    pf = DijkstraPathfinder(grid)
    cost, path = pf.dijkstra(start, dest)
    if path:
        print(f"\nOptimal path cost: {cost:.2f}, length: {len(path)}")
        print_grid_with_path(grid, path)
    else:
        print("\nNo path exists from S to D in this grid.")

if __name__ == "__main__":
    random.seed()  # or set to an integer for reproducibility
    play_game()
