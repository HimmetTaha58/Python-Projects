import re ,random

user_input = input("Girdi:")

match = re.match(r"(\d+)d(\d+)", user_input)

if match:
    first_number = match.group(1)
    second_number = match.group(2)

    for i in range(int(first_number)):
        random_num = random.randint(1, int(second_number))
        print(random_num, end=" ")


else:
    print("Girdi formatı hatalı!")



