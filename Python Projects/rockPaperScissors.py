import random

print("""Rock, Paper, Scissors
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.""")

wins = 0
ties = 0
lose = 0

game_running = True
while game_running:
    elements = ["rock", "paper", "scissors"]
    rand_element = random.choice(elements)

    print(f"{wins} Wins, {lose} Losses, {ties} Ties")

    user_input = input("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit ")
    if user_input.lower() == "r":
        if rand_element == "rock":
            print("Rock, İts a tie")
            ties += 1
        elif rand_element == "paper":
            print("Paper ,Lose !")
            lose += 1
        else:
            print("Scissors , You Win!")
            wins += 1
    elif user_input.lower() == "p":
        if rand_element == "rock":
            print("Rock , You Win! ")
            wins += 1
        elif rand_element == "paper":
            print("İts a tie")
            ties += 1
        else:
            print("Scissors ,Lose !")
            lose += 1
    elif user_input.lower() == "s":
        if rand_element == "rock":
            print("Rock , You Lose! ")
            lose += 1
        elif rand_element == "paper":
            print("Paper ,You win")
            wins += 1
        else:
            print("İts a tie ")
            ties += 1
    elif user_input.lower() == "q":
        game_running = False
    else:
        print("""
        Wrong input please enter only R, S, P or Quit !
        """)
        continue




