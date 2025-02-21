import random

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

safe = 0
budget = int(input("Enter your budget : "))

true_false = True
while true_false:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sums = dice1 + dice2

    bet_input = int(input(f"You have {budget} mon . How much do you bet ?"))
    pot = bet_input // 10

    if bet_input > budget:
        print("You do not have enough to make that bet.")
    else:
        print("""
            The dealer swirls the cup and you hear the rattle of dice.
        The dealer slams the cup on the floor, still covering the
        dice and asks for your bet.

        """)

        choice = input("CHO (even) or HAN (odd)? :")

        print(f"""The dealer lift the cup to reveal : 
        {JAPANESE_NUMBERS.get(dice1)}   -   {JAPANESE_NUMBERS.get(dice2)}
        {dice1}   {dice2}""")

        if choice.lower() == "even":
            if sums % 2 == 0:
                print(f"You won! You take {bet_input * 2} mon.")
                budget += bet_input
                print(f'The house collects a', pot, 'mon fee.')
                safe += pot
                budget -= pot
            else:
                print("You lost!")
                budget -= bet_input

        elif choice.lower() == "odd":
            if sums % 2 == 0:
                print("You lost!")
                budget -= bet_input
            else:
                print(f"You won! You take {bet_input * 2} mon.")
                budget += bet_input
                print(f'The house collects a', pot, 'mon fee.')
                safe += pot
                budget -= pot
        else:
            print("Wrong input !")



