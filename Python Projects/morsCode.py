morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'

}

print("""Welcome to the Morse Code Translator!
Please select an option:
1. Encode text to Morse code
2. Decode Morse code to text
3. Exit
""")

loop_running = True
while loop_running:

    mors_list = []
    text_list = []

    user_choice = input("Enter your choice :")
    if user_choice.isdigit():

        choice_num = int(user_choice)
        if choice_num == 1:

            text_mors = input("Enter the text you want to encode :")

            for i in text_mors:

                if i.upper() in morse_code_dict:

                    mors_value = morse_code_dict[i.upper()]
                    mors_list.append(mors_value)

            print(' '.join(mors_list))


        elif choice_num == 2:
            mors_text = input(
                "Enter the Morse code you want to decode (use space between letters and / for space between words): ")
            words = mors_text.split(' / ')

            for word in words:
                letters = word.split()

                for letter in letters:

                    for key, value in morse_code_dict.items():

                        if letter == value:
                            text_list.append(key)

                text_list.append(' ')

            print(''.join(text_list).strip())

        elif choice_num == 3:

            print("\nQuitting")
            loop_running = False

        else:
            print("Please enter a valid number")
    else:
        print("Please enter a number")