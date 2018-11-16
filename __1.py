import sqlite3                  #Database
import tkinter.ttk as ttk       #Seperator Line
import PIL.Image as img         #PIL
import PIL.ImageTk as imgtk     #PIL
from tkinter import *           #GUI

#RootWindow
root = Tk()


#Frame Globals
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
frame_13 = Frame(root)
frame_14 = Frame(root)
frame_15 = Frame(root)
frame_16 = Frame(root)
frame_17 = Frame(root)


#Dictionary Globals
Dict_1 = {}
Dict_2 = {}


#Database Connetion
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





#Display Work In Progress
def a():

    print("Work In Progress.")


#Input for SignUp
def Input_1():

    global SignUp_entry_1
    global SignUp_entry_2

    e1 = SignUp_entry_1.get()
    e2 = SignUp_entry_2.get()

    data_entry(e1, e2)

#Input for SignIn
def Input_2():

    global SignIn_entry_1

    e1 = SignIn_entry_1.get()

    name_retrival(e1)


#DropDown-Input
def DropDown_Input(item):

    global Dict_1, Dict_2, Size_List, Quantity_List

    a = Size_List[item].get()
    b = Quantity_List[item].get()

    Dict_1[a] = item
    Dict_2[b] = item

    print(Dict_1)
    print(Dict_2)


