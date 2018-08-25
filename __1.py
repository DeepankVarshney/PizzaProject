import sqlite3                  #Database
import tkinter.ttk as ttk       #Seperator Line
import PIL.Image as img         #PIL
import PIL.ImageTk as imgtk     #PIL
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
frame_9 = Frame(root)
frame_10 = Frame(root)
frame_11 = Frame(root)
frame_12 = Frame(root)
frame_13= Frame(root)
frame_14 = Frame(root)
frame_15 = Frame(root)
frame_16 = Frame(root)
frame_17= Frame(root)



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

    global root, frame_5, frame_6, frame_7, frame_8, frame_9

    frame_5.destroy()

    #Veg_Pizzas-ImageImport
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

    #NonVeg_Pizzas-ImageImport
    a_5 = img.open("Icons/1.png")
    a_5 = a_5.resize((100, 100), img.ANTIALIAS)
    b_5 = imgtk.PhotoImage(a_5)
    a_6 = img.open("Icons/2.png")
    a_6 = a_6.resize((100, 100), img.ANTIALIAS)
    b_6 = imgtk.PhotoImage(a_6)
    a_7 = img.open("Icons/3.png")
    a_7 = a_7.resize((100, 100), img.ANTIALIAS)
    b_7 = imgtk.PhotoImage(a_7)
    a_8 = img.open("Icons/4.png")
    a_8 = a_8.resize((100, 100), img.ANTIALIAS)
    b_8 = imgtk.PhotoImage(a_8)

    #Sides-ImageImport
    a_9 = img.open("Icons/1.png")
    a_9 = a_9.resize((100, 100), img.ANTIALIAS)
    b_9 = imgtk.PhotoImage(a_9)
    a_10 = img.open("Icons/2.png")
    a_10 = a_10.resize((100, 100), img.ANTIALIAS)
    b_10 = imgtk.PhotoImage(a_10)
    a_11 = img.open("Icons/3.png")
    a_11 = a_11.resize((100, 100), img.ANTIALIAS)
    b_11 = imgtk.PhotoImage(a_11)
    a_12 = img.open("Icons/4.png")
    a_12 = a_12.resize((100, 100), img.ANTIALIAS)
    b_12 = imgtk.PhotoImage(a_12)

    #Beverages-ImageImport
    a_13 = img.open("Icons/1.png")
    a_13 = a_13.resize((100, 100), img.ANTIALIAS)
    b_13 = imgtk.PhotoImage(a_13)
    a_14 = img.open("Icons/2.png")
    a_14 = a_14.resize((100, 100), img.ANTIALIAS)
    b_14 = imgtk.PhotoImage(a_14)
    a_15 = img.open("Icons/3.png")
    a_15 = a_15.resize((100, 100), img.ANTIALIAS)
    b_15 = imgtk.PhotoImage(a_15)
    a_16 = img.open("Icons/4.png")
    a_16 = a_16.resize((100, 100), img.ANTIALIAS)
    b_16 = imgtk.PhotoImage(a_16)

    #Veg_Pizzas-Ready
    label_1 = Label(frame_6, text = "Veg Pizzas")
    label_2 = Label(frame_6, image = b_1)
    label_2.image = b_1
    label_3 = Label(frame_6, image = b_2)
    label_3.image = b_2
    label_4 = Label(frame_6, image = b_3)
    label_4.image = b_3
    label_5 = Label(frame_6, image = b_4)
    label_5.image = b_4

    #NonVeg_Pizzas-Ready
    label_6 = Label(frame_7, text = "Non - Veg Pizzas")
    label_7 = Label(frame_7, image = b_5)
    label_7.image = b_5
    label_8 = Label(frame_7, image = b_6)
    label_8.image = b_6
    label_9 = Label(frame_7, image = b_7)
    label_9.image = b_7
    label_10 = Label(frame_7, image = b_8)
    label_10.image = b_8

    #Sides-Ready
    label_11 = Label(frame_8, text = "Sides")
    label_12 = Label(frame_8, image = b_9)
    label_12.image = b_9
    label_13 = Label(frame_8, image = b_10)
    label_13.image = b_10
    label_14 = Label(frame_8, image = b_11)
    label_14.image = b_11
    label_15 = Label(frame_8, image = b_12)
    label_15.image = b_12

    #Beverages-Ready
    label_16 = Label(frame_9, text = "Beverages")
    label_17 = Label(frame_9, image = b_13)
    label_17.image = b_13
    label_18 = Label(frame_9, image = b_14)
    label_18.image = b_14
    label_19 = Label(frame_9, image = b_15)
    label_19.image = b_15
    label_20 = Label(frame_9, image = b_16)
    label_20.image = b_16

    #Spacing
    label_100 = Label(frame_6, text = " ")
    label_200 = Label(frame_7, text = " ")
    label_300 = Label(frame_8, text = " ")
    label_400 = Label(frame_9, text = " ")

    #Veg_Pizzas-Pack
    frame_6.pack()
    label_1.grid(row = 0, columnspan = 4, sticky = N)
    label_2.grid(row = 1, column = 0, padx = 20, pady = 20)
    label_3.grid(row = 1, column = 1, padx = 20, pady = 20)
    label_4.grid(row = 1, column = 2, padx = 20, pady = 20)
    label_5.grid(row = 1, column = 3, padx = 20, pady = 20)
    label_100.grid(row = 2, columnspan = 4)
    ttk.Separator(root).place(x = 0, y = 160, relwidth=2)

    #NonVeg_Pizzas-Pack
    frame_7.pack()
    label_6.grid(row = 0, columnspan = 4, sticky = N)
    label_7.grid(row = 1, column = 0, padx = 20, pady = 20)
    label_8.grid(row = 1, column = 1, padx = 20, pady = 20)
    label_9.grid(row = 1, column = 2, padx = 20, pady = 20)
    label_10.grid(row = 1, column = 3, padx = 20, pady = 20)
    label_200.grid(row = 2, columnspan = 4)
    ttk.Separator(root).place(x = 0, y = 350, relwidth=2)

    #Sides-Pack
    frame_8.pack()
    label_11.grid(row = 0, columnspan = 4, sticky = N)
    label_12.grid(row = 1, column = 0, padx = 20, pady = 20)
    label_13.grid(row = 1, column = 1, padx = 20, pady = 20)
    label_14.grid(row = 1, column = 2, padx = 20, pady = 20)
    label_15.grid(row = 1, column = 3, padx = 20, pady = 20)
    label_300.grid(row = 2, columnspan = 4)
    ttk.Separator(root).place(x = 0, y = 540, relwidth=2)

    #NonVeg_Pizzas-Pack
    frame_9.pack()
    label_16.grid(row = 0, columnspan = 4, sticky = N)
    label_17.grid(row = 1, column = 0, padx = 20, pady = 20)
    label_18.grid(row = 1, column = 1, padx = 20, pady = 20)
    label_19.grid(row = 1, column = 2, padx = 20, pady = 20)
    label_20.grid(row = 1, column = 3, padx = 20, pady = 20)
    label_200.grid(row = 2, columnspan = 4)
    ttk.Separator(root).place(x = 0, y = 730, relwidth=2)


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
