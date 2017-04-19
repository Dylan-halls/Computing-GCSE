import json
import random

def __init__():
    global data
    data = {}
    try:
        with open('mastermind.txt', 'r') as file:
            tab = json.load(file)
            for i in tab:
                print(tab[i])
    except: pass

__init__()

def greet():
    print("Hello welcome to mastermind")

    name = input("What is your name: ")
    
    print("\nEasy -> 1\nHard -> 2")
    lev = int(input("\nLevel: "))

    return lev, name

def getnum(numcount=None):
    nlist = []
    for i in range(numcount):
        num = random.randint(1, 9)
        nlist.append(str(num))
    return int(''.join(nlist))

level, name = greet()

if level is 1:
    print("You are playing easy mode... I will show you your correct digit you guessed\n")
    random_num = getnum(numcount=4)
if level is 2:
    random_num = getnum(numcount=5)

guess = ''
trys = 0
while True:
    guess = input("Guess>>> ")
    trys += 1
    if level is 1:
        if len(guess) != 4:
            print("Invalid length number!!")
            trys -= 1
            continue
    elif level is 2:
        if len(guess) != 5:
            print("Invalid length number!!")
            trys -= 1
            continue
    if level is 1 and int(guess) != int(random_num):
        for i in list(map(str, guess)):
            if i == str(random_num)[0]:
                print("Your guess,",i,"is at the first digit in the number")
            if i == str(random_num)[1]:
                print("Your guess,",i,"is at the second digit in the number")
            if i == str(random_num)[2]:
                print("Your guess,",i,"is at the third digit in the number")
            if i == str(random_num)[3]:
                print("Your guess,",i,"is at the fourth digit in the number")
    elif level is 2:
        pass
    if int(guess) == int(random_num):
        print("Congratulations!!!", guess, "is the correct number :-)\nYou had",trys,"attampts")
        data[name] = trys
        with open('mastermind.txt', 'w') as file:
            json.dump(data, file)
        exit()
