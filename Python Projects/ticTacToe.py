spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|\n")
    print(board)

def check_winner(spots, char):
    return ((spots[1] == spots[2] == spots[3] == char) or
            (spots[4] == spots[5] == spots[6] == char) or
            (spots[7] == spots[8] == spots[9] == char) or
            (spots[1] == spots[4] == spots[7] == char) or
            (spots[2] == spots[5] == spots[8] == char) or
            (spots[3] == spots[6] == spots[9] == char) or
            (spots[1] == spots[5] == spots[9] == char) or
            (spots[3] == spots[5] == spots[7] == char))

def is_draw(spots):
    return all(spot in ["X", "O"] for spot in spots.values())

print("Welcome to Tic-Tac-Toe! madeitby: Tahta\n")

user1_char = "X"
user2_char = "O"

game_running = True
while game_running:
    draw_board(spots)

    user1_input = input("What is X's move? (1 - 9) ")
    if user1_input.isdigit():
        target_value = int(user1_input)
        if 1 <= target_value <= 9:
            if spots[target_value] in [user1_char, user2_char]:
                print("This spot is already taken!")
                continue
            spots[target_value] = user1_char
        else:
            print("Please enter a number between 1 and 9!")
            continue
    else:
        print("Please enter a valid number!")
        continue

    if check_winner(spots, user1_char):
        draw_board(spots)
        print(f"Player {user1_char} wins!")
        break

    if is_draw(spots):
        draw_board(spots)
        print("It's a draw!")
        break

    draw_board(spots)

    user2_input = input("What is O's move? (1 - 9) ")
    if user2_input.isdigit():
        target_value = int(user2_input)
        if 1 <= target_value <= 9:
            if spots[target_value] in [user1_char, user2_char]:
                print("This spot is already taken!")
                continue
            spots[target_value] = user2_char
        else:
            print("Please enter a number between 1 and 9!")
            continue
    else:
        print("Please enter a valid number!")
        continue

    if check_winner(spots, user2_char):
        draw_board(spots)
        print(f"Player {user2_char} wins!")
        break

    if is_draw(spots):
        draw_board(spots)
        print("It's a draw!")
        break
