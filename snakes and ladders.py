import random, time, sys

player = 0

"""
Start 
"""

while True:
   
   # Start the timmer
   
    start_time = time.time()
    if player <= 100:
       print("Your score is:", player)
       input("Press any key to play...")
       role1 = random.randint(1,6)
       player += role1
       print("\033[1;31mRole 1:", role1, "\033[00m")
       role2 = random.randint(1,6)
       player += role2
       print("\033[1;31mRole 2:", role2, "\033[00m")

       #snakes
   
       if player == 99:
           player = 0
           #print it in a nice color
           print("[\033[1;33mHit a Snake!!! Your Score is: {}\033[00m]".format(player))
       elif player == 5:
           player = 0
           print("[\033[1;33mHit a Snake!!! Your Score is: {}\033[00m]".format(player))
       elif player == 19:
           player = 0
           print("[\033[1;33mHit a Snake!!! Your Score is: {}\033[00m]".format(player))
       elif player == 58:
           player = 0
           print("[\033[1;33mHit a Snake!!! Your Score is: {}\033[00m]".format(player))
       elif player == 73:
           player = 0
           print("[\033[1;33mHit a Snake!!! Your Score is: {}\033[00m]".format(player))
       elif player == 49:
           player = 0
           print("[\033[1;33mHit a Snake!!! Your Score is: {}\033[00m]".format(player))
       #ladders
       elif player == 7:
           player = 47
           print("[\033[1;32mHit a Ladder!!! Your Score is: {}\033[00m]".format(player))
       elif player == 59:
           player = 98
           print("[\033[1;32mHit a Ladder!!! Your Score is: {}\033[00m]".format(player))
       elif player == 39:
           player = 89
           print("[\033[1;32mHit a Ladder!!! Your Score is: {}\033[00m]".format(player))
    else:
        # stop the timmer
        time = time.time() - start_time
        print("\n\n\033[1;45mYou Win!!! your played for:", time, "\033[00m")
        break


