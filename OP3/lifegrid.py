from arrays import Array2D

# Доповнити модуль lifegrid_5x5.py:

# реалізацією функції draw(). Функція повинна виводити на екран поточний стан системи. Для позначення мертвих та живих комірок потрібно використовувати символ L для живих комірок й D для мертвих.
# фрагментом, який дозволить користувачу вводити розмір поля та кількість поколінь для генерації.

# def draw():


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """

    DEAD_CELL = 'D'
    LIVE_CELL = 'L'

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        self._grid = Array2D(num_rows, num_cols)
        self.configure([])

    def num_rows(self):
        """ Returns the number of rows in the grid. """
        return self._grid.num_rows()

    def num_cols(self):
        """ Returns the number of columns in the grid. """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """ Configures the grid to contain the given live cells. """
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                self._grid[row,col] = self.DEAD_CELL
        for x, y in coord_list:
            self._grid[x,y] = self.LIVE_CELL

    def is_live_cell(self, row, col):
        """ Returns True if the given cell is alive, False otherwise. """
        return self._grid[row,col] == self.LIVE_CELL

    def clear_cell(self, row, col):
        """ Sets a cell to dead. """
        self._grid[row,col] = self.DEAD_CELL

    def set_cell(self, row, col):
        """ Sets a cell to live. """
        self._grid[row,col] = self.LIVE_CELL

    def num_live_neighbors(self, row, col):
        """ Returns the number of live neighbors for the given cell. """
        live_counter = 0
        rows, cols = self.num_rows(), self.num_cols()
        
        neighbors = [
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1),                (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        ]
        
        for r, c in neighbors:
            if 0 <= r < rows and 0 <= c < cols and self._grid[r,c] == self.LIVE_CELL:
                live_counter += 1

        return live_counter

    def __str__(self):
        """ Returns a string representation of the grid. """
        return "\n".join("".join(self._grid[r,c] for c in range(self.num_cols())) for r in range(self.num_rows()))






# class LifeGrid:
#     """
#     Implements the LifeGrid ADT for use with the Game of Life.
#     """
#     # Defines constants to represent the cell states.
#     DEAD_CELL = 0
#     LIVE_CELL = 1

#     def __init__(self, num_rows, num_cols):
#         """
#         Creates the game grid and initializes the cells to dead.
#         :param num_rows: the number of rows.
#         :param num_cols: the number of columns.
#         """
#         # Allocates the 2D array for the grid.
#         self._grid = Array2D(num_rows, num_cols)
#         # Clears the grid and set all cells to dead.
#         self.configure(list())

#     def num_rows(self):
#         """
#         Returns the number of rows in the grid.
#         :return: the number rows in the grid.
#         """
#         return len(self._grid)

#     def num_cols(self):
#         """
#         Returns the number of columns in the grid.
#         :return:Returns the number of columns in the grid.
#         """
#         return len(self._grid[0])

#     def configure(self, coord_list):
#         """
#         Configures the grid to contain the given live cells.

#         :param coord_list:
#         :return:
#         """
#         # for row in range (self._grid.num_rows()):
#         #     for col in range (self._grid.num_cols()):
#         #         self._grid[row][col] = 'D'
#         for x, y in coord_list:
#             self._grid[x][y] = 'L'
#         return self._grid

#     def is_live_cell(self, row, col):
#         """
#         Does the indicated cell contain a live organism?

#         :param row: row of the cell.
#         :param col: column of the cell.
#         :return: the result of check.
#         """
#         if self._grid[row][col] == 'L':
#             return True
#         return False

#     def clear_cell(self, row, col):
#         """
#         Clears the indicated cell by setting it to dead.
#         :param row: row of the cell.
#         :param col: column of the cell.
#         """
#         self._grid[row][col] = 'D'

#     def set_cell(self, row, col):
#         """
#         Sets the indicated cell to be alive.
#         :param row: row of the cell.
#         :param col: column of the cell.
#         """
#         self._grid[row][col] = 'L'

#     def num_live_neighbors(self, row, col):
#         """
#         Returns the number of live neighbors for the given cell.
#         :param row: row of the cell.
#         :param col: column of the cell.
#         :return:
#         """
#         # live_counter = 0
#         # rows, cols = self._grid.num_rows(), self._grid.num_cols()
#         # up = (row + 1, col) if row + 1 < rows else None
#         # down = (row - 1, col) if row - 1 >= 0 else None
#         # right = (row, col + 1) if col + 1 < cols else None
#         # left = (row, col - 1) if col - 1 >= 0 else None
#         # if self._grid[up[0]][up[1]] == 'L':
#         #     live_counter += 1
#         # if self._grid[down[0]][down[1]] == 'L':
#         #     live_counter += 1
#         # if self._grid[right[0]][right[1]] == 'L':
#         #     live_counter += 1
#         # if self._grid[left[0]][left[1]] == 'L':
#         #     live_counter += 1
#         live_counter = 0
#         rows, cols = self.num_rows(), self.num_cols()
        
#         neighbors = [
#             (row-1, col-1), (row-1, col), (row-1, col+1),
#             (row, col-1),                (row, col+1),
#             (row+1, col-1), (row+1, col), (row+1, col+1)
#         ]
        
#         for r, c in neighbors:
#             if 0 <= r < rows and 0 <= c < cols and self._grid[r][c] == self.LIVE_CELL:
#                 live_counter += 1

#         return live_counter
    
#     def __str__(self):
#         """
#         Returns string representation of LifeGrid
#         in the form of:
#         DDLDD
#         DLDLD
#         DLDLD
#         DDLDD
#         DDDDD
#         Where 'D' - dead cell, 'L' - live cell.
#         """
#         result = []
        
#         for r in range(self._grid.num_rows()):
#             row_str = ""
#             for c in range(self._grid.num_cols()):
#                 row_str += self._grid[r, c]
#             result.append(row_str)
        
#         return "\n".join(result)


# # test = LifeGrid(4,5)
# # print(test._grid)
