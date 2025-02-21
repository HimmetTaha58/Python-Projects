import random

budget_amount = int(input("Enter your starting budget: "))


def draw_card():
    suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    all_cards = [(suit, card) for suit in suits for card in cards]
    random_card = random.choice(all_cards)

    if random_card[1] == "Ace":
        value = 11
    elif random_card[1] in ["J", "Q", "K"]:
        value = 10
    else:
        value = int(random_card[1])

    return random_card, value


def ace_value(hand_value, aces_count):
    while hand_value > 21 and aces_count > 0:
        hand_value -= 10
        aces_count -= 1
    return hand_value


def blackjack():
    global budget_amount
    player_hand = []
    dealer_hand = []
    player_aces = 0
    dealer_aces = 0

    bet_amount = int(input("Enter your bet amount: "))

    print("Player is drawing cards...")
    card, value = draw_card()
    if card[1] == "Ace":
        player_aces += 1
    player_hand.append((card, value))

    card, value = draw_card()
    if card[1] == "Ace":
        player_aces += 1
    player_hand.append((card, value))

    player_value = player_hand[0][1] + player_hand[1][1]
    player_value = ace_value(player_value, player_aces)

    print(
        f"Player's Hand: {player_hand[0][0][0]} {player_hand[0][0][1]}, {player_hand[1][0][0]} {player_hand[1][0][1]} - Value: {player_value}")

    print("Dealer is drawing cards...")
    card, value = draw_card()
    if card[1] == "Ace":
        dealer_aces += 1
    dealer_hand.append((card, value))

    card, value = draw_card()
    if card[1] == "Ace":
        dealer_aces += 1
    dealer_hand.append((card, value))

    dealer_hidden_value = dealer_hand[0][1]
    dealer_visible_value = dealer_hand[1][1]
    dealer_value = ace_value(dealer_hidden_value + dealer_visible_value, dealer_aces)

    print(f"Dealer's Hand: ? ?, {dealer_hand[1][0]} {dealer_hand[1][1]} - Visible Value: {dealer_visible_value}")

    if dealer_value > 21:
        print("Dealer busted! Player wins!")
        budget_amount += bet_amount
        print(f"You won! Your new budget is: {budget_amount} $.")
        return

    while True:
        to_continue = input("Do you want to continue (y / n): ")
        if to_continue.lower() == "y":
            card, value = draw_card()
            if card[1] == "Ace":
                player_aces += 1
            player_hand.append((card, value))
            player_value += value
            player_value = ace_value(player_value, player_aces)
            print(f"Player drew a new card: {card[0]} {card[1]} - New Value: {player_value}")
            if player_value > 21:
                print("You busted! Dealer wins.")
                budget_amount -= bet_amount
                print(f"You lost! Your new budget is: {budget_amount} $.")
                return
        else:
            break

    # Dealer draws cards
    print(f"Dealer's Hidden Card: {dealer_hand[0][0]} {dealer_hand[0][1]}")
    while dealer_value < 17:
        print("Dealer is drawing cards...")
        card, value = draw_card()
        if card[1] == "Ace":
            dealer_aces += 1
        dealer_hand.append((card, value))
        dealer_value += value
        dealer_value = ace_value(dealer_value, dealer_aces)
        print(f"Dealer drew a new card: {card[0]} {card[1]} - New Value: {dealer_value}")
        if dealer_value > 21:
            print("Dealer busted! Player wins!")
            budget_amount += bet_amount
            print(f"You won! Your new budget is: {budget_amount} $.")
            return

    # Game result
    if player_value > dealer_value:
        print("Player wins!")
        budget_amount += bet_amount
    elif player_value < dealer_value:
        print("Dealer wins!")
        budget_amount -= bet_amount
    else:
        print("It's a tie!")

    print(f"Game Result! Your new budget is: {budget_amount} $.")


blackjack()

again = input("Do you want to play again (y / n): ")

if again.lower() == "y":
    blackjack()
