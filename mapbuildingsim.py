import pygame
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
        if direction in [(-1, 0), (0, -1)]:
            move_cost = 0.5
        return move_cost

    def get_neighbors(self, r, c):
        for dr, dc in self.directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] != 'X':
                yield (nr, nc), (dr, dc)

    def dijkstra(self, start, destination):
        unvisited = set((r, c) for r in range(self.rows) for c in range(self.cols) if self.grid[r][c] != 'X')
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


pygame.init()
WIDTH, HEIGHT = 1000, 920
ROWS, COLS = 10, 10
GRID_OFFSET_X = 200  # Space for instructions
CELL_SIZE = (WIDTH - GRID_OFFSET_X) // COLS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Warehouse Editor + Pathfinding")

font = pygame.font.SysFont("Arial", 18)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
LEGEND_BG = (240, 240, 240)
INSTRUCTION_BG = (230, 230, 230)


cell_types = {
    0: '.',   # empty
    1: 'X',   # wall
    2: 'P',   # low cost
    3: 'S',   # start
    4: 'D'    # end
}
current_cell_type = 3  # Default to Start cell type

warehouse = [['.' for _ in range(COLS)] for _ in range(ROWS)]

# Flags to track Start and Destination placement
start_placed = False
end_placed = False

# Log message to display
log_message = ""

