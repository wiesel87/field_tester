from tkinter import *

window = Tk()

window.geometry("1920x1080")
window.title("Sani field tester alpha v0.1")
menuColor = "#FFFFFF"
window.configure(bg=menuColor)
window.bind('<Escape>', lambda event: window.destroy())

####################### Graphics ##############################
logo_IMG = PhotoImage(file='img/sani_logo.png')
home_IMG = PhotoImage(file='img/Button_Home.png')
home_IMG_a = PhotoImage(file='img/Button_Home_active.png')
scan_IMG = PhotoImage(file='img/Button_Scan.png')
scan_IMG_a = PhotoImage(file='img/Button_Scan_active.png')
results_IMG = PhotoImage(file='img/Button_Results.png')
results_IMG_a = PhotoImage(file='img/Button_Results_active.png')
settings_IMG = PhotoImage(file='img/Button_Settings.png')
settings_IMG_a = PhotoImage(file='img/Button_Settings_active.png')
power_IMG = PhotoImage(file='img/Button_Power.png')
power_IMG_a = PhotoImage(file='img/Button_Power_active.png')

background_IMG = PhotoImage(file="img/Background.png")
background_scan_IMG = PhotoImage(file="img/Background_Scan.png")

################ Design ######################

## LEFT MENU ##
menu_frame = Frame(
    window,
    bg=menuColor,
    height=1080,
    width=400,
    bd=0,
    highlightthickness=0,
    relief="ridge")

menu_frame.place(x=0, y=0)

menu_canvas = Canvas(
    menu_frame,
    bg=menuColor,
    height=1080,
    width=400,
    bd=0,
    highlightthickness=0,
    relief="ridge")

menu_canvas.pack()
menu_canvas.place(x=0, y=0)

