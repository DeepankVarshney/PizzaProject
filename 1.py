from tkinter import *

root = Tk()
frame_1 = Frame(root)

def Step_1():

    global root
    global frame_1
    root.geometry("1500x750+10+10")

    
    frame_1.pack()
    label_1 = Label(frame_1, text = "Are you a Customer or an Employee?", fg = "Black")
    label_1.pack(fill = X)
    button_1 = Button(frame_1, text = "Customer", bg = "gainsboro", fg = "Black", command = Step_2_Cust )
    button_1.pack()

    root.mainloop()

def Step_2_Cust():

    global root
    global frame_1
    frame_1.destroy()


    frame_2 = Frame(root)
    label_1 = Label(frame_2, text = "Customer ID")
    label_2 = Label(frame_2, text = "Password")
    global entry_1
    entry_1 = Entry(frame_2)
    global entry_2
    entry_2 = Entry(frame_2)

    frame_2.pack()
    label_1.grid(row = 0, sticky = E)
    label_2.grid(row = 1, sticky = W)
    entry_1.grid(row = 0, column = 1)
    entry_2.grid(row = 1, column = 1)

    button_1 = Button(frame_2, text = "Submit", command = Input )
    button_1.grid(columnspan = 2)


Step_1()
