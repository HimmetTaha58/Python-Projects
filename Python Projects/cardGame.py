import random

def random_card(deck):
    random_card = random.choice(deck)
    deck.remove(random_card)

    if random_card[1] == "Ace":
        value = 1
    elif random_card[1] in ["J", "Q", "K"]:
        value = 10
    else:
        value = int(random_card[1])

    return random_card, value, deck


suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [(suit, card) for suit in suits for card in cards]

user1_score = 0
user2_score = 0

game_running = True
while game_running:
    user1_value = 0
    user2_value = 0

    if len(deck) == 0:
        if user1_score > user2_score:
            print("Player1 WON !")
        elif user1_score < user2_score:
            print("Player2 WON !")
        else:
            print("İts a tie Amazing")
        print("Deste bitti. Oyun sona erdi.")
        game_running = False
    else:
        card, value, deck = random_card(deck)

        user1_input = input("Player1 tap enter or (Q)uit")
        if user1_input.lower() == "q":
            game_running = False
            break
        else:
            print(f"Çekilen kart: {card[1]} of {card[0]}, Değer: {value}\n")
            user1_value = value

        card, value, deck = random_card(deck)

        user2_input = input("Player2 tap enter or (Q)uit")
        if user2_input.lower() == "q":
            game_running = False
            break
        else:
            print(f"Çekilen kart: {card[1]} of {card[0]}, Değer: {value}\n")
            user2_value = value


        if user1_value > user2_value:
            user1_score += 1
            print("Player1 Win !\n")
        elif user1_value < user2_value:
            user2_score += 1
            print("Player2 Win !\n")
        else:
            print("İts a tie!")

        print(f"Scores : {user1_score}, {user2_score}\n")


