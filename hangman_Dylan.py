import getpass, os

os.system("clear")

play = input("Do you want to play hangman?: ").lower()
if play == 'y':
   pass
else:
   exit()

word = []
word = getpass.getpass("Please Enter Your Word: ")
length = len(word)
if len(word) > 0: pass
else:
   print("print you must enter a word")
   exit()

trys = 0
tr = 0
for i in range(0, 10):
   guess = input("-->")
   if len(guess) != 1:
      print("Must enter 1 number!!!")
      exit()
   else: pass
   if guess in word:
      tr += 1
      print("guess", guess, "is correct!")
   else:
      print("Wrong!!")
   if tr == length:
      print("word: ", word)
      exit()
   else:
      pass


