import os
import tkinter
from PIL import ImageTk, Image


# creation window
window = tkinter.Tk()
window.geometry("800x600")
window.title("Safe 3.0")
window.resizable(width=0, height=0)

# load background
img = ImageTk.PhotoImage(Image.open("backgrounds/index1.jpg"))
bg = tkinter.Label(window, image=img)
bg.place(x=0, y=0)

# label that show author
author = tkinter.Label(text=" Samuele Valiante ", fg="white", bg="black", font=16)
author.place(x=0, y=573)

# label that show version
version = " v 1.0 "
vers = tkinter.Label(text=version, fg="white", bg="black", font=16)
vers.place(x=754, y=573)


def gui():
    # null label
    null = tkinter.Label(text=" ", fg="white", bg="#27282c")
    null.grid(column=0, row=0, pady=50)

    # creation label
    text_selection = tkinter.Label(text="  Choose one of the two options  ", font=16, fg="white", bg="black")
    text_selection.grid(column=5, row=3, pady=15, padx=280)

    # creation button to add password
    add_button = tkinter.Button(text=" Add password ", font=14, fg="white", bg="#27282c", command=lambda: (clean_window(), add_password()))
    add_button.grid(column=5, row=4, pady=15)

    # creation button to show passwords
    show_button = tkinter.Button(text="Show password", fg="white", bg="#27282c", font=14, command=lambda: (clean_window(), show_password()))
    show_button.grid(column=5, row=5, pady=15)


def clean_window():
    lista = window.grid_slaves()
    for x in lista:
        x.destroy()


# function that save data
def add_password():
    # clean window
    text_selection.destroy()
    add_button.destroy()
    show_button.destroy()
    null.destroy()

    # creating text boxes to save new password
    label_name_password = tkinter.Label(text="Insert name app/account:", fg="white", bg="#27282c")
    label_name_password.grid(column=5, row=4, pady=15)
    label_name_password.place(x=140, y=200)
    name1 = tkinter.StringVar()
    name_password = tkinter.Entry(textvariable=name1)
    name_password.grid(column=6, row=4, pady=15)
    name_password.place(x=320, y=200)
    alert_label = tkinter.Label(text="DON'T USE A NAME ALREADY USED!", fg="red", bg="#27282c")
    alert_label.grid(column=7, row=4)
    alert_label.place(x=490, y=200)

    # username
    label_username = tkinter.Label(text="Insert username:", fg="white", bg="#27282c")
    label_username.grid(column=5, row=5, pady=15)
    label_username.place(x=140, y=230)
    username1 = tkinter.StringVar()
    username = tkinter.Entry(textvariable=username1)
    username.grid(column=6, row=5, pady=15)
    username.place(x=320, y=230)

    # email
    label_email = tkinter.Label(text="Insert email address:", fg="white", bg="#27282c")
    label_email.grid(column=5, row=6, pady=15)
    label_email.place(x=140, y=260)
    email1 = tkinter.StringVar()
    email = tkinter.Entry(textvariable=email1)
    email.grid(column=6, row=6, pady=15)
    email.place(x=320, y=260)

    # ID
    label_ident = tkinter.Label(text="Insert ID:", fg="white", bg="#27282c")
    label_ident.grid(column=5, row=7, pady=15)
    label_ident.place(x=140, y=290)
    ident1 = tkinter.StringVar()
    ident = tkinter.Entry(textvariable=ident1)
    ident.grid(column=6, row=7, pady=15)
    ident.place(x=320, y=290)

    # password
    label_password = tkinter.Label(text="Insert password:", fg="white", bg="#27282c")
    label_password.grid(column=5, row=8, pady=15)
    label_password.place(x=140, y=320)
    password1 = tkinter.StringVar()
    password = tkinter.Entry(textvariable=password1)
    password.grid(column=6, row=8, pady=15)
    password.place(x=320, y=320)

    # save button
    save_button = tkinter.Button(text="Save", font=16, fg="white", bg="#27282c",
                                 command=lambda: save_data(name1, username1, email1, ident1, password1))
    save_button.grid(column=6, row=9)
    save_button.place(x=350, y=380)

    # function that save data in a temp file and restart function
    def save_data(sname, suser, semail, sident, spassword):
        file = open("tmp.txt", "w")
        filenpswd = open("namepswd.txt", "a")
        filenpswd.write(f"{sname.get()}\n")
        file.write(f"{sname.get()}\n{suser.get()}\n{semail.get()}\n{sident.get()}\n{spassword.get()}\n")
        file.close()
        filenpswd.close()
        os.system("cc -o database database.c")
        os.system("./database")
        label_password.destroy()
        label_name_password.destroy()
        label_email.destroy()
        label_ident.destroy()
        label_username.destroy()
        name_password.destroy()
        username.destroy()
        email.destroy()
        ident.destroy()
        password.destroy()
        save_button.destroy()
        alert_label.destroy()
        return_button.destroy()
        add_password()

    # button that return at the menu
    return_button = tkinter.Button(text="Back", font=24, fg="white", bg="#27282c", command=lambda: (gui(),
                                                                                                    label_password.destroy(),
                                                                                                    label_name_password.destroy(),
                                                                                                    label_email.destroy(),
                                                                                                    label_ident.destroy(),
                                                                                                    label_username.destroy(),
                                                                                                    name_password.destroy(),
                                                                                                    username.destroy(),
                                                                                                    email.destroy(),
                                                                                                    ident.destroy(),
                                                                                                    password.destroy(),
                                                                                                    save_button.destroy(),
                                                                                                    alert_label.destroy(),
                                                                                                    return_button.destroy()))

    return_button.grid(column=0, row=0, sticky=tkinter.N, pady=10, padx=10)


