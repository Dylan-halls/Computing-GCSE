import getpass

file = open('passwords.txt')
s = file.read()
sp = s.splitlines()

u = s.find(':')
o = u + 1
b = u + 1

usr = s[:b].split()[0]
pas = s[o:].split()[0]

user = input("Username: ")
try:
    if user == usr:
        pass
    else:
        print("No Users Called", user)

    password = input("Password: ")
    if password == pas:
        pass
    else:
        print("Password Does Not Match!")

    npass = getpass.getpass("New Password: ")

    while len(npass) <= 0:
        print("Must Enter a Password!")
        npass = getpass.getpass("New Password: ")

    del sp[0]
    file.close()
    wfile = open('passwords.txt', 'w')
    print(file)
    wfile.write(user + " : " + npass)
    wfile.close()
    print('written')


except IOError:
    print("ERROR: Could not find password file")


