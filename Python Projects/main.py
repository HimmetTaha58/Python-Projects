import random

num = str(random.randint(100, 999))
life = 30

print('''I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
You have 10 guesses to get it.''')


while life > 0:
    user_input = input("Tahmininizi giriniz: ")

    if len(user_input) != 3:
        print("Lütfen 3 basamaklı bir sayı girin.")
        continue

    if not user_input.isdigit():
        print("Lütfen sadece sayılardan oluşan bir değer girin.")
        continue

    input_list = []
    feedback = []

    for index in range(len(user_input)):
        input_list.append(user_input[index])

        if input_list[index] == num[index]:
            feedback.append("Fermi")
        elif input_list[index] in num:
            feedback.append("Pico")
        else:
            feedback.append("Bagels")
            life -= 1

    if ''.join(input_list) == num:
        print("Oyunu kazandınız")
        break

    print(" ".join(feedback))

    life -= 1
