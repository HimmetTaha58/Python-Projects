import random

life = 4
print("""Find the password in the computer's memory:
0x1150  $],>@|~~RESOLVE^    0x1250  {>+)<!?CHICKEN,%
0x1160  }@%_-:;/$^(|<|!(    0x1260  .][})?#@#ADDRESS
0x1170  _;)][#?<&~$~+&}}    0x1270  ,#=)>{-;/DESPITE
0x1180  %[!]{REFUGEE@?~,    0x1280  }/.}!-DISPLAY%%/
0x1190  _[^%[@}^<_+{_@$~    0x1290  =>>,:*%?_?@+{%#.
0x11a0  )?~/)+PENALTY?-=    0x12a0  >[,?*#IMPROVE@$/

""")

passwords = ["resolve", "chicken", "address", "despite", "refugee",
             "display", "penalty", "improve", "network", "monitor"]

rand_list = []
rand_word = random.choice(passwords)
for _ in rand_word:
    rand_list.append(_)
print(rand_word)

while life > 0:
    char_num = 0
    input_list = []
    user_input = input(f"{life} tries meaning. Enter Password : ")
    if user_input.lower() in passwords:
        for i in user_input:
            input_list.append(i)
        for n in range(len(input_list)):
            if rand_word[n] == input_list[n]:
                char_num += 1
        if char_num == len(rand_word):
            print("A C C E S S   G R A N T E D")
            break
        else:
            print(f"Access Denied ({char_num} / {len(rand_word)}) correct.")
            life -= 1
    else:
        print("Yanlış girdi")

    if life == 0:
        print("A C C E S S  D E N İ E D")
