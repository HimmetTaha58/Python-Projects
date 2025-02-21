true_false = True
num_input = input("Enter a starting number (greater than 0) or type 'QUIT':")
num = 0
counter = 0

if num_input.lower() == "quit":
    true_false = False
elif num_input.isdigit():
    num = int(num_input)
else:
    print("Please enter a valid number or type 'QUIT' to exit.")

while true_false:
    if num == 1:
        print("Number is 1!")
        break

    if num < 0:
        print("Please enter a positive number")
        break
    elif num == 0:
        print("Please enter a number greater than 0")
        break
    else:
        if num % 2 == 0:
            num = num / 2
            counter += 1
        else:
            num = num * 3 + 1
            counter += 1
        print(f"Step: {counter}  Number: {num}")
