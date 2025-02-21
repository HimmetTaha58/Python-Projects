
leetspeak_dict = {
    'A': '4',
    'B': '8',
    'C': '(',
    'D': '[)',
    'E': '3',
    'F': '|=',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': '_|',
    'K': '|<',
    'L': '1',
    'M': '/\\/\\',
    'N': '|\\|',
    'O': '0',
    'P': '|*',
    'Q': '0,',
    'R': '2',
    'S': '5',
    'T': '7',
    'U': '|_|',
    'V': '\\/',
    'W': '\\/\\/',
    'X': '><',
    'Y': '`/',
    'Z': '2'
}

leeted_list = []

print("Enter your leet message:")
user_input = input(">").upper()

for i in user_input:
    if i in leetspeak_dict:
        leeted_list.append(leetspeak_dict[i])
print(' '.join(leeted_list))