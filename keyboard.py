from tkinter import *
import GUI

############## Keyboard Section #################

keyboard_ABC_frame = Frame(
    GUI.description_canvas,
    bg="#444444",
    height=640,
    width=1551,
    bd=0,
    highlightthickness=0,
    relief="ridge")

keyboard_ABC_frame.place(x=0, y=600)

keyboard_ABC_canvas = Canvas(
    keyboard_ABC_frame,
    bg="#FFFFFF",
    height=640,
    width=1551,
    bd=0,
    highlightthickness=0,
    relief="ridge")

keyboard_ABC_canvas.pack()
keyboard_ABC_canvas.place(x=0, y=0)

keyboard_123_frame = Frame(
    GUI.description_canvas,
    bg="#444444",
    height=640,
    width=1551,
    bd=0,
    highlightthickness=0,
    relief="ridge")

keyboard_123_frame.place(x=0, y=600)

keyboard_123_canvas = Canvas(
    keyboard_123_frame,
    bg="#FFFFFF",
    height=640,
    width=1551,
    bd=0,
    highlightthickness=0,
    relief="ridge")

keyboard_123_canvas.pack()
keyboard_123_canvas.place(x=0, y=0)

textInput = StringVar()

displayText = Entry(
    GUI.description_canvas,
    bg="#2966D3",
    width=50,
    font=("None", int(16.0)),
    state='readonly',
    #insertbackground="black",
    textvariable=textInput)

TextLabel = GUI.description_canvas.create_text(
    5, 5,
    text="CANVAS",
    fill="#000000",
    font=("None", int(16.0)),
    anchor=NW)

displayText.pack()
displayText.place(x=460, y=300)

keyboard_ABC_frame.tkraise()

#####################################################

#q = Button(keyboard_on_screen,text = 'Q', command = lambda : press('Q'))
#q.grid(row = 1 , column = 0, ipadx = 14 , ipady = 14)
#q.pack()
#q.place(x=50, y=50, width = 50, height = 50)




#keyboard_on_screen2.pack()
#keyboard_on_screen2.place(x=0, y=600)



exp = " "          # global variable
# showing all data in display

def press(num):
    global exp
    exp=exp + str(num)
    textInput.set(exp)
# end


# function clear button

def clear():
    global exp
    exp = ""
    textInput.set(exp)

# end

def switchToABC_keyboard():
    keyboard_ABC_frame.tkraise()

def switchTo123_keyboard():
    keyboard_123_frame.tkraise()

def backspace():
    global textInput
    global exp
    exp = exp[:-1]
    textInput.set(exp)


Q = Button(keyboard_ABC_canvas,text = 'Q', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('Q'))
Q.place(x=10, y=10, width = 100, height = 100)

W = Button(keyboard_ABC_canvas,text = 'W', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('W'))
W.place(x=120, y=10, width = 100, height = 100)

E = Button(keyboard_ABC_canvas,text = 'E', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('E'))
E.place(x=230, y=10, width = 100, height = 100)

R = Button(keyboard_ABC_canvas,text = 'R', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('R'))
R.place(x=340, y=10, width = 100, height = 100)

T = Button(keyboard_ABC_canvas,text = 'T', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('T'))
T.place(x=450, y=10, width = 100, height = 100)

Y = Button(keyboard_ABC_canvas,text = 'Y', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('Y'))
Y.place(x=560, y=10, width = 100, height = 100)

U = Button(keyboard_ABC_canvas,text = 'U', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('U'))
U.place(x=670, y=10, width = 100, height = 100)

I = Button(keyboard_ABC_canvas,text = 'I', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('I'))
I.place(x=780, y=10, width = 100, height = 100)

O = Button(keyboard_ABC_canvas,text = 'O', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('O'))
O.place(x=890, y=10, width = 100, height = 100)

P = Button(keyboard_ABC_canvas,text = 'P', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('P'))
P.place(x=1000, y=10, width = 100, height = 100)

Å = Button(keyboard_ABC_canvas,text = 'Å', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('Å'))
Å.place(x=1110, y=10, width = 100, height = 100)

BackSpace = Button(keyboard_ABC_canvas,text = 'Backspace', font = ("Sofia Pro Medium",int(35.0)), command = backspace)
BackSpace.place(x=1220, y=10, width = 290, height = 100)

#cur = Button(keyboard_on_screen,text = '{' , width = 8, command = lambda : press('{'))
#cur.grid(row = 1 , column = 11 , ipadx = 6 , ipady = 10)

#cur_c = Button(keyboard_on_screen,text = '}' , width = 8, command = lambda : press('}'))
#cur_c.grid(row = 1 , column = 12, ipadx = 6 , ipady = 10)

#back_slash = Button(keyboard_on_screen,text = '\\' , width = 8, command = lambda : press('\\'))
#back_slash.grid(row = 1 , column = 13, ipadx = 6 , ipady = 10)

#clear = Button(keyboard_on_screen,text = 'Clear' , width = 8, command = clear)
#clear.grid(row = 1 , column = 14, ipadx = 20 , ipady = 10)

# Second Line Button

A = Button(keyboard_ABC_canvas,text = 'A', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('A'))
A.place(x=10, y=120, width = 100, height = 100)

