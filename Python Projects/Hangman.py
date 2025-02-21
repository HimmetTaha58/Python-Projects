import random

hangman_pics = [
    """
  +--+
  |  |
     |
     |
     |
     |
 =====""",
    """
  +--+
  |  |
  O  |
     |
     |
     |
 =====""",
    """
  +--+
  |  |
  O  |
  |  |
     |
     |
 =====""",
    """
  +--+
  |  |
  O  |
 /|  |
     |
     |
 =====""",
    """
  +--+
  |  |
  O  |
 /|\ |
     |
     |
 =====""",
    """
  +--+
  |  |
  O  |
 /|\ |
 /   |
     |
 =====""",
    """
  +--+
  |  |
  O  |
 /|\ |
 / \ |
     |
 ====="""
]

categories = {
    "animals": [
        "elephant", "giraffe", "kangaroo", "penguin", "dolphin",
        "cheetah", "leopard", "tiger", "lion", "zebra",
        "panda", "koala", "monkey", "gorilla", "horse",
        "rhinoceros", "hippopotamus", "bear", "wolf", "fox",
        "rabbit"
    ],
    "fruits": [
        "apple", "banana", "orange", "grape", "mango",
        "pineapple", "strawberry", "blueberry", "kiwi", "peach",
        "pear", "plum", "watermelon", "cantaloupe", "nectarine",
        "pomegranate", "fig", "date", "avocado", "cherry",
        "lemon"
    ],
    "countries": [
        "usa", "canada", "mexico", "brazil", "argentina",
        "china", "india", "japan", "south korea", "germany",
        "france", "italy", "spain", "uk", "australia",
        "south africa", "nigeria", "egypt", "turkey", "saudi arabia",
        "russia"
    ],
    "colors": [
        "red", "blue", "green", "yellow", "purple",
        "orange", "pink", "brown", "black", "white",
        "grey", "cyan", "magenta", "lime", "navy",
        "teal", "maroon", "olive", "indigo", "violet",
        "beige"
    ],
    "vehicles": [
        "car", "motorcycle", "bicycle", "bus", "truck",
        "train", "airplane", "helicopter", "boat", "scooter",
        "van", "submarine", "sailboat", "yacht", "hovercraft",
        "jet", "tractor", "skateboard", "rollerblades", "moped",
        "limousine"
    ]
}

selected_category = random.choice(list(categories.keys()))
selected_word = random.choice(categories[selected_category])


missed_letters = []
word_list = ["_"] * len(selected_word)
pics_num = 0

game_running = True
while game_running:
    print(hangman_pics[pics_num])
    print(f"Selected Category: {selected_category}")
    print(' '.join(word_list))

    user_input = input("Guess a letter: ").lower()

    if user_input in missed_letters or user_input in word_list:
        print("Bu harfi  daha önce seçtiniz")
        continue

    if user_input in selected_word:
        for n in range(len(selected_word)):
            if user_input == selected_word[n]:
                word_list[n] = user_input
    else:
        print("Letter not found ")
        missed_letters.append(user_input)
        pics_num += 1

    if "_" not in word_list:
        print(f"Congratulations! You've guessed the word: {selected_word}")
        game_running = False
    elif pics_num >= len(hangman_pics) - 1:
        print("You have run out of guesses! ADAM ÖLDÜ AQ")
        print(f"The word was: {selected_word}")
        game_running = False
