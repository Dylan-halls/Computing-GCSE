import random, sys

grd = list("""
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
""")

def grid():
    spot1 = random.randint(0, 100)
    spot2 = random.randint(0, 100)
    spot3 = random.randint(0, 100)
    spot4 = random.randint(0, 100)
    spot5 = random.randint(0, 100)
    spot6 = random.randint(0, 100)
    spot7 = random.randint(0, 100)
    spot8 = random.randint(0, 100)
    spot9 = random.randint(0, 100)
    spot10 = random.randint(0, 100)

    g = grd[spot1]='*'
    g = grd[spot2]='*'
    g = grd[spot3]='*'
    g = grd[spot4]='*'
    g = grd[spot5]='*'
    g = grd[spot6]='*'
    g = grd[spot7]='*'
    g = grd[spot8]='*'
    g = grd[spot9]='*'
    g = grd[spot10]='*'

    print(' '.join(grd))

def shooter(x, y):
    f = x+y
    b = int(f)
    if grd[b] == '*':
        print("HIT!!")
    else:
        print("MISSED")

def choice():
    while True:
        x = input("x coodinate >>>")
        y = input("y coodinate >>>")
        shooter(x, y)

grid()
choice()
