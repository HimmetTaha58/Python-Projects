print("Please enter (Q)uit to quit")

loop_running = True
while loop_running:
    menu_dict = {1: 3.50, 2: 2.50, 3: 4.00, 4: 3.50, 5: 1.75, 6: 1.50, 7: 2.25, 8: 3.75, 9: 1.25}
    barcode_list = []
    money_count = 0

    barcode_input = input("Enter barcode :")



    if barcode_input.isdigit():
        for i in barcode_input:
            barcode_list.append(i)
        for n in range(1, 10):
            count_value = barcode_list.count(str(n))
            money_count += count_value * menu_dict[n]
        print(money_count)
    elif barcode_input.lower() == "q":
        print("Quitting..")
        loop_running = False
    else:
        print("Please enter a valid num")
        continue