#The Home Frame
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

    global root, frame_5, frame_6, frame_7, frame_8, frame_9, Size, Quantity, Size_List, Quantity_List

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

    #Veg_Pizzas-Image_Ready
    label_h1 = Label(frame_6, text = "Veg Pizzas")
    label_1 = Label(frame_6, image = b_1)
    label_1.image = b_1
    label_2 = Label(frame_6, image = b_2)
    label_2.image = b_2
    label_3 = Label(frame_6, image = b_3)
    label_3.image = b_3
    label_4 = Label(frame_6, image = b_4)
    label_4.image = b_4

    #NonVeg_Pizzas-Image_Ready
    label_h2 = Label(frame_7, text = "Non - Veg Pizzas")
    label_5 = Label(frame_7, image = b_5)
    label_5.image = b_5
    label_6 = Label(frame_7, image = b_6)
    label_6.image = b_6
    label_7 = Label(frame_7, image = b_7)
    label_7.image = b_7
    label_8 = Label(frame_7, image = b_8)
    label_8.image = b_8

    #Sides-Image_Ready
    label_h3 = Label(frame_8, text = "Sides")
    label_9 = Label(frame_8, image = b_9)
    label_9.image = b_9
    label_10 = Label(frame_8, image = b_10)
    label_10.image = b_10
    label_11 = Label(frame_8, image = b_11)
    label_11.image = b_11
    label_12 = Label(frame_8, image = b_12)
    label_12.image = b_12

    #Beverages-Image_Ready
    label_h4 = Label(frame_9, text = "Beverages")
    label_13 = Label(frame_9, image = b_13)
    label_13.image = b_13
    label_14 = Label(frame_9, image = b_14)
    label_14.image = b_14
    label_15 = Label(frame_9, image = b_15)
    label_15.image = b_15
    label_16 = Label(frame_9, image = b_16)
    label_16.image = b_16

    #Spacing
    label_100 = Label(frame_6, text = " ")
    label_200 = Label(frame_7, text = " ")
    label_300 = Label(frame_8, text = " ")
    label_400 = Label(frame_9, text = " ")


    #Generating Multiple StringVars
    Size_List = []
    Quantity_List = []

    for i in range(0, 17):

        Size = StringVar(root)
        Size_List.append(Size)

        Quantity = StringVar(root)
        Quantity_List.append(Quantity)


    #Option-Menus
    option_1a = OptionMenu(frame_6, Size_List[1], "Small", "Medium", "Large")
    option_1b = OptionMenu(frame_6, Quantity_List[1], "1", "2", "3")
    option_2a = OptionMenu(frame_6, Size_List[2], "Small", "Medium", "Large")
    option_2b = OptionMenu(frame_6, Quantity_List[2], "1", "2", "3")
    option_3a = OptionMenu(frame_6, Size_List[3], "Small", "Medium", "Large")
    option_3b = OptionMenu(frame_6, Quantity_List[3], "1", "2", "3")
    option_4a = OptionMenu(frame_6, Size_List[4], "Small", "Medium", "Large")
    option_4b = OptionMenu(frame_6, Quantity_List[4], "1", "2", "3")
    option_5a = OptionMenu(frame_7, Size_List[5], "Small", "Medium", "Large")
    option_5b = OptionMenu(frame_7, Quantity_List[5], "1", "2", "3")
    option_6a = OptionMenu(frame_7, Size_List[6], "Small", "Medium", "Large")
    option_6b = OptionMenu(frame_7, Quantity_List[6], "1", "2", "3")
    option_7a = OptionMenu(frame_7, Size_List[7], "Small", "Medium", "Large")
    option_7b = OptionMenu(frame_7, Quantity_List[7], "1", "2", "3")
    option_8a = OptionMenu(frame_7, Size_List[8], "Small", "Medium", "Large")
    option_8b = OptionMenu(frame_7, Quantity_List[8], "1", "2", "3")

    option_9a = OptionMenu(frame_8, Size_List[9], "Small", "Medium", "Large")
    option_9b = OptionMenu(frame_8, Quantity_List[9], "1", "2", "3")
    option_10a = OptionMenu(frame_8, Size_List[10], "Small", "Medium", "Large")
    option_10b = OptionMenu(frame_8, Quantity_List[10], "1", "2", "3")
    option_11a = OptionMenu(frame_8, Size_List[11], "Small", "Medium", "Large")
    option_11b = OptionMenu(frame_8, Quantity_List[11], "1", "2", "3")
    option_12a = OptionMenu(frame_8, Size_List[12], "Small", "Medium", "Large")
    option_12b = OptionMenu(frame_8, Quantity_List[12], "1", "2", "3")
    option_13a = OptionMenu(frame_9, Size_List[13], "Small", "Medium", "Large")
    option_13b = OptionMenu(frame_9, Quantity_List[13], "1", "2", "3")
    option_14a = OptionMenu(frame_9, Size_List[14], "Small", "Medium", "Large")
    option_14b = OptionMenu(frame_9, Quantity_List[14], "1", "2", "3")
    option_15a = OptionMenu(frame_9, Size_List[15], "Small", "Medium", "Large")
    option_15b = OptionMenu(frame_9, Quantity_List[15], "1", "2", "3")
    option_16a = OptionMenu(frame_9, Size_List[16], "Small", "Medium", "Large")
    option_16b = OptionMenu(frame_9, Quantity_List[16], "1", "2", "3")


    #OK Buttons
    button_1 = Button(frame_6, text="OK", command= lambda: DropDown_Input(1))
    button_2 = Button(frame_6, text="OK", command= lambda: DropDown_Input(2))
    button_3 = Button(frame_6, text="OK", command= lambda: DropDown_Input(3))
    button_4 = Button(frame_6, text="OK", command= lambda: DropDown_Input(4))
    button_5 = Button(frame_7, text="OK", command= lambda: DropDown_Input(5))
    button_6 = Button(frame_7, text="OK", command= lambda: DropDown_Input(6))
    button_7 = Button(frame_7, text="OK", command= lambda: DropDown_Input(7))
    button_8 = Button(frame_7, text="OK", command= lambda: DropDown_Input(8))
    button_9 = Button(frame_8, text="OK", command= lambda: DropDown_Input(9))
    button_10 = Button(frame_8, text="OK", command= lambda: DropDown_Input(10))
    button_11 = Button(frame_8, text="OK", command= lambda: DropDown_Input(11))
    button_12 = Button(frame_8, text="OK", command= lambda: DropDown_Input(12))
    button_13 = Button(frame_9, text="OK", command= lambda: DropDown_Input(13))
    button_14 = Button(frame_9, text="OK", command= lambda: DropDown_Input(14))
    button_15 = Button(frame_9, text="OK", command= lambda: DropDown_Input(15))
    button_16 = Button(frame_9, text="OK", command= lambda: DropDown_Input(16))


    #Veg_Pizzas-Pack
    frame_6.pack()
    label_h1.grid(row = 0, columnspan = 7, sticky = N)
    label_1.grid(row = 1, rowspan = 3, column = 0, padx = 20, pady = 20)
    option_1a.grid(row = 1, column = 1, sticky = S)
    option_1b.grid(row = 2, column = 1, sticky = N)
    button_1.grid(row = 3, column = 1)
    label_2.grid(row = 1, rowspan = 3, column = 2, padx = 20, pady = 20)
    option_2a.grid(row = 1, column = 3, sticky = S)
    option_2b.grid(row = 2, column = 3, sticky = N)
    button_2.grid(row = 3, column = 3)
    label_3.grid(row = 1, rowspan = 3, column = 4, padx = 20, pady = 20)
    option_3a.grid(row = 1, column = 5, sticky = S)
    option_3b.grid(row = 2, column = 5, sticky = N)
    button_3.grid(row = 3, column = 5)
    label_4.grid(row = 1, rowspan = 3, column = 6, padx = 20, pady = 20)
    option_4a.grid(row = 1, column = 7, sticky = S)
    option_4b.grid(row = 2, column = 7, sticky = N)
    button_4.grid(row = 3, column = 7)
    label_100.grid(row = 4, columnspan = 7)
    ttk.Separator(root).place(x = 0, y = 170, relwidth=2)

    #NonVeg_Pizzas-Pack
    frame_7.pack()
    label_h2.grid(row = 0, columnspan = 7, sticky = N)
    label_5.grid(row = 1, rowspan = 3, column = 0, padx = 20, pady = 20)
    option_5a.grid(row = 1, column = 1, sticky = S)
    option_5b.grid(row = 2, column = 1, sticky = N)
    button_5.grid(row = 3, column = 1)
    label_6.grid(row = 1, rowspan = 3, column = 2, padx = 20, pady = 20)
    option_6a.grid(row = 1, column = 3, sticky = S)
    option_6b.grid(row = 2, column = 3, sticky = N)
    button_6.grid(row = 3, column = 3)
    label_7.grid(row = 1, rowspan = 3, column = 4, padx = 20, pady = 20)
    option_7a.grid(row = 1, column = 5, sticky = S)
    option_7b.grid(row = 2, column = 5, sticky = N)
    button_7.grid(row = 3, column = 5)
    label_8.grid(row = 1, rowspan = 3, column = 6, padx = 20, pady = 20)
    option_8a.grid(row = 1, column = 7, sticky = S)
    option_8b.grid(row = 2, column = 7, sticky = N)
    button_8.grid(row = 3, column = 7)
    label_200.grid(row = 4, columnspan = 7)
    ttk.Separator(root).place(x = 0, y = 360, relwidth=2)

    #Sides-Pack
    frame_8.pack()
    label_h3.grid(row = 0, columnspan = 7, sticky = N)
    label_9.grid(row = 1, rowspan = 3, column = 0, padx = 20, pady = 20)
    option_9a.grid(row = 1, column = 1, sticky = S)
    option_9b.grid(row = 2, column = 1, sticky = N)
    button_9.grid(row = 3, column = 1)
    label_10.grid(row = 1, rowspan = 3, column = 2, padx = 20, pady = 20)
    option_10a.grid(row = 1, column = 3, sticky = S)
    option_10b.grid(row = 2, column = 3, sticky = N)
    button_10.grid(row = 3, column = 3)
    label_11.grid(row = 1, rowspan = 3, column = 4, padx = 20, pady = 20)
    option_11a.grid(row = 1, column = 5, sticky = S)
    option_11b.grid(row = 2, column = 5, sticky = N)
    button_11.grid(row = 3, column = 5)
    label_12.grid(row = 1, rowspan = 3, column = 6, padx = 20, pady = 20)
    option_12a.grid(row = 1, column = 7, sticky = S)
    option_12b.grid(row = 2, column = 7, sticky = N)
    button_12.grid(row = 3, column = 7)
    label_300.grid(row = 4, columnspan = 7)
    ttk.Separator(root).place(x = 0, y = 540, relwidth=2)

    #Beverages-Pack
    frame_9.pack()
    label_h4.grid(row = 0, columnspan = 7, sticky = N)
    label_13.grid(row = 1, rowspan = 3, column = 0, padx = 20, pady = 20)
    option_13a.grid(row = 1, column = 1, sticky = S)
    option_13b.grid(row = 2, column = 1, sticky = N)
    button_13.grid(row = 3, column = 1)
    label_14.grid(row = 1, rowspan = 3, column = 2, padx = 20, pady = 20)
    option_14a.grid(row = 1, column = 3, sticky = S)
    option_14b.grid(row = 2, column = 3, sticky = N)
    button_14.grid(row = 3, column = 3)
    label_15.grid(row = 1, rowspan = 3, column = 4, padx = 20, pady = 20)
    option_15a.grid(row = 1, column = 5, sticky = S)
    option_15b.grid(row = 2, column = 5, sticky = N)
    button_15.grid(row = 3, column = 5)
    label_16.grid(row = 1, rowspan = 3, column = 6, padx = 20, pady = 20)
    option_16a.grid(row = 1, column = 7, sticky = S)
    option_16b.grid(row = 2, column = 7, sticky = N)
    button_16.grid(row = 3, column = 7)
    label_200.grid(row = 4, columnspan = 7)
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

    c.execute("SELECT customer_name FROM customer_all WHERE customer_id = ?", (id,))
    name = c.fetchone()
    Step_5_Cust(name)



def Cust_Input():

    create_table()
    data_entry(id_, pass_)

Step_1_Cust()
