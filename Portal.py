from tkinter import *

with open ("Info.txt",'r') as r:
    text = str(r.read())
try:
    exec("ID_list = {}".format(text))
except:
    ID_list = []
    
root = Tk()
root.geometry("600x600")
root.title("LOGIN PORTAL")

ID_read = 0

def pass_check(string):
    low = 0
    up = 0
    digit = 0
    String = list(string)
    for i in range(len(String)):
        if String[i].islower():
            low = 1
        if String[i].isupper():
            up = 1
        if String[i].isdigit():
            digit = 1
    if low==up==digit==1:
        return True
    else:
        return False

def get_data():
    global IdIndex,ID_read
    if ID_read == 1:
        data = txt.get(0.0,END)
        ID_list[IdIndex][2] = data
        with open ("Info.txt",'w') as w:
            w.write(str(ID_list))
def user_data():
    ID = Id.get()
    PASS = Pass.get()
    validity = 0
    for a in range(len(ID_list)):
        if ID == ID_list[a][0]:
            validity = 1
            if PASS == ID_list[a][1]:
                global IdIndex
                IdIndex = a
                txt.delete(0.0,END)
                Fg = "green"
                Text = "Logged In\nSuccesfully"
                txt.insert(0.0,ID_list[a][2])
                ShowText()
                global ID_read
                ID_read = 1
            else:
                Fg = "red"
                Text = "Invalid\nPassword"
        else:
            reg['fg'] = "red"
            reg['text'] = "Invalid\nUsername"
    if validity == 1:
        reg['fg'] = Fg
        reg['text'] = Text
            
def LogOut():
    HideText()
    global ID_read
    ID_read = 0
    txt.delete(0.0,END)
    Id.delete(0,END)
    Pass.delete(0,END)
    reg['text'] = ""
    
def HideText():
    txt.place(x=1000,y=1000)
    b1.place(x=1000,y=1000)
def ShowText():
    txt.place(x=0,y=120)
    b1.place(x=250,y=545)

def ChangePortal(Pos):
    if HyperText['text'] == "Register Now":
        global RegRules
        LogOut()
        login.place(x=1000,y=1000)
        logout.place(x=1000,y=1000)
        regButton.place(x=200,y=80)
        HyperText['text'] = "Login Now"
        regInfo['text'] = RegRules
    else:
        login.place(x=150,y=75)
        logout.place(x=250,y=75)
        regButton.place(x=1000,y=1000)
        HyperText['text'] = "Register Now"
        regInfo['text'] = ""
        regStat['text'] = ""
def Register():
    ID = Id.get()
    PASS = Pass.get()
    valid = pass_check(PASS)

    old_Ids=[ID_list[a][0] for a in range(len(ID_list))]

    regCheck=""
    regStat['fg'] = "red"
    if len(ID)<8:
        regCheck="Atleast 8 Characters Required in USERNAME"
    elif ID in old_Ids:
        regCheck="USERNAME already exists"
        
    elif len(PASS)<8:
        regCheck="Atleast 8 Characters Required in PASSWORD"
    elif valid == False:
        regCheck = "Password should contain uppercase, lowercase and digits"

    else:
        regCheck = "Registered Succesfully....Login Now"
        regStat['fg'] = "green"
        myList = [ID,PASS,""]
        ID_list.append(myList)
        with open ("Info.txt",'w') as w:
            w.write(str(ID_list))

    regStat['text'] = regCheck
    
HyperText = Label(root,font=("Arial",12,"normal"),text="Register Now",fg="blue")
HyperText.place(x=425,y=85)
HyperText.bind("<Button-1>",ChangePortal)

reg = Label(root,font=("Arial",16,"italic"),text="",fg="red")
reg.place(y=5,x=400)

RegRules="""For USERNAME :-
1. It should contain atleast 8 characters.

For PASSWORD :-
1. It should contain atleast 8 characters.
2. It shoud have atleast One uppercase,
   One lowercase and One digit.
"""

regInfo = Label(root,font=("Arial",13,"normal"),text="",fg="purple")
regInfo.place(x=100,y=250)

regStat = Label(root,font=("Ubuntu",16,"bold"),text="",fg="red")
regStat.place(x=10,y=125)

regButton = Button(root,text="Register",font=("Ubuntu",12,'bold'),bg="green",fg="white",command=Register)
regButton.place(x=1000,y=1000)
    
l1 = Label(root,font=("Ubuntu",12,"normal"),text="USERNAME :")
l1.place(y=7,x=3)
Id = Entry(root,width=30,font=("Courier",10,"normal"))
Id.place(x=120,y=10)

l2 = Label(root,font=("Ubuntu",12,"normal"),text="PASSWORD :")
l2.place(y=37,x=3)
Pass = Entry(root,width=30,font=("Courier",10,"normal"))
Pass.place(x=120,y=40)

login = Button(root,text="LOG IN",font=("Ubuntu",12,'bold'),bg="blue",fg="white",command=user_data)
login.place(x=150,y=75)
logout = Button(root,text="LOG OUT",font=("Ubuntu",12,'bold'),bg="red",fg="white",command=LogOut)
logout.place(x=250,y=75)

b1 = Button(root,text="SAVE",font=("Ubuntu",15,'bold'),bg="yellow",fg="red",command=get_data)
b1.place(x=1000,y=1000)

txt = Text(root,font=("Arial",12,'italic'),width=66,height=22,wrap=WORD)
HideText()

root.mainloop()
