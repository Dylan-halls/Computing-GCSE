import sys
import random

firstname = random.choice(["ra-", "we-", "ht-", "ks-", "yg-", "vf-"])
lastname = random.choice(["gr", "rg", "ge", "ev", "hw", "ld"])
clas = random.choice(["Worrior", "Soilder", "Prince", "Knight"])
gender = random.choice(["Male", "Female", "Dragon", "Ogre"])
trade = random.choice(["Builder", "Carpenter", "Blacksmith"])

#Attributes
dexterity = int(input("Dexterity>>> "))
strength = int(input("Strength>>> "))
speed = int(input("Speed>>> "))

print("\nYour name is: ", end='')
print("%s%s" % (firstname, lastname), file=sys.stderr)
print("Your gender is: ", end='')
print("%s" % (gender), file=sys.stderr)
print("Your class is: ", end='')
print("%s" % (trade), file=sys.stderr)