def draw_legend():
    global current_cell_type
    legend_font = pygame.font.SysFont("Arial", 16)
    legend = [
        ("Start", BLUE, 3),
        ("End", GREEN, 4),
        ("Wall", (23, 23, 23), 1),
        ("Low Cost", YELLOW, 2),
        ("Eraser", WHITE, 0)
    ]

    bezel_rect = pygame.Rect(GRID_OFFSET_X, 800, WIDTH - GRID_OFFSET_X, 120)
    pygame.draw.rect(screen, LEGEND_BG, bezel_rect)

    x_offset = GRID_OFFSET_X + 20
    y_offset = 810

    for text, color, cell_type in legend:
        pygame.draw.rect(screen, color, (x_offset, y_offset, 50, 50))
        pygame.draw.rect(screen, BLACK, (x_offset, y_offset, 50, 50), 2)
        label = legend_font.render(text, True, BLACK)
        screen.blit(label, (x_offset - (label.get_width() // 2) + 25, y_offset + 55))
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            if x_offset < mx < x_offset + 50 and y_offset < my < y_offset + 50:
                current_cell_type = cell_type
                print(f"Selected: {text} ({cell_type})")
        x_offset += 80

    # Draw selected cell preview
    pygame.draw.rect(screen, BLACK, (WIDTH - 70, 810, 50, 50), 2)
    pygame.draw.rect(screen, get_color_from_cell_type(current_cell_type), (WIDTH - 70, 810, 50, 50))
    label = legend_font.render("Selected", True, BLACK)
    screen.blit(label, (WIDTH - 71, 870))

def draw_instructions():
    pygame.draw.rect(screen, INSTRUCTION_BG, (0, 0, GRID_OFFSET_X, 800))
    instructions = [
        "Instructions:",
        "Click on the boxes below",
        "to select an object you",
        "want to place!",
        "",
        "",
        "- Left click to place.",
        "- Right click to erase.",
        "- Press SPACE to find path.",
        "- Press C to clear grid.",
        "- Press ESC to quit.",
        "",
    ]
    y = 20
    for line in instructions:
        label = font.render(line, True, BLACK)
        screen.blit(label, (20, y))
        y += 30

def get_color_from_cell_type(cell_type):
    if cell_type == 1:
        return BLACK
    elif cell_type == 2:
        return YELLOW
    elif cell_type == 3:
        return BLUE
    elif cell_type == 4:
        return GREEN
    else:
        return WHITE

def draw_arrow(start_pos, end_pos, color=RED, width=4):
    pygame.draw.line(screen, color, start_pos, end_pos, width)
    # Arrowhead
    rotation = np.arctan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
    arrow_length = 10
    angle = np.pi / 6
    pygame.draw.line(screen, color, end_pos, 
                     (end_pos[0] - arrow_length * np.cos(rotation - angle),
                      end_pos[1] - arrow_length * np.sin(rotation - angle)), width)
    pygame.draw.line(screen, color, end_pos, 
                     (end_pos[0] - arrow_length * np.cos(rotation + angle),
                      end_pos[1] - arrow_length * np.sin(rotation + angle)), width)

def draw_log_message():
    log_font = pygame.font.SysFont("Arial", 14)
    pygame.draw.rect(screen, WHITE, (10, HEIGHT - 60, 180, 50))  # Background for log
    pygame.draw.rect(screen, BLACK, (10, HEIGHT - 60, 180, 50), 2)  # Border for log box
    log_label = log_font.render(log_message, True, BLACK)
    screen.blit(log_label, (15, HEIGHT - 50))


running = True
while running:
    screen.fill(WHITE)

    draw_instructions()

    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(GRID_OFFSET_X + c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, get_color_from_cell_type([k for k, v in cell_types.items() if v == warehouse[r][c]][0]), rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

    draw_legend()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed()[0]:  # lc
            x, y = pygame.mouse.get_pos()
            if GRID_OFFSET_X <= x < WIDTH and y < 800:
                c, r = (x - GRID_OFFSET_X) // CELL_SIZE, y // CELL_SIZE
                if 0 <= r < ROWS and 0 <= c < COLS:
                    if current_cell_type == 0:  # eraser
                        warehouse[r][c] = '.'
                    elif current_cell_type == 3:  # start
                        if not start_placed:  # Allow placing only one Start
                            warehouse[r][c] = 'S'
                            start_placed = True
                            log_message = "Start placed."
                        else:
                            log_message = "Start already placed!"
                    elif current_cell_type == 4:  # end
                        if not end_placed:  # Allow placing only one end
                            warehouse[r][c] = 'D'
                            end_placed = True
                            log_message = "Destination placed."
                        else:
                            log_message = "Destination already placed!"
                    else:
                        warehouse[r][c] = cell_types[current_cell_type]

        if pygame.mouse.get_pressed()[2]:  # rc
            x, y = pygame.mouse.get_pos()
            if GRID_OFFSET_X <= x < WIDTH and y < 800:
                c, r = (x - GRID_OFFSET_X) // CELL_SIZE, y // CELL_SIZE
                if 0 <= r < ROWS and 0 <= c < COLS:
                    if warehouse[r][c] == 'S':  # If it's start, allow erasing it
                        start_placed = False
                    elif warehouse[r][c] == 'D':  # If it's end, allow erasing it
                        end_placed = False
                    warehouse[r][c] = '.'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start, end = find_start_end(warehouse)
                if start and end:
                    pathfinder = DijkstraPathfinder(warehouse)
                    total_cost, path = pathfinder.dijkstra(start, end)
                    if path:
                        log_message = f"Path found! Cost: {total_cost}"
                        for i in range(len(path) - 1):
                            r1, c1 = path[i]
                            r2, c2 = path[i + 1]
                            start_pos = (GRID_OFFSET_X + c1 * CELL_SIZE + CELL_SIZE // 2, r1 * CELL_SIZE + CELL_SIZE // 2)
                            end_pos = (GRID_OFFSET_X + c2 * CELL_SIZE + CELL_SIZE // 2, r2 * CELL_SIZE + CELL_SIZE // 2)
                            draw_arrow(start_pos, end_pos)
                            pygame.display.update()
                            pygame.time.delay(100)
                    else:
                        log_message = "No path found."
                else:
                    log_message = "Start and Destination not set!"

            if event.key == pygame.K_c:
                warehouse = [['.' for _ in range(COLS)] for _ in range(ROWS)]
                start_placed = False
                end_placed = False
                log_message = "Grid cleared."

            if event.key == pygame.K_ESCAPE:
                running = False

    draw_log_message()
    pygame.display.flip()

pygame.quit()
