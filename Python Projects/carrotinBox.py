import random
import os

user1 = input("Birinci oyuncu isminizi girin :")
user2 = input("İkinci oyuncu isminizi giriniz :")

user1_score = 0
user2_score = 0

box_art = f"""
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
   {user1}           {user2}
"""
print(box_art)

true_false = True
while true_false:

    input('When ' + user2 + ' has closed their eyes, press Enter...')

    red_box = 0
    gold_box = 0
    random1 = random.randint(1, 2)
    if random1 == 1:
        print(f"{user1} here is the inside of your box:")
        red_box = 1
        gold_box = 0
        box_art_carrot = """
       ___VV____        __________
      |   VV   |      /         /|
      |   VV   |     +---------+ |
      |___||___|     |   GOLD  | |
     /    ||   /|    |   BOX   | /
    +---------+ |    +---------+/
    |   RED   | |
    |   BOX   | /
    +---------+/  
        """

        print(box_art_carrot)

    else:
        print(f"{user1} here is the inside of your box:")
        red_box = 0
        gold_box = 1
        box_art_no_carrot = """
       ----------
       |         |        __________
       |         |       /         /|
       |_________|      +---------+ |
      /         /|      |   GOLD  | |
     +---------+ |      |   BOX   | /
     |   RED   | /      +---------+/
     |   BOX   |/
     +---------+/  

    """
        print(box_art_no_carrot)

    input("Press enter to continue")
    print(box_art)

    takas_input = input(f"{user2} do you want to change box ( y / n )?")

    if takas_input.lower() == "y":
        if red_box == 1:
            print("Havuç kırmızı kutuda kazandınız")
            user2_score += 1
        else:
            print("Havuç sizin kutunuzdaydı kaybettiniz")
            user1_score += 1
    else:
        if gold_box == 1:
            print("Havuç gold kutuda kazandınız")
            user2_score += 1
        else:
            print("Havuç kırmızıdaydı kaybettiniz")
            user1_score += 1

    print(f"Puanlar : Oyuncu1 : {user1_score} , Oyuncu2 : {user2_score} ")
    print("")
    to_continue = input("Tekrar oynamak istiyormusunuz ? ( y / n )")

    if to_continue.lower() == "n":
        true_false = False
