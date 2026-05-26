import random, time, os

def create_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def next_generation(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            neighbors = sum(
                grid[(r + dr) % rows][(c + dc) % cols]
                for dr in [-1, 0, 1]
                for dc in [-1, 0, 1]
                if (dr, dc) != (0, 0)
            )
            if grid[r][c] == 1:
                new_grid[r][c] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[r][c] = 1 if neighbors == 3 else 0
    return new_grid

def display(grid):
    os.system("cls" if os.name == "nt" else "clear")
    for row in grid:
        print("".join("■ " if cell else "  " for cell in row))

grid = create_grid(20, 40)

for gen in range(100):
    display(grid)
    print(f"Generation: {gen + 1}")
    grid = next_generation(grid)
    time.sleep(0.15)