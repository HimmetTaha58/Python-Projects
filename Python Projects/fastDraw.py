import time, random

score = 0
true_false = True
while true_false:
    print()
    print('It is high noon...')
    time.sleep(random.randint(20, 50) / 10.0)
    print('DRAW!')
    first_time = time.time()
    input()
    last_time = time.time()

    result_time = last_time - first_time

    if result_time > 0.3:
        print("Lose")
        break
    else:
        print(f"You are fast! Score : {score}")
        score += 1
