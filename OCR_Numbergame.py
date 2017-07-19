import random
import sys
import os

player1_name = ""
player2_name = ""
player1_pos = 0
player2_pos = 0

def show_board(position):
	endnums = [7, 14, 21, 28, 35, 42, 49]
	for i in range(1, 50):
		if len(str(i)) > 1:
			sys.stdout.write("| ")
		else:
			sys.stdout.write("|  ")
		if i in endnums:
			if position == i:
				sys.stdout.write("\033[1;35m{} \033[00m| \n".format(i))
			else:
				sys.stdout.write("{} |\n".format(i))
		else:
			if position == i:
				sys.stdout.write("\033[1;35m{} \033[00m|".format(i))
			else:
				sys.stdout.write("{} |".format(i))	
				
def greet():
	print("Welcome to the dice game")

def diceroll():
	return random.randint(1, 6) + random.randint(1, 6)

print(greet())
while True:
	input()
	#show_board(player1_pos + diceroll())
	player1_pos = player1_pos + diceroll()
	show_board(player1_pos)
	if player1_pos >= 49: exit()
