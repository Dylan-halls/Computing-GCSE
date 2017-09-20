#!/usr/bin/env python3

import crypt
import base64

"""
ps_hash = hashpassword("dylan")
psalt = getsalt(ps_hash)
check_hash(ps_hash, "dylan", psalt)
"""

def writetofile(username, password):
	with open("password.txt", "a") as file:
		username = base64.b64encode(username.encode('utf-8'))
		file.write("{0}:{1}".format(username.decode('utf-8'), password))

def hashpassword(password):
	return crypt.crypt(password, crypt.mksalt())+"\n"
	
def check_hash(phash, password, salt):
	new_hash = crypt.crypt(password, salt)
	
	if new_hash == phash.strip('\n'):
		return True
	else:
		return False
	
def auth(username, password, tpe):
	username = base64.b64encode(username.encode('utf-8'))
	with open("password.txt", "r") as file:
		data = file.readlines()
		for i in data:
			line = ''.join(i)
			uname, pass_hash = line.split(":")
			if tpe == "user":
				if uname == username.decode('utf-8'):
					return True
			if tpe == "hash":
				psalt = getsalt(pass_hash)
				return check_hash(pass_hash, password, psalt)
				
def getsalt(phash):
	c = 0
	for i in range(0, len(phash)):
		if phash[i] == '$':
			c += 1
		if c == 3:
			return phash[:i]

			
user = input("Username>>> ")
password = input("Password>>> ")
if auth(user, None, "user") == True:
	if auth(user, password, "hash") == True:
		print("Logged in")

else:
	print("Registered")
	writetofile(user, hashpassword(password))
