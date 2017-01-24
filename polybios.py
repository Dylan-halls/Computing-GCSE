#!/usr/bin/env python3

import sys

class Polybios_Encode(object):
	def __init__(self):
		global dic
		#Database
		dic = {'a':'11',
		'b':'12',
		'c':'13',
		'd':'14',
		'e':'15',
		'f':'16',
		'g':'21',
		'h':'22',
		'i':'23',
		'j':'24',
		'k':'25',
		'l':'26',
		'm':'31',
		'n':'32',
		'o':'33',
		'p':'34',
		'q':'35',
		'r':'36',
		's':'41',
		't':'42',
		'u':'43',
		'v':'44',
		'w':'45',
		'x':'46',
		'y':'51',
		'z':'52',
		'1':'53',
		'2':'54',
		'3':'55',
		'4':'56',
		'5':'61',
		'6':'62',
		'7':'63',
		'8':'64',
		'9':'65',
		'0':'66'}
	
	def ecode_str(self, data):
		data = data.replace(' ', '')
		encoded = []
		for i in data:
			encoded.append(dic[i])
		print("Encoded Without Cipher --> ", ''.join(encoded))
		return ''.join(encoded)

	def ecode_cip(self, cipher):
		ciphr = []
		for x in cipher:
			ciphr.append(dic[x])
		print("Encoded Cipher --> ", ''.join(ciphr))
		return ''.join(ciphr)

class Polybios_Decode(object):
	def __init__(self):
		global d_dic
		d_dic = {'11':'a',
		'12':'b',
		'13':'c',
		'14':'d',
		'15':'e',
		'16':'f',
		'21':'g',
		'22':'h',
		'23':'i',
		'24':'j',
		'25':'k',
		'26':'l',
		'31':'m',
		'32':'n',
		'33':'o',
		'34':'p',
		'35':'q',
		'36':'r',
		'41':'s',
		'42':'t',
		'43':'u',
		'44':'v',
		'45':'w',
		'46':'x',
		'51':'y',
		'52':'z',
		'53':'1',
		'54':'2',
		'55':'3',
		'56':'4',
		'61':'5',
		'62':'6',
		'63':'7',
		'64':'8',
		'65':'9',
		'66':'0'}

	def decode(self, data, cipher=''):
		p = Polybios_Encode()
		cipher = p.ecode_cip(cipher)
		data = int(data)-int(cipher)
		data = str(data)
		data = iter(list(data))
		decoded = []
		for i in data:
			i = i+next(data)
			decoded.append(d_dic[i])
		try:
			print("Decoded --> ", ''.join(decoded))
		except NameError: pass
		return ''.join(decoded)

def full_decode():
	p = Polybios_Decode()
	hh = input("String >>> ")
	cc = input("Cipher >>> ")
	de = p.decode(hh, cipher=cc)
	try:
		print("Decoded With Cipher --> ", full_str)
	except NameError: pass

def full_encode():
	p = Polybios_Encode()
	hh = input("String >>> ")
	cc = input("Cipher >>> ")
	de = p.ecode_str(hh)
	ci = p.ecode_cip(cc)
	full_str = int(de)+int(ci)
	print("Ecoded With Cipher --> ", full_str)

if __name__ == '__main__':
	ch = input("Encode or Decode?[E/D]: ").lower()
	if ch == 'e':
		full_encode()
	elif ch == 'd':
		full_decode()