import time
import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as tkMessageBox

class Minesweeper(tk.Frame):
	"""Minesweeper game"""
	def __init__(self, master=None):
		super(Minesweeper, self).__init__()
		ttk.Frame.__init__(self, master)
		inc = 0
		self.bomb = random.randint(1, 20)
		print(self.bomb)
		for y in range(5):
			for x in range(4):
				inc += 1
				if (inc == self.bomb):
					self.bomb_button = tk.Button(self, text='', height=2, width=5, command=self.bomb_change)
					self.bomb_button.grid(row=y, column=x)
				else:
					self.button = tk.Button(self, text='', height=2, width=5)
					self.button.grid(row=y, column=x)
		self.pack()
	
	def bomb_change(self):
		self.bomb_button.configure(activebackground="red", bg="red")
		tkMessageBox.showerror("Game Over", "Game Over")
		exit()

if __name__ == '__main__':
	mine = Minesweeper()
	mine.master.title("Minesweeper")
	mine.mainloop()