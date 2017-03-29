from statistics import *

class Commands(object):
	def __init__(self):
		pass

	def mode(self, numbers):
		l = []
		numbers = numbers.replace(",", ' ')
		for i in numbers:
			if i == ' ':
				pass
			else:
				l.append(int(i))
		try:
			print(mode(l))
		except:
			print("ERROR: More than one mode ")
			pass

	def average(self, numbers):
		l = []
		numbers = numbers.replace(",", ' ')
		for i in numbers:
			if i == ' ':
				pass
			else:
				l.append(int(i))
		print(max(l) - min(l))

	def median(self, numbers):
		l = []
		numbers = numbers.replace(",", ' ')
		for i in numbers:
			if i == ' ':
				pass
			else:
				l.append(int(i))
		print(median(l))

	def mean(self, numbers):
		l = []
		numbers = numbers.replace(",", ' ')
		for i in numbers:
			if i == ' ':
				pass
			else:
				l.append(int(i))
		print(mean(l))

	def help(self):
		help = """
	help - shows this help menu
	mean, median, average, mode - one argument of your list

	example:
		mean 7,8,2,5
			   """
		print(help)

	def check(self, arg):
		cmds = ['mode', 'average', 'median', 'mean', 'help']
		for i in cmds:
			if i in arg:
				return True
		
class Interface(object):
	"""This is the interface to accept the cmds"""
	def __init__(self):
		super(Interface, self).__init__()
		pass

	def accept(self):
		cmd = input("statistics>>> ")
		return cmd

	def _run_cmd(self, cmd):
		c = Commands()
		if 'mode' in cmd:
			c.mode(cmd[5:])
		elif 'average' in cmd:
			c.average(cmd[8:])
		elif 'median' in cmd:
			c.median(cmd[7:])
		elif 'mean' in cmd:
			c.mean(cmd[5:])
		elif 'help' in cmd:
			c.help()

if __name__ == '__main__':
	i = Interface()
	c = Commands()
	
	while True:
		try:
			cmd = i.accept()
			if c.check(cmd) == True:
				i._run_cmd(cmd)
		except KeyboardInterrupt:
			print(" ")
			exit()