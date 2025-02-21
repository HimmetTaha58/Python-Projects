import numpy as np

grid = np.full((6, 7), '.')
line = 5

def draw_grid():
    for row in grid:
        print(''.join(row))


def check_vertical(grid, symbol):
    for col in range(grid.shape[1]):
        for row in range(grid.shape[0] - 3):
            if grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col] == symbol:
                return True
    return False

def check_horizontal(grid, symbol):
    for row in grid:
        for i in range(len(row) - 3):
            if row[i] == row[i + 1] == row[i + 2] == row[i + 3] == symbol:
                return True
    return False

def check_diagonal_down(grid, symbol):
    for row in range(grid.shape[0] - 3):
        for col in range(grid.shape[1] - 3):
            if grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3] == symbol:
                return True
    return False

def check_diagonal_up(grid, symbol):
    for row in range(3, grid.shape[0]):
        for col in range(grid.shape[1] - 3):
            if grid[row][col] == grid[row - 1][col + 1] == grid[row - 2][col + 2] == grid[row - 3][col + 3] == symbol:
                return True
    return False


user1_symbol = "X"
user2_symbol = "O"

game_running = True
while game_running:
    user1_input = int(input("1: >"))
    grid[line][user1_input - 1] = user1_symbol

    draw_grid()


    if check_vertical(grid, user1_symbol):
        print("Oyuncu 1 kazandı!")
        break

    if check_horizontal(grid, user1_symbol):
        print("Oyuncu 1 kazandı!")
        break

    if check_diagonal_down(grid, user1_symbol):
        print("Oyuncu1 kazandı!")
        break

    if check_diagonal_up(grid, user1_symbol):
        print("Oyuncu1 kazandı!")
        break

    user2_input = int(input("2: >"))
    grid[line][user2_input - 1] = user2_symbol

    draw_grid()

    if check_vertical(grid, user2_symbol):
        print("Oyuncu 2 kazandı!")
        break

    if check_horizontal(grid, user2_symbol):
        print("Oyuncu 2 kazandı!")
        break

    if check_diagonal_down(grid, user2_symbol):
        print("Oyuncu2 kazandı!")
        break

    if check_diagonal_up(grid, user2_symbol):
        print("Oyuncu1 kazandı!")
        break

    if np.all(grid[line] != "."):
        line -= 1
        if line < 0:
            print("Oyun berabere!")
            break

    if np.all(grid[line] != "."):
        line -= 1

