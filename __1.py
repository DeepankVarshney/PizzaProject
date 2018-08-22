import sqlite3                  #Database
import tkinter.ttk as ttk       #Seperator Line
import PIL.Image as img  #PIL
import PIL.ImageTk as imgtk  #PIL
from tkinter import *           #GUI

root = Tk()
frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(root)
frame_4 = Frame(root)
frame_5 = Frame(root)
frame_6 = Frame(root)
frame_7 = Frame(root)
frame_8 = Frame(root)


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


def Input_1():

    global SignUp_entry_1
    global SignUp_entry_2

    e1 = SignUp_entry_1.get()
    e2 = SignUp_entry_2.get()

    data_entry(e1, e2)

def Input_2():

    global SignIn_entry_1

    e1 = SignIn_entry_1.get()

    name_retrival(e1)



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
    print(SignIn_entry_1)
    button_1 = Button(frame_3, text = "Submit", command = Input_2)

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
    button_1 = Button(frame_4, text = "Submit", command = Input_1)

    frame_4.pack()
    label_1.grid(row = 0, sticky = E)
    label_2.grid(row = 1, sticky = W)
    SignUp_entry_1.grid(row = 0, column = 1)
    SignUp_entry_2.grid(row = 1, column = 1)
    button_1.grid(columnspan = 2)


#User Welcome
def Step_5_Cust(name_):

    global root, frame_3, frame_4, frame_5

    frame_3.destroy()
    frame_4.destroy()

    var_1 = StringVar()
    var_1.set("Welcome " + str(name_[0]) )

    label_1 = Label (frame_5, textvariable = var_1,)
    button_1 = Button(frame_5, text = "New Order", bg = "gainsboro", fg = "Black", command = Step_6_Cust)
    button_2 = Button(frame_5, text = "Order History", bg = "gainsboro", fg = "Black", command = a)

    frame_5.pack()
    label_1.pack(fill = X)
    button_1.pack()
    button_2.pack()


#Predefined Menu
def Step_6_Cust():

    global root, frame_5

    frame_5.destroy()

    a_1 = img.open("Icons/1.png")
    a_1 = a_1.resize((100, 100), img.ANTIALIAS)
    b_1 = imgtk.PhotoImage(a_1)
    a_2 = img.open("Icons/2.png")
    a_2 = a_2.resize((100, 100), img.ANTIALIAS)
    b_2 = imgtk.PhotoImage(a_2)
    a_3 = img.open("Icons/3.png")
    a_3 = a_3.resize((100, 100), img.ANTIALIAS)
    b_3 = imgtk.PhotoImage(a_3)
    a_4 = img.open("Icons/4.png")
    a_4 = a_4.resize((100, 100), img.ANTIALIAS)
    b_4 = imgtk.PhotoImage(a_4)
    label_1 = Label(frame_6, text = "Veg Pizzas")
    label_2 = Label(frame_6, image = b_1)
    label_2.image = b_1
    label_3 = Label(frame_6, image = b_2)
    label_3.image = b_2
    label_4 = Label(frame_6, image = b_3)
    label_4.image = b_3
    label_5 = Label(frame_6, image = b_4)
    label_5.image = b_4


    frame_6.pack()
    label_1.grid(row = 0, sticky = N)
    label_2.grid(row = 3, column = 0)
    label_3.grid(row = 3, column = 1)
    label_4.grid(row = 3, column = 2)
    label_5.grid(row = 3, column = 3)

    ttk.Separator(root).place(x=0, y=200, relwidth=5)



def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS customer_all(customer_id INTEGER, customer_name TEXT, customer_order TEXT, price REAL, total_price REAL, order_datetime TEXT)")

def data_entry(id_, name_ ):

    id = id_
    name = name_

    c.execute("INSERT INTO customer_all(customer_id, customer_name) VALUES(?, ?)", (id, name))
    conn.commit()

    name_retrival(id)


def name_retrival(id_):

    name = ""
    id = id_

    print(name)
    c.execute("SELECT customer_name FROM customer_all WHERE customer_id = ?", (id,))
    name = c.fetchone()
    Step_5_Cust(name)



def Cust_Input():

    create_table()
    data_entry(id_, pass_)

Step_1_Cust()
