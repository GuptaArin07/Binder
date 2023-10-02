from tkinter import *
import random
import pickle
import os


os.system("clear")

#creating the main window
mainwin = Tk()
mainwin.title("Binder")
mainwin.geometry("1500x900")
Label(mainwin, text = "BINDER", font='san-serif 56 bold').pack()
mainwin.resizable(1,1)
photo = PhotoImage(file = "BinderLogo.png")
mainwin.iconphoto(False,photo)




def Passcreate(length):
    password = ""
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "<", ">","-"]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    calphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    nums = ["0","1","2","3","4","5","6","7","8","9"]

    for i in range(length):
        choose = random.randint(1,4)
        if choose == 1:
            password += symbols[random.randint(0,len(symbols)-1)]
        if choose == 2:
            password += alphabet[random.randint(0,len(alphabet)-1)]
        if choose == 3:
            password += calphabet[random.randint(0,len(calphabet)-1)]
        if choose == 4:
            password += nums[random.randint(0,len(nums)-1)]
    return password

def PCwin_create():
    PCwin = Tk()
    PCwin.geometry("500x300")
    PCwin.resizable(0,0)
    PCwin.title("Password Creator - Binder")
    password = Passcreate(12)
    Label(PCwin, text ="Your Password is: " + password, font='san-serif 16 bold').place(x=0,y=0)


Button(mainwin, text = "Random Password Generator", font='san-serif 16 bold', command=PCwin_create).place(x = 650, y = 350)

def Plist_create():
    Plist = Tk()
    Plist.geometry("1000x600")
    Plist.resizable(0,0)
    Plist.title("Password List - Binder")

Button(mainwin, text = "Password List", font='san-serif 16 bold', command=Plist_create).place(x = 650, y = 250)


def Contact_list():
    Clist = Tk()
    Clist.geometry("1000x600")
    Clist.resizable(0,0)
    Clist.title("Contact List - Binder")

Button(mainwin, text = "Contact List", font='san-serif 16 bold', command=Contact_list).place(x = 650, y = 550)


def CC():
    CC = Tk()
    CC.geometry("1000x600")
    CC.resizable(0,0)
    CC.title("Create Contact - Binder")
   
Button(mainwin, text = "Create Contact", font='san-serif 16 bold', command=CC).place(x = 650, y = 650)

def NP():
    global notes
    NP = Tk()
    NP.geometry("1000x600")
    NP.resizable(0,0)
    NP.title("Notepad - Binder")
    Label(NP, text = 'Warning: Binder Notes cannot be edited once saved', font='san-serif 32 bold').pack()
    notes = Text(NP,width = 70, height = 150, pady = 20)
    #mynote = notes.get("1.0", 'end-1c')
    notes.pack()
    Button(NP, text = "Save", font = 'san-serif 32 bold', command = savetxt).place(x = 800, y =150)
    Button(NP, text = "Cancel", font = 'san-serif 32 bold', command = NP.destroy).place(x = 800, y = 250)
    Button(NP, text = "Load", font = 'san-serif 32 bold', command = loadtxt).place(x = 800, y =350)
    #print(notes.get("1.0", 'end-1c'))
    #notes.pack()


Button(mainwin, text = "Notepad", font='san-serif 16 bold', command=NP).place(x = 650, y = 150)


def savetxt():
    #pickle.dump(str(mynote), open("notes.txt", "w"))
    mynote = notes.get("1.0", 'end-1c')
    f = open("notes.txt", "w")
    f.write(str(mynote))
    f.close()

def loadtxt():
    txtx = Tk()
    txtx.geometry("1000x600")
    txtx.resizable(0,0)
    txtx.title("Saved Note - Binder")
    note = open("notes.txt")
    Label(txtx, text = note.read(), font='san-serif 32 bold').pack()
   
   

def coin():
    co = Tk()
    co.geometry("500x300")
    co.title("Coin Flip - Binder")
    co.resizable(0,0)
    outcome = random.randint(0,1)
    if outcome == 1:
        outcome = "Heads"
    elif outcome == 0:
        outcome = "Tails"
    Label(co, text = outcome, font='san-serif 36 bold').pack()

Button(mainwin, text = "Coin Flip", font = "san-serif 16 bold", command = coin).place(x = 650, y = 750)

def dice():
    diy = Tk()
    diy.geometry("500x300")
    diy.title("Dice Roll - Binder")
    diy.resizable(0,0)
    droll = random.randint(1,6)
    Label(diy, text = droll, font = "san-serif 36 bold").pack()

Button(mainwin, text = "Dice Roll", font = 'san-serif 16 bold', command = dice).place(x = 650, y = 850)

def addpass():
    ap = Tk()
    ap.geometry("1000x600")
    ap.title("Add Password - Binder")
    ap.resizable(0,0)

Button(mainwin, text = "Add To Password List", font = "san-serif 16 bold", command = addpass).place(x = 650, y = 450)

#it was at this point he realized: CLASSES