# function that show all password
def show_password():
    # clean window
    text_selection.destroy()
    add_button.destroy()
    show_button.destroy()

    # button that return at the menu
    return_button2 = tkinter.Button(text="Back", font=24, fg="white", bg="#27282c", command=lambda: (list_grid(), gui()))
    return_button2.grid(column=0, row=0, pady=10, padx=10, sticky=tkinter.NW)

    # select password
    select = tkinter.Label(text=" Choose a password that you want see ", fg="white", bg="black")
    select.grid(column=40, row=1, pady=10)
    select.place(x=330, y=570)
    select_variable = tkinter.StringVar()
    select_entry = tkinter.Entry(text=select_variable)
    select_entry.grid(column=40, row=3, ipady=5)
    select_entry.place(x=347, y=40)

    # null label to place various element
    null2 = tkinter.Label(text=" ", fg="white", bg="#27282c")
    null2.grid(column=0, row=3)
    null3 = tkinter.Label(text=" ", fg="white", bg="#27282c")
    null3.grid(column=1, row=4)
    null4 = tkinter.Label(text="  ", fg="white", bg="#27282c")
    null4.grid(column=2, row=5)

    # read every lines of namepswd.txt file and store them in list
    filepswd = open("namepswd.txt", "r")
    list_names = filepswd.readlines()
    new_list_names = []

    # removing /n from the list of the name passwords
    for i in list_names:
        y = ""
        i2 = list(i)
        i2.pop(len(i2) - 1)
        for x in i2:
            y += x
        new_list_names.append(y)

    def buttons_psw(name_passwd, r, c):
        button = tkinter.Label(text=name_passwd, fg="white", bg="#27282c")
        button.grid(column=c, row=r, ipadx=5, padx=5)

    column = 0
    row = 5
    for i in list_names:
        buttons_psw(i, row, column)
        row += 1
        if row == 17:
            row = 5
            column += 1
        if column > 11:
            full = tkinter.Tk()
            full.geometry("200x200")
            full.title("Error")
            full2 = tkinter.Label(master=full, text="Application is full!", fg="red")
            full2.grid(column=6, row=3)

    # button to search password
    def button_search():
        tmpfile = open("tmp.txt", "w")
        tmpfile.write(f"{new_list_names.index(select_variable.get())}")
        tmpfile.close()
        os.system("cc -o encoding eddof.c")
        os.system("./encoding")
        os.system("python3 showpswd.py")

    select_button = tkinter.Button(text="Search", fg="white", bg="#27282c", command=lambda: button_search())
    select_button.grid(column=6, row=3, pady=10)
    select_button.place(x=385, y=70)

    def list_grid():
        lista = window.grid_slaves()
        select_button.destroy()
        select.destroy()
        select_entry.destroy()
        for xy in lista:
            xy.destroy()


# control access
filecontr = open("rxwts98.txt", "r")
dt = filecontr.read()
if int(dt) == 1:
    print("ok")
else:
    print("compila ed esegui safe3.c")
    exit()

gui()

null = tkinter.Label(text=" ")
text_selection = tkinter.Label(text="  Choose one of the two options  ", font=16, fg="white", bg="black")
add_button = tkinter.Button(text=" Add password ", font=14, command=lambda: (add_password(),
                                                                             text_selection.destroy(),
                                                                             add_button.destroy(),
                                                                             show_button.destroy()))
show_button = tkinter.Button(text="Show password", font=14, command=lambda: (show_password(),
                                                                             text_selection.destroy(),
                                                                             add_button.destroy(),
                                                                             show_button.destroy()))

window.mainloop()
