import tkinter
from PIL import ImageTk, Image

window_login = tkinter.Tk()         # window creation
window_login.title("Login")         #
window_login.geometry("200x200")    #
window_login.resizable(width=0, height=0)

# load background
img = ImageTk.PhotoImage(Image.open("backgrounds/index1.png"))
bg = tkinter.Label(window_login, image=img)
bg.place(x=0, y=0)

entry_password = tkinter.Entry()        # password label creation
entry_password.pack()                   #
entry_password.place(x=30, y=80)        #


def save_input(txt):                # function that save input and write it in a temp file
    temp = open("tmp.txt", "w")     #
    temp.write(txt)                 #
    temp.close()                    #


def save_password(txt):
    tmpfile = open("tmp.txt", "w")                      # saving input in tmp.txt and copy it contents in loginfile.txt
    loginfile = open("loginfile.txt", "w")              #
    tmpfile.write(txt)                                  #
    loginfile.write(f"9ednhf98d766s78w76s8{txt}")       #
    tmpfile.close()                                     #
    loginfile.close()                                   #


def login_user():                                                                                                       # function to login user
    text_login = tkinter.Label(master=window_login, text=" Insert password ", fg="white", bg="#27282c")       # text to label creation
    text_login.pack()                                                               #
    text_login.place(x=50, y=59)                                                    #

    button_login = tkinter.Button(master=window_login,                                    # button of login creation
                                  text="Login",
                                  fg="white", bg="#27282c",                                   #
                                  command=lambda: save_input(entry_password.get()) & exit())#
    button_login.pack()                                                                   #
    button_login.place(x=70, y=102)                                                       #


def new_user():                                                                                                         # function for a new user
    text_login = tkinter.Label(master=window_login, text="Insert the new password", fg="white", bg="#27282c")       # text to label creation
    text_login.pack()                                                                        #
    text_login.place(x=25, y=59)                                                             #

    button_login = tkinter.Button(master=window_login,                                  # button of login creation
                                  text="Save the new password",
                                  fg="white", bg="#27282c",                                    #
                                  command=lambda: save_password(entry_password.get()) & exit())  #
    button_login.pack()                                                                 #
    button_login.place(x=25, y=102)                                                     #


file = open("loginfile.txt", "r+")

if file.read():
    login_user()
else:
    new_user()

window_login.mainloop()
