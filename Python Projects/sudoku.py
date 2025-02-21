grid = {
    'A': [".", ".", ".", ".", ".", ".", "4", ".", "."],
    'B': [".", ".", "3", "6", ".", ".", ".", ".", "."],
    'C': ["9", ".", ".", ".", "9", "4", ".", "3", "."],
    'D': [".", "5", ".", "4", ".", ".", ".", ".", "2"],
    'E': [".", ".", ".", ".", ".", ".", "1", ".", "."],
    'F': [".", ".", ".", "2", "1", ".", ".", ".", "."],
    'G': [".", ".", "7", ".", ".", ".", ".", ".", "."],
    'H': ["5", ".", ".", ".", ".", "7", ".", "6", "."],
    'I': [".", "8", ".", ".", "8", ".", ".", ".", "."],
}

keys_list = list(grid.keys())


def find_region(row, col):
    return (row // 3) * 3 + (col // 3) + 1


def check_value_in_region(grid, row, col, value):
    region_row_start = (row // 3) * 3
    region_col_start = (col // 3) * 3
    for r in range(region_row_start, region_row_start + 3):
        for c in range(region_col_start, region_col_start + 3):
            if grid[keys_list[c]][r] == value:
                return True
    return False


def is_sudoku_solved(grid):
    for row in range(9):
        for col in range(9):
            value = grid[keys_list[col]][row]
            if value == ".":
                return False
            if check_value_in_region(grid, row, col, value) == False:
                return False
    return True


game_running = True
while game_running:
    print(f"  {' '.join(keys_list[:3])} | {' '.join(keys_list[3:6])} | {' '.join(keys_list[6:])}")

    for i in range(9):
        row_values = [grid[col][i] for col in keys_list]
        print(f"{i + 1} {' '.join(row_values[:3])} | {' '.join(row_values[3:6])} | {' '.join(row_values[6:])}")

        if i in [2, 5]:
            print("  ------+-------+------")

    user_input = input("Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:").split()

    if len(user_input) >= 2 and user_input[0][0].isalpha() and user_input[0][1].isdigit():
        target_char = user_input[0][0].upper()
        target_num = int(user_input[0][1]) - 1
        new_value = user_input[1]

        if target_char in grid and 0 <= target_num < len(grid[target_char]):
            if grid[target_char][target_num] == ".":
                grid[target_char][target_num] = new_value

                row = target_num
                col = keys_list.index(target_char)

                if check_value_in_region(grid, row, col, new_value):
                    print(f"Value '{new_value}' is found in the region containing cell {target_char}{target_num + 1}.")
                else:
                    print(
                        f"Value '{new_value}' is not found in the region containing cell {target_char}{target_num + 1}.")

                if is_sudoku_solved(grid):
                    print("Congratulations! Sudoku is solved.")
                    game_running = False
            else:
                print("Cell already has a value. Choose another cell.")
        else:
            print("Invalid cell location.")
    else:
        print("Invalid input. Expected format: 'A1 value'")

    if not game_running:
        break

    if input("Continue? (yes/no): ").lower() == "no":
        game_running = False
