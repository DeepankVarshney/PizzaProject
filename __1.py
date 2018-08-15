import sqlite3      #Database
from tkinter import *       #GUI

root = Tk()
frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(root)
frame_4 = Frame(root)
frame_5 = Frame(root)


conn = sqlite3.connect('pizza.db')
c = conn.cursor()


#
# cost = 0.00
#
# base = {'personal': 50, 'regular': 150, 'large': 275}
#
# toppings_per = {'pepperoni': 15, 'meatballs': 20, 'mushroom': 17, 'onions': 13, 'sausage': 21, 'bacon': 25, 'paneer': 23, 'corn': 14, 'jalapeno': 19, 'olive': 22}
# toppings_reg = {'pepperoni': 45, 'meatballs': 60, 'mushroom': 42, 'onions': 39, 'sausage': 63, 'bacon': 75, 'paneer': 69, 'corn': 42, 'jalapeno': 57, 'olive': 66}
# toppings_lar = {'pepperoni': 75, 'meatballs': 100, 'mushroom': 85, 'onions': 65, 'sausage': 105, 'bacon': 125, 'paneer': 115, 'corn': 70, 'jalapeno': 95, 'olive': 110}


def a():

    print("Work In Progress.")


def Input():

    global SignUp_entry_1
    global SignUp_entry_2

    e1 = SignUp_entry_1.get()
    e2 = SignUp_entry_2.get()

    data_entry(e1, e2)


#The Home Window
def Step_1_Cust():

    global root, frame_1
    root.geometry("1500x750+10+10")

    label_1 = Label(frame_1, text = "Are you a Customer or an Employee?", fg = "Black")
    button_1 = Button(frame_1, text = "Customer", bg = "gainsboro", fg = "Black", command = Step_2_Cust )
    button_2 = Button(frame_1, text = "Employee", bg = "gainsboro", fg = "Black", command = a )

    frame_1.pack()
    label_1.pack(fill = X)
    button_1.pack()
    button_2.pack()
    root.mainloop()


#User Choice, New or Existing
def Step_2_Cust():
    global root, frame_1, frame_2

    frame_1.destroy()

    label_1 = Label(frame_2, text = "Are you an Existing Customer or a New One?")
    button_1 = Button(frame_2, text = "Existing User", bg = "gainsboro", fg = "Black", command = Step_3_Cust )
    button_2 = Button(frame_2, text = "New User", bg = "gainsboro", fg = "Black", command = Step_4_Cust )

    frame_2.pack()
    label_1.pack(fill = X)
    button_1.pack()
    button_2.pack()


#User SignIn
def Step_3_Cust():
    global root, frame_2, frame_3, SignIn_entry_1

    frame_2.destroy()

    label_1 = Label(frame_3, text = "Enter your ID")
    SignIn_entry_1 = Entry(frame_3)
    button_1 = Button(frame_3, text = "Submit", command = Input)

    frame_3.pack()
    label_1.grid(row = 0, sticky = E)
    SignIn_entry_1.grid(row = 0, column = 1)
    button_1.grid(columnspan = 2)


#User SignUp
def Step_4_Cust():

    global root, frame_2, frame_4, SignUp_entry_1, SignUp_entry_2

    frame_2.destroy()

    label_1 = Label(frame_4, text = "ID")
    label_2 = Label(frame_4, text = "Name")
    SignUp_entry_1 = Entry(frame_4)
    SignUp_entry_2 = Entry(frame_4)
    button_1 = Button(frame_4, text = "Submit", command = Input)

    frame_4.pack()
    label_1.grid(row = 0, sticky = E)
    label_2.grid(row = 1, sticky = W)
    SignUp_entry_1.grid(row = 0, column = 1)
    SignUp_entry_2.grid(row = 1, column = 1)
    button_1.grid(columnspan = 2)




def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS customer_all(customer_id INTEGER, customer_name TEXT, customer_order TEXT, price REAL, total_price REAL, order_datetime TEXT)")

def data_entry(id_, name_ ):

    id = id_
    name = name_

    c.execute("INSERT INTO customer_all(customer_id, customer_name) VALUES(?, ?)", (id, name))
    conn.commit()

def Cust_Input():

    create_table()
    data_entry(id_, pass_)

Step_1_Cust()
