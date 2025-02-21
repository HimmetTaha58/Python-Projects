import math

user_input = input("Bir sayı girin: ")

if user_input.isdigit():
    sayi = int(user_input)
    sayi_sqrt = math.isqrt(sayi)
    factors = []

    for i in range(1, sayi_sqrt + 1):
        if sayi % i == 0:
            factors.append(i)
            if i != sayi // i:
                factors.append(sayi // i)

    factors.sort()
    print("Çarpanlar:", factors)
else:
    print("Geçersiz giriş. Lütfen bir sayı girin.")
