loop_running = True
while loop_running:
    count = 1
    user_input = int(input("Faktöriyeli alınacak sayıyı girin:"))
    for i in range(user_input):
        count += count * i
    print(count)
