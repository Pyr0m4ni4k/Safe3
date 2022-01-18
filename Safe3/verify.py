import tkinter

window = tkinter.Tk()                                                             # show error message
window.title("ERROR: incorrect password")                                         #
window.geometry("300x100")                                                        #
window.resizable(width=0, height=0)

label = tkinter.Label(master=window, text="ERROR: incorrect password", fg="red")  #
label.pack()                                                                      #
label.place(x=70, y=30)                                                           #

filedetent = open("rxwts98.txt", "w").write("0")
filetemp = open("tmp.txt", "w").write("")                                         #

window.mainloop()                                                                 #
