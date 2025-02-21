import random

def shuffle_alphabet(shift: int):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shuffled_alphabet = alphabet[shift:] + alphabet[:shift]
    return shuffled_alphabet


def caesar_cipher(text: str, shift: int, mode: str):
    if mode.lower() == "decrypt":
        shift = -shift

    shuffled_alphabet = shuffle_alphabet(shift)
    result = ""

    for char in text:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            index = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char)
            result += shuffled_alphabet[index]
        else:
            result += char

    return result


if __name__ == "__main__":
    mode = input("Do you want to (e)ncrypt or (d)ecrypt? :")
    key = int(input("Please enter the key (0 to 25) to use: "))
    text = input("Enter the message to encrypt/decrypt: ")

    if mode.lower() == "e":
        print(caesar_cipher(text, key, mode))
    else:
        print(caesar_cipher(text, key, mode))