S = Button(keyboard_ABC_canvas,text = 'S', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('S'))
S.place(x=120, y=120, width = 100, height = 100)

D = Button(keyboard_ABC_canvas,text = 'D', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('D'))
D.place(x=230, y=120, width = 100, height = 100)

F = Button(keyboard_ABC_canvas,text = 'F', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('F'))
F.place(x=340, y=120, width = 100, height = 100)

G = Button(keyboard_ABC_canvas,text = 'G', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('G'))
G.place(x=450, y=120, width = 100, height = 100)

H = Button(keyboard_ABC_canvas,text = 'H', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('H'))
H.place(x=560, y=120, width = 100, height = 100)

J = Button(keyboard_ABC_canvas,text = 'J', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('J'))
J.place(x=670, y=120, width = 100, height = 100)

K = Button(keyboard_ABC_canvas,text = 'K', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('K'))
K.place(x=780, y=120, width = 100, height = 100)

L = Button(keyboard_ABC_canvas,text = 'L', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('L'))
L.place(x=890, y=120, width = 100, height = 100)

Æ = Button(keyboard_ABC_canvas,text = 'Æ', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('Æ'))
Æ.place(x=1000, y=120, width = 100, height = 100)

Ø = Button(keyboard_ABC_canvas,text = 'Ø', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('Ø'))
Ø.place(x=1110, y=120, width = 100, height = 100)

Enter = Button(keyboard_ABC_canvas,text = 'Enter', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press(''))
Enter.place(x=1220, y=120, width = 290, height = 100)

# third line Button

Z = Button(keyboard_ABC_canvas,text = 'Z', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('Z'))
Z.place(x=10, y=230, width = 100, height = 100)

X = Button(keyboard_ABC_canvas,text = 'X', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('X'))
X.place(x=120, y=230, width = 100, height = 100)

C = Button(keyboard_ABC_canvas,text = 'C', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('C'))
C.place(x=230, y=230, width = 100, height = 100)

V = Button(keyboard_ABC_canvas,text = 'V', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('V'))
V.place(x=340, y=230, width = 100, height = 100)

B = Button(keyboard_ABC_canvas,text = 'B', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('B'))
B.place(x=450, y=230, width = 100, height = 100)

N = Button(keyboard_ABC_canvas,text = 'N', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('N'))
N.place(x=560, y=230, width = 100, height = 100)

M = Button(keyboard_ABC_canvas,text = 'M', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('M'))
M.place(x=670, y=230, width = 100, height = 100)

comma = Button(keyboard_ABC_canvas,text = ',', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press(','))
comma.place(x=780, y=230, width = 100, height = 100)

dot = Button(keyboard_ABC_canvas,text = '.', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('.'))
dot.place(x=890, y=230, width = 100, height = 100)

dash = Button(keyboard_ABC_canvas,text = '-', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('-'))
dash.place(x=1000, y=230, width = 100, height = 100)

shift = Button(keyboard_ABC_canvas,text = 'shift', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('shift'))
shift.place(x=1110, y=230, width = 100, height = 100)

Exit = Button(keyboard_ABC_canvas,text = 'Exit', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('Exit'))
Exit.place(x=1220, y=230, width = 290, height = 100)

#Fourth Line Button

option = Button(keyboard_ABC_canvas,text = '123', font = ("Sofia Pro Medium",int(35.0)), command = switchTo123_keyboard)
option.place(x=10, y=340, width = 100, height = 100)

space = Button(keyboard_ABC_canvas,text = 'Space', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press(' '))
space.place(x=420, y=340, width = 500, height = 100)

######### Extra menu

number_0 = Button(keyboard_123_canvas,text = '0', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('0'))
number_0.place(x=10, y=10, width = 100, height = 100)

number_1 = Button(keyboard_123_canvas,text = '1', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('1'))
number_1.place(x=120, y=10, width = 100, height = 100)

number_2 = Button(keyboard_123_canvas,text = '2', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('2'))
number_2.place(x=230, y=10, width = 100, height = 100)

number_3 = Button(keyboard_123_canvas,text = '3', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('3'))
number_3.place(x=340, y=10, width = 100, height = 100)

number_4 = Button(keyboard_123_canvas,text = '4', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('4'))
number_4.place(x=450, y=10, width = 100, height = 100)

number_5 = Button(keyboard_123_canvas,text = '5', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('5'))
number_5.place(x=560, y=10, width = 100, height = 100)

number_6 = Button(keyboard_123_canvas,text = '6', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('6'))
number_6.place(x=670, y=10, width = 100, height = 100)

number_7 = Button(keyboard_123_canvas,text = '7', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('7'))
number_7.place(x=780, y=10, width = 100, height = 100)

number_8 = Button(keyboard_123_canvas,text = '8', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('8'))
number_8.place(x=890, y=10, width = 100, height = 100)

number_9 = Button(keyboard_123_canvas,text = '9', font = ("Sofia Pro Medium",int(35.0)), command = lambda : press('9'))
number_9.place(x=1000, y=10, width = 100, height = 100)

option = Button(keyboard_123_canvas,text = 'ABC', font = ("Sofia Pro Medium",int(35.0)), command = switchToABC_keyboard)
option.place(x=10, y=340, width = 100, height = 100)




