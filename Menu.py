from tkinter import *
import random

class Scripts(object):
    def __init__(self):
        pass

    def C12(self):
        name = input("Enter Your Name: ")
        print("hello", name)

        g = input("Would you like another go?: ").lower()
        if 'y' in g:
            self.C12()

    def A2(self):
        print("Hello World!")

    def A4(self):
        name = input("Hello! What Your Name: ")
        if len(name) > 0:
            print("Oh Hello", name)

    def A6(self):
        print("This is a Program That Will Add Two Numbers")
        try:
            n1 = int(input("First Number: "))
            n2 = int(input("Second Number: "))
            print("The Sum is:", n1+n2)
        except ValueError:
            print("\nI Dont like Words, So I Wont Add Them\n")
            self.A6()

    def C14(self):
        with open("numbers.txt", "w") as file:
            for i in range(10):
                file.write(str(random.randint(1, 10)))
            file.close()
        print("Numbers Wrote To File")

    def A8(self):
        print("This is a Random Number Generator!")
        try:
            f = int(input("Enter a Number and i will get a random one between that and zero!: "))
            print("Heres a Random Number bettween 0 and {0}: {1}".format(f, random.randint(0, f)))
        except ValueError:
            print("\nI Dont Like Words\n")
            self.A8()

    def B10(self):
        names = []
        na1 = input("Name 1: ")
        na2 = input("Name 2: ")
        na3 = input("Name 3: ")
        names.append(na1)
        names.append(na2)
        names.append(na3)
        print("Name 1 Was {}".format(names[0]))
        print("Name 2 Was {}".format(names[1]))
        print("Name 3 Was {}".format(names[2]))


class Menu:

    def __init__(self, master):
        global frame, lframe
        frame = Frame(master)
        lframe = Frame(master)
        lframe.pack(side=TOP, anchor="w")
        frame.pack(side=TOP, anchor="w")
        
    def Attributes(self):
        self.text_A2 = Label(lframe, text="A2: Prints A Message On The Screen")
        self.text_A4 = Label(lframe, text="A4: Asks Your Name Then Displays it On The Screen")
        self.text_A6 = Label(lframe, text="A6: Adds Two Supplied Numbers")
        self.text_A8 = Label(lframe, text="A8: Generates a Random From 0 To Your Number")
        self.text_B10 = Label(lframe, text="B10: Ask For 3 Names Then Displays Them")
        self.text_C12 = Label(lframe, text="C12: Displays Your Name Then Asks To Go Again")
        self.text_C14 = Label(lframe, text="C14: Writes a Random Number To a File")
        self.text_A2.pack(side=TOP, anchor="w")
        self.text_A4.pack(side=TOP, anchor="w")
        self.text_A6.pack(side=TOP, anchor="w")
        self.text_A8.pack(side=TOP, anchor="w")
        self.text_B10.pack(side=TOP, anchor="w")
        self.text_C12.pack(side=TOP, anchor="w")
        self.text_C14.pack(side=TOP, anchor="w")

        def buttons():
            self.C12 = Button(frame, text="C12", fg="red", bg="white", command=Scripts().C12)
            self.C14 = Button(frame, text="C14", fg="red", bg="white", command=Scripts().C14)
            self.A2 = Button(frame, text="A2", fg="red", bg="white", command=Scripts().A2)
            self.A4 = Button(frame, text="A4", fg="red", bg="white", command=Scripts().A4)
            self.A6 = Button(frame, text="A6", fg="red", bg="white", command=Scripts().A6)
            self.A8 = Button(frame, text="A8", fg="red", bg="white", command=Scripts().A8)
            self.B10 = Button(frame, text="B10", fg="red", bg="white", command=Scripts().B10)
            self.A2.pack(side=LEFT)
            self.A4.pack(side=LEFT)
            self.A6.pack(side=LEFT)
            self.A8.pack(side=LEFT)
            self.B10.pack(side=LEFT)
            self.C12.pack(side=LEFT)
            self.C14.pack(side=LEFT)

        buttons()

root = Tk()
root.configure()
root.wm_title("Python Challange Sheet")
w = Label(root, font = "Verdana 10 bold", text="Select The Script You Want To Run")
w.pack()

app = Menu(root).Attributes()

root.mainloop()
root.destroy()
