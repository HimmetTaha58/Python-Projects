import random

def dice_main():
    dice_shapes = {
        1: [
            "+-------+",
            "|       |",
            "|   O   |",
            "|       |",
            "+-------+"
        ],
        2: [
            "+-------+",
            "|       |",
            "| O   O |",
            "|       |",
            "+-------+"
        ],
        3: [
            "+-------+",
            "| O     |",
            "|   O   |",
            "|     O |",
            "+-------+"
        ],
        4: [
            "+-------+",
            "| O   O |",
            "|       |",
            "| O   O |",
            "+-------+"
        ],
        5: [
            "+-------+",
            "| O   O |",
            "|   O   |",
            "| O   O |",
            "+-------+"
        ],
        6: [
            "+-------+",
            "| O   O |",
            "| O   O |",
            "| O   O |",
            "+-------+"
        ]
    }

    dice_num = random.randint(1, 6)
    return dice_shapes[dice_num], dice_num

def print_dice_row(dice_list):
    for i in range(5):
        for dice in dice_list:
            print(dice[i], end="  ")  ,
        print()

score = 0
life = 3
true_false = True
while true_false:

    dice_much = random.randint(2, 6)
    total_value = 0

    dice_list = []
    for i in range(dice_much):
        dice_value, dice_num = dice_main()
        dice_list.append(dice_value)
        total_value += dice_num

    print_dice_row(dice_list)

    user_input = int(input("Toplam: "))

    if user_input == total_value:
        score += 1
        print(f"Doğru, skorunuz: {score}")
    else:
        life -= 1
        print(f"Yanlış bildiniz, Canınız: {life}")

    if life == 0:
        true_false = False
        print("Oyun bitti!")
