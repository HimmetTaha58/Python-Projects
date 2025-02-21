import random


game_running = True
while game_running:
    num = random.randint(1, 100)
    guessed_nums = []
    print("1 ile 100 arasında bir sayı düşünüyorum...")

    life = 10

    while True:
        print(f"You have {life} guesses left. Take a guess.")
        try:
            user_guess = int(input("> "))
        except ValueError:
            print("Geçerli bir sayı girin.")
            continue

        if user_guess in guessed_nums:
            print("Sayıyı daha önce tahmin ettiniz")
            continue

        if user_guess == num:
            if life == 10:
                print("Tekte bildin helal olsun !")
            else:
                print("Sayıyı doğru bildin")

            to_continue = input("Devam etmek istiyormuusn ( y / n )")
            if to_continue.lower() == "y":
                break
            elif to_continue.lower() == "n":
                game_running = False
                break
            else:
                print("Geçerli harf girin")
                continue
        else:
            if user_guess > num:
                print("Tahmininiz büyük")

            else:
                print("Tahmininiz küçük")
            guessed_nums.append(user_guess)
            life -= 1


        if life == 0:
            print("Hayatınız kalmadı, oyun bitti!")
            to_continue = input("Tekrar oynamak ister misiniz? (y/n) ")
            if to_continue.lower() == "y":
                print()
                break
            else:
                game_running = False
            break

