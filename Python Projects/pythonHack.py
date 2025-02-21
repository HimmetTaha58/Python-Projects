# Örnek input : RJWMFGF


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = input("Please enter a text: ").upper()  # Metni büyük harfe dönüştür

for i in range(1, 26):
    new_alphabet = alphabet[i:] + alphabet[:i]
    new_text_list = []

    for char in text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_text_list.append(new_alphabet[old_index])

        else:
            print(f"Character '{char}' not found in alphabet.")
    print(f"Key {i}: {''.join(new_text_list)}")