######################################################################
####################### Graphics Screen ##############################
#######################                 ##############################
####################### HOME SCREEN: 1 ##########################
home_Frame_1 = Frame(
    window,
    bg="#e2e0e0",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge")

home_Frame_1.pack()

home_Canvas_1 = Canvas(
    home_Frame_1,
    bg="#444444",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge")
# home_Canvas_1.place(x=50, y=50)
home_Canvas_1.pack()
home_Frame_1.place(x=342, y=0)

TextLabel = home_Canvas_1.create_text(
    5, 5,
    text="HOME",
    fill="#000000",
    font=("None", int(16.0)),
    anchor=NW)

########################## SCAN SCREEN: 1 ###########################

    
scan_Frame_1 = Frame(
    window,
    bg="#FF0000",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge")

scan_Frame_1.pack()
scan_Frame_1.place(x=342, y=0)

scan_Canvas_1 = Canvas(
    scan_Frame_1,
    # bg="#e2e0e0",
    height=1080,
    width=1920,
    #bd=3,
    #highlightthickness=3,
    #relief="ridge"
    )
# scan_Canvas_1.place(x=100, y=200)
scan_Canvas_1.pack()  ##important

background_LBL = Label(scan_Canvas_1, image=background_scan_IMG).place(x=12, y=12)

#background_focus_LBL = Label(scan_Canvas_1,bg="#EAF2FF",image=background_focus_IMG).place(x=26-8, y=26-8)

#### Frame with scrollbar ###
frame = Frame(scan_Canvas_1, width=810, height=500, bg="red", colormap="new")
# frame.pack()
frame.place(x=405-342, y=120, width=810, height=900)

scrollbar = Scrollbar(frame, width=40, bd=0,highlightthickness=0,troughcolor="#FFFFFF")
scrollbar.pack(side=RIGHT, fill=Y)

# imgx = PhotoImage(file = f"img/skl.png")
# style.configure("Vertical.TScrollbar",bordercolor="red", arrowcolor="white")
# print("OKKKAAYYY")

mylist = Listbox(frame, yscrollcommand=scrollbar.set, width=300, font=("SofiaProMedium", int(22.0)),bd=0,highlightthickness=0, relief=FLAT)
for line in range(100):
    mylist.insert(END, "#" + str(line)+ " Sani Sensor 2>> "+ "RSSI: 10 " + "SNR: 10 " )
    mylist.see(END)

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview, width=50)

##-----------------

####################### Settings SCREEN: 1 ##########################
settings_Frame_1 = Frame(
    window,
    bg="#e2e0e0",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge")

settings_Frame_1.pack()

settings_Canvas_1 = Canvas(
    settings_Frame_1,
    bg="#aa00FF",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge")
# home_Canvas_1.place(x=50, y=50)
settings_Canvas_1.pack()
##DRAW th first canvas
settings_Frame_1.place(x=342, y=0)

TextLabel = settings_Canvas_1.create_text(
    0, 0,
    text="Settings",
    fill="#000000",
    font=("None", int(16.0)),
    anchor=NW)


####################### LEFT MENU  ##########################

############# LEFT MENU BTN Functions ######################

def home_FUN():
    change_img_of_BTN("home")
    home_Frame_1.tkraise()
    print("HOME PRESSED")

def scan_FUN():
    # home_Canvas_1.itemconfigure(TextLabel, text="Scan")
    change_img_of_BTN("scan")
    scan_Frame_1.tkraise()
    print("SCAN PRESSED")

def results_FUN():
    home_Canvas_1.itemconfigure(TextLabel, text="Results")
    change_img_of_BTN("results")

def settings_FUN():
    settings_Frame_1.tkraise()
    change_img_of_BTN("settings")

def power_FUN():
    settings_Frame_1.tkraise()  # show page
    change_img_of_BTN("power")
    window.destroy()

############################### LEFT MENU Buttons #############################
# def btn_clicked():
#    print("sda")


Label(menu_canvas,
      image=logo_IMG, bg=menuColor).place(x=20, y=26)

home_BTN = Button(menu_canvas,
                  image=home_IMG_a,
                  bg=menuColor,
                  activebackground=menuColor,
                  borderwidth=0,
                  highlightthickness=0,
                  command=home_FUN,
                  relief="flat")

home_BTN.place(x=26, y=188, width=289, height=73)

scan_BTN = Button(menu_canvas,
                  image=scan_IMG,
                  bg=menuColor,
                  activebackground=menuColor,
                  borderwidth=0,
                  highlightthickness=0,
                  command=scan_FUN,
                  relief="flat")

scan_BTN.place(x=26, y=293, width=289, height=73)

results_BTN = Button(menu_canvas,
                     image=results_IMG,
                     bg=menuColor,
                     activebackground=menuColor,
                     borderwidth=0,
                     highlightthickness=0,
                     command=results_FUN,
                     relief="flat")

results_BTN.place(x=26, y=398, width=289, height=73)

settings_BTN = Button(menu_canvas,
                      image=settings_IMG,
                      bg=menuColor,
                      activebackground=menuColor,
                      borderwidth=0,
                      highlightthickness=0,
                      command=settings_FUN,
                      relief="flat")

settings_BTN.place(x=26, y=503, width=289, height=73)

power_BTN = Button(menu_canvas,
                   image=power_IMG,
                   borderwidth=0,
                   bg=menuColor,
                   activebackground=menuColor,
                   highlightthickness=0,
                   command=power_FUN,
                   relief="flat")

power_BTN.place(x=26, y=968, width=289, height=73)

################ DESCRIPTION ENTRY FRAME ######################

description_frame = Frame(
    window,
    bg="#E2E0E0",
    height=1080,
    width=1551,
    bd=0,
    highlightthickness=0,
    relief="ridge")

description_frame.place(x=342, y=0)

description_canvas = Canvas(
    description_frame,
    bg="#E2E0E0",
    height=1080,
    width=1551,
    bd=0,
    highlightthickness=0,
    relief="ridge")

description_canvas.pack()
description_canvas.place(x=0, y=0)

################ Graphic functions ######################

def change_img_of_BTN(x):
    global home_IMG
    global home_IMG_a
    global scan_IMG
    global scan_IMG_a
    global results_IMG
    global results_IMG_a
    global settings_IMG
    global settings_IMG_a
    global power_IMG
    global power_IMG_a

    if x == "home":
        home_BTN.configure(image=home_IMG_a)
        scan_BTN.configure(image=scan_IMG)
        results_BTN.configure(image=results_IMG)
        settings_BTN.configure(image=settings_IMG)
        power_BTN.configure(image=power_IMG)
    elif x == "scan":
        home_BTN.configure(image=home_IMG)
        scan_BTN.configure(image=scan_IMG_a)
        results_BTN.configure(image=results_IMG)
        settings_BTN.configure(image=settings_IMG)
        power_BTN.configure(image=power_IMG)
    elif x == "results":
        home_BTN.configure(image=home_IMG)
        scan_BTN.configure(image=scan_IMG)
        results_BTN.configure(image=results_IMG_a)
        settings_BTN.configure(image=settings_IMG)
        power_BTN.configure(image=power_IMG)
    elif x == "settings":
        home_BTN.configure(image=home_IMG)
        scan_BTN.configure(image=scan_IMG)
        results_BTN.configure(image=results_IMG)
        settings_BTN.configure(image=settings_IMG_a)
        power_BTN.configure(image=power_IMG)
    elif x == "power":
        home_BTN.configure(image=home_IMG)
        scan_BTN.configure(image=scan_IMG)
        results_BTN.configure(image=results_IMG)
        settings_BTN.configure(image=settings_IMG)
        power_BTN.configure(image=power_IMG_a)


# window.resizable(False, False)
#window.wm_attributes('-fullscreen', 'True')
# window.config(cursor="none")


