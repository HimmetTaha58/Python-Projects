num_list = []

true_false = True
while true_false:
    user_input = input("""Enter the Nth Fibonacci number you wish to calculate
     (such as 5, 50, 1000, 9999), or QUIT to quit: """)

    if user_input.lower() == "quit":
        break
    else:
        num = int(user_input)
        num_list = [0, 1]
        for i in range(2, num):
            num_list.append(num_list[-1] + num_list[-2])

        print(num_list)


