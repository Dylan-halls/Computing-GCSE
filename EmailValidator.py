import re

def match(data):
    remail = '[a-zA-Z0-9.-]+[@][a-zA-Z0-9.-]+[.][a-zA-Z0-9.-]+'
    ree = re.compile(remail)
    ree.match(data)

def getaddr():
    email = input("Email>>> ")
    return email

email = getaddr()
if match(email) == None:
    print("Passed")
