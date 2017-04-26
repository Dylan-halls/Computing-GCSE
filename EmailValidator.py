import re

def greet():
    print("1  -  Single email\n2  -  Text file with emails\n")
    return int(input("[CHOICE] ")) 

def match(data):
    remail = '[a-zA-Z0-9.-]+[@][a-zA-Z0-9.-]+[.][a-zA-Z0-9]+'
    ree = re.compile(remail)
    match = ree.match(data)
    return match

def getaddr():
    email = input("\nEmail>>> ")
    return email

def finderror(data):
    regexat = '[a-zA-Z0-9.-]+[@]'
    cregexat = re.compile(regexat)
    if cregexat.match(data) != None:
        at = True
    else:
        at = False
    regexdomain = '[a-zA-Z0-9.-]+[@][a-zA-Z0-9.-]'
    cregexdomain = re.compile(regexdomain)
    if cregexdomain.match(data) != None:
        domain = True
    else:
        domain = False
    topdomain = '[a-zA-Z0-9.-]+[@][a-zA-Z0-9.-]+[.][a-zA-Z0-9]+'
    ctopdomain = re.compile(topdomain)
    if ctopdomain.match(data) != None:
        topdomain = True
    else:
        topdomain = False
    return at, domain, topdomain

def single():
    email = getaddr()
    if match(email) != None:
        print("Passed")
    else:
        at, domain, topdomain = finderror(email)
        try:
            if at == True: pass
            else: print("Email must have '@' symbol")
            if domain== True : pass
            else: print("Email must have a domain")
            if topdomain == True : pass
            else: print("Email must have a top level domain")
        except:
            pass

def multi(text_file):
    with open(text_file, 'r') as file:
        rfile = file.readlines()
        file.close()
    p = 0
    f = []
    for i in rfile:
        if match(i) != None:
            p += 1
        else:
            f.append(i)

    print("\nEmails passed:", p)
    print("Failed:\n", ''.join(f))
    
        

while True:
    choice = greet()
    if choice == 1:
        single()
        break
    elif choice == 2:
        f = input("Email File: ")
        multi(f)
        break
    else:
        print("\nMust Choose Vaild Option!\n")
        continue
