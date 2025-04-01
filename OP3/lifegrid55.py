# Program for playing the game of Life.
from lifegrid import LifeGrid

# Define the initial configuration of live cells.
INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]

# Set the size of the grid.
GRID_WIDTH = int(input("Enter grid width: "))
GRID_HEIGHT = int(input("Enter grid height: "))
NUM_GENS = int(input("Enter number of generations: "))

# Indicate the number of generations.
# NUM_GENS = 8


def main():
    # Constructs the game grid and configure it.
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    # Plays the game.
    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)


# Generates the next generation of organisms.
def evolve(grid):
    # List for storing the live cells of the next generation.
    live_cells = []

    # Iterate over the elements of the grid.
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):

            # Determine the number of live neighbors for this cell.
            neighbors = grid.num_live_neighbors(i, j)

            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation.
            if (neighbors == 2 and grid.is_live_cell(i, j)) or (neighbors == 3):
                live_cells.append((i, j))

    # Reconfigure the grid using the liveCells coord list.
    grid.configure(live_cells)


# Prints a text based representation of the game grid.
def draw(grid):
    for i in range(grid.num_rows()):
        row_str = "".join('L' if grid.is_live_cell(i, j) else 'D' for j in range(grid.num_cols()))
        print(row_str)
    print("\n") 

# def draw(grid):
#     for r in range(grid.num_rows()):
#         for c in range(grid.num_cols()):
#             drawing = ''
#             if grid.is_live_cell(r,c):
#                 drawing += grid[r,c]
#                 print(drawing)
#             print('\n')




# Executes the main routine.
main()
