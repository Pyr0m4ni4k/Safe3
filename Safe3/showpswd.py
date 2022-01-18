import tkinter


def showpswd(namepswd, username, email, ident, password):
    # creation window
    window = tkinter.Tk()
    window.title(namepswd)
    window.geometry("350x130")
    window.resizable(width=0, height=0)

    # write data on the window
    usern = tkinter.Label(text=f"Username:  {username}", font=10)
    usern.place(y=5, x=5)
    eemail = tkinter.Label(text=f"Email:           {email}", font=10)
    eemail.place(y=35, x=5)
    iid = tkinter.Label(text=f"ID:                 {ident}", font=10)
    iid.place(y=65, x=5)
    passw = tkinter.Label(text=f"Password:   {password}", font=10)
    passw.place(y=95, x=5)

    window.mainloop()


# read file tmp.txt and store data in a list
file = open("tmp.txt", "r")
data = file.readlines()
file.close()
data2 = []
data3 = ["", "", "", "", ""]

for x in data:
    data2.append(list(x))

n = 0

for y in data2:

    if y == data2[0]:
        y.pop(0)
        y.pop(0)
    y.pop(len(y) - 1)

    for i in y:
        data3[n] += i
    n += 1

# call showpswd() function
showpswd(data3[0], data3[1], data3[2], data3[3], data3[4])
