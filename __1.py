import sqlite3                  #Database
import PIL.Image as img         #PIL
import PIL.ImageTk as imgtk     #PIL
import datetime                 #Date&Time
import json                     #JSON
import sys                      #System
from tkinter import *           #GUI
from tkinter import ttk         #TkinterToolkit
from tkinter import messagebox  #MessageBox


#RootWindow
root = Tk()

#Globals

SignIn_entry_password = ''
SignUp_entry_phone = 0
SignUp_entry_name = ''
SignUp_entry_email = ''
SignUp_entry_password = ''
SignUp_entry_repassword = ''
customerID = 0
customerName = ''
Order_Total = 0


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

#List Globals
Size_List = []
Quantity_List = []

#Dictionary Globals
Dict_1 = {}
Dict_2 = {}
Dict_Name = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9,
             10:10, 11:11, 12:12, 13:13, 14:14, 15:15, 16:16}
Dict_smallPrice = {1:110, 2:125, 3:100, 4:135, 5:150, 6:170, 7:165, 8:190,
                   9:25, 10:75, 11:95, 12:135, 13:40, 14:55, 15:75, 16:110}

Dict_mediumPrice = {1:210, 2:235, 3:215, 4:270, 5:300, 6:345, 7:320, 8:365,
                   9:40, 10:95, 11:110, 12:155, 13:50, 14:70, 15:125, 16:205}

Dict_largePrice = {1:305, 2:315, 3:280, 4:385, 5:450, 6:480, 7:535, 8:595,
                   9:65, 10:105, 11:140, 12:170, 13:65, 14:135, 15:195, 16:285}

#Database Connetion
conn = sqlite3.connect('pizza.db')
c = conn.cursor()



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
def Input_SignUp():

    global SignUp_entry_phone, SignUp_entry_name, SignUp_entry_email, SignUp_entry_password, SignUp_entry_repassword

    e1 = SignUp_entry_phone.get()
    e2 = SignUp_entry_name.get()
    e3 = SignUp_entry_email.get()
    e4 = SignUp_entry_password.get()
    e5 = SignUp_entry_repassword.get()

    print(e1, e2, e3, e4, e5)
    if e1 == '' or e2 == '' or e3 == '' or e4 == '' or e5 == '':
        Display_MessageBox("SignUp_missing")

    else:
        flag_id, name = Phone_Email_check(e1, e3)

        if flag_id == 0:
            Display_MessageBox("Phone_exists", name[0])

        elif flag_id == 1:
            Display_MessageBox("Email_exists", name[0])


        name = Custdata_entry(e1, e2, e3, e4)
        Step_SignIn_Cust()


#Input for SignIn
def Input_SignIn():

    global SignIn_entry_phone, SignIn_entry_password, customerID

    e1 = SignIn_entry_phone.get()
    e2 = SignIn_entry_password.get()

    flag_id = ID_check(e1)

    if flag_id == 0:

        Display_MessageBox("ID_missing")

    else:

        if flag_id == 1:

            ans = Display_MessageBox("ID_wrong")
            if ans == 'yes':
                Step_SignUp_Cust()

        else:
            flag_password = Password_Check(e1, e2)

            if flag_password == 0:
                Display_MessageBox("Password_missing")

            elif flag_password == 1:
                Display_MessageBox("Password_wrong")

            else:
                name = Custdata_retrival(e1)
                Step_Welcome_Cust(name)


#DropDown-Input
def DropDown_Input(item_no):

    global Dict_1, Dict_2, Size_List, Quantity_List

    if item_no != 0:

        a = Size_List[item_no].get()
        b = Quantity_List[item_no].get()

        Dict_1[item_no] = a
        Dict_2[item_no] = b

        print(Dict_1)
        print(Dict_2)

    #The Done Button
    else:
        Calc_Price(Dict_1, Dict_2)


#Price Calculation
def Calc_Price(Dict_1, Dict_2):

    global Dict_smallPrice, Dict_mediumPrice, Dict_largePrice

    order_list = []
    amount_list = []

    for i in range(1, 17):
        if i in Dict_1:
            order_list.append([i, Dict_1[i], int(Dict_2[i])])
            print(Dict_1[i], Dict_2[i])
    print(order_list)

    for i in order_list:
        if i[1] == 'Small':
            a = Dict_smallPrice[i[0]] * i[2]
            amount_list.append(int(a))

        elif i[1] == 'Medium':
            a = Dict_mediumPrice[i[0]] * i[2]
            amount_list.append(int(a))

        else:
            a = Dict_mediumPrice[i[0]] * i[2]
            amount_list.append(int(a))

    print(amount_list)
    Step_Bill_Cust(order_list, amount_list)

#Displaying different MessageBoxes
def Display_MessageBox(info, name = ''):

    if info == 'Password_missing':
        messagebox.showinfo("Password Missing", "Please enter a Password")

    elif info == 'Password_wrong':
        messagebox.showinfo("Incorrect Password", "Sorry, the entered password is Wrong")

    elif info == 'ID_missing':
        messagebox.showinfo("Phone No Missing", "Please enter your Phone No")

    elif info == 'ID_wrong':
        ans = messagebox.askquestion("Are you a new user", "The entered phone no does not match any of our users,\n Would you like to SignUp?")
        return ans

    elif info == 'SignUp_missing':
        messagebox.showinfo("Fields Empty", "Please fill all the details")

    elif info == 'Phone_exists':
        messagebox.askquestion("Phone No Exists", "This Phone No belongs to: " + name + "\nPlease SignIn or use a different Phone No\n Would you like to SignIn?")

    elif info == 'Email_exists':
        messagebox.askquestion("Email Exists", "This Email belongs to: " + name + "\nPlease SignIn or use a different Email\n Would you like to SignIn?")

#The Home Frame
def Step_Home():

    global root, frame_1
    root.geometry("1500x750+10+10")

    label_1 = Label(frame_1, text = "Are you a Customer or an Employee?", fg = "Black")
    button_1 = Button(frame_1, text = "Customer", bg = "gainsboro", fg = "Black", command = Step_Choice_Cust )
    button_2 = Button(frame_1, text = "Employee", bg = "gainsboro", fg = "Black", command = a )

    frame_1.pack()
    label_1.pack(fill = X)
    button_1.pack()
    button_2.pack()
    root.mainloop()


#User Choice, New or Existing
def Step_Choice_Cust():
    global root, frame_1, frame_2

    frame_1.destroy()

    label_1 = Label(frame_2, text = "Are you an Existing Customer or a New One?")
    button_1 = Button(frame_2, text = "Existing User", bg = "gainsboro", fg = "Black", command = Step_SignIn_Cust )
    button_2 = Button(frame_2, text = "New User", bg = "gainsboro", fg = "Black", command = Step_SignUp_Cust )

    frame_2.pack()
    label_1.pack(fill = X)
    button_1.pack()
    button_2.pack()


#User SignIn
def Step_SignIn_Cust():
    global root, frame_2, frame_3, SignIn_entry_phone, SignIn_entry_password

    frame_2.destroy()
    frame_4.pack_forget()

    label_1 = Label(frame_3, text = "Phone No : ")
    label_2 = Label(frame_3, text = "Password : ")
    label_header = Label(frame_3, text = "Please enter your Login Details")
    SignIn_entry_phone = Entry(frame_3)
    SignIn_entry_password = Entry(frame_3)
    button_1 = Button(frame_3, text = "Submit", command = Input_SignIn)

    frame_3.pack()
    label_header.grid(row = 0, columnspan = 2)
    label_1.grid(row = 1, sticky = E)
    label_2.grid(row = 2, sticky = E)
    SignIn_entry_phone.grid(row = 1, column = 1)
    SignIn_entry_password.grid(row = 2, column = 1)
    button_1.grid(columnspan = 2)


#User SignUp
def Step_SignUp_Cust():

    global root, frame_2, frame_3, frame_4, SignUp_entry_phone, SignUp_entry_name, SignUp_entry_email, SignUp_entry_password, SignUp_entry_repassword

    frame_2.destroy()
    frame_3.pack_forget()

    label_1 = Label(frame_4, text = "Enter your Phone No : ")
    label_2 = Label(frame_4, text = "Enter your Name : ")
    label_3 = Label(frame_4, text = "Enter your Email : ")
    label_4 = Label(frame_4, text = "Set a Password : ")
    label_5 = Label(frame_4, text = "Retype Password")
    label_header = Label(frame_4, text = "Enter your Details : ")

    SignUp_entry_phone = Entry(frame_4)
    SignUp_entry_name = Entry(frame_4)
    SignUp_entry_email = Entry(frame_4)
    SignUp_entry_password = Entry(frame_4)
    SignUp_entry_repassword = Entry(frame_4)

    button_1 = Button(frame_4, text = "Submit", command = Input_SignUp)

    frame_4.pack()
    label_header.grid(row = 0, columnspan = 2, sticky = W+E)
    label_1.grid(row = 1, sticky = E)
    label_2.grid(row = 2, sticky = E)
    label_3.grid(row = 3, sticky = E)
    label_4.grid(row = 4, sticky = E)
    label_5.grid(row = 5, sticky = E)

    SignUp_entry_phone.grid(row = 1, column = 1)
    SignUp_entry_name.grid(row = 2, column = 1)
    SignUp_entry_email.grid(row = 3, column = 1)
    SignUp_entry_password.grid(row = 4, column = 1)
    SignUp_entry_repassword.grid(row = 5, column = 1)

    button_1.grid(columnspan = 2)


#User Welcome
def Step_Welcome_Cust(name):

    global root, frame_3, frame_4, frame_5

    frame_3.destroy()
    frame_4.destroy()

    var_1 = StringVar()
    var_1.set("Welcome " + str(name[0]))

    label_1 = Label (frame_5, textvariable = var_1,)
    button_1 = Button(frame_5, text = "New Order", bg = "gainsboro", fg = "Black", command = Step_Menu_Cust)
    button_2 = Button(frame_5, text = "Order History", bg = "gainsboro", fg = "Black", command = Step_OrderHistory_Cust)

    frame_5.pack()
    label_1.pack(fill = X)
    button_1.pack()
    button_2.pack()


#Predefined Menu
def Step_Menu_Cust():

    global root, frame_5, frame_6, frame_7, frame_8, frame_9, Size, Quantity, Size_List, Quantity_List, Dict_Name

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
    label_heading1 = Label(frame_6, text = "Veg Pizzas")
    label_1 = Label(frame_6, image = b_1)
    label_1.image = b_1
    label_name1 = Label(frame_6, text = str(Dict_Name[1]))
    label_2 = Label(frame_6, image = b_2)
    label_2.image = b_2
    label_name2 = Label(frame_6, text = str(Dict_Name[2]))
    label_3 = Label(frame_6, image = b_3)
    label_3.image = b_3
    label_name3 = Label(frame_6, text = str(Dict_Name[3]))
    label_4 = Label(frame_6, image = b_4)
    label_4.image = b_4
    label_name4 = Label(frame_6, text = str(Dict_Name[4]))

    #NonVeg_Pizzas-Image_Ready
    label_heading2 = Label(frame_7, text = "Non - Veg Pizzas")
    label_5 = Label(frame_7, image = b_5)
    label_5.image = b_5
    label_name5 = Label(frame_7, text = str(Dict_Name[5]))
    label_6 = Label(frame_7, image = b_6)
    label_6.image = b_6
    label_name6 = Label(frame_7, text = str(Dict_Name[6]))
    label_7 = Label(frame_7, image = b_7)
    label_7.image = b_7
    label_name7 = Label(frame_7, text = str(Dict_Name[7]))
    label_8 = Label(frame_7, image = b_8)
    label_8.image = b_8
    label_name8 = Label(frame_7, text = str(Dict_Name[8]))

    #Sides-Image_Ready
    label_heading3 = Label(frame_8, text = "Sides")
    label_9 = Label(frame_8, image = b_9)
    label_9.image = b_9
    label_name9 = Label(frame_8, text = str(Dict_Name[9]))
    label_10 = Label(frame_8, image = b_10)
    label_10.image = b_10
    label_name10 = Label(frame_8, text = str(Dict_Name[10]))
    label_11 = Label(frame_8, image = b_11)
    label_11.image = b_11
    label_name11 = Label(frame_8, text = str(Dict_Name[11]))
    label_12 = Label(frame_8, image = b_12)
    label_12.image = b_12
    label_name12 = Label(frame_8, text = str(Dict_Name[12]))

    #Beverages-Image_Ready
    label_heading4 = Label(frame_9, text = "Beverages")
    label_13 = Label(frame_9, image = b_13)
    label_13.image = b_13
    label_name13 = Label(frame_9, text = str(Dict_Name[13]))
    label_14 = Label(frame_9, image = b_14)
    label_14.image = b_14
    label_name14 = Label(frame_9, text = str(Dict_Name[14]))
    label_15 = Label(frame_9, image = b_15)
    label_15.image = b_15
    label_name15 = Label(frame_9, text = str(Dict_Name[15]))
    label_16 = Label(frame_9, image = b_16)
    label_16.image = b_16
    label_name16 = Label(frame_9, text = str(Dict_Name[16]))

    #Spacing
    label_100 = Label(frame_6, text = " ")
    label_200 = Label(frame_7, text = " ")
    label_300 = Label(frame_8, text = " ")
    label_400 = Label(frame_9, text = " ")


    #Generating Multiple StringVars
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
    button_17 = Button(frame_9, text="Done!!", command= lambda: DropDown_Input(0))


    #Veg_Pizzas-Pack
    frame_6.pack()
    label_heading1.grid(row = 0, columnspan = 7, sticky = N)
    label_1.grid(row = 1, rowspan = 3, column = 0, padx = 20, pady = 20)
    label_name1.grid(row = 3, column = 0, sticky = S)
    option_1a.grid(row = 1, column = 1, sticky = S)
    option_1b.grid(row = 2, column = 1, sticky = N)
    button_1.grid(row = 3, column = 1, sticky = S)
    label_2.grid(row = 1, rowspan = 3, column = 2, padx = 20, pady = 20)
    label_name2.grid(row = 3, column = 2, sticky = S)
    option_2a.grid(row = 1, column = 3, sticky = S)
    option_2b.grid(row = 2, column = 3, sticky = N)
    button_2.grid(row = 3, column = 3)
    label_3.grid(row = 1, rowspan = 3, column = 4, padx = 20, pady = 20)
    label_name3.grid(row = 3, column = 4, sticky = S)
    option_3a.grid(row = 1, column = 5, sticky = S)
    option_3b.grid(row = 2, column = 5, sticky = N)
    button_3.grid(row = 3, column = 5)
    label_4.grid(row = 1, rowspan = 3, column = 6, padx = 20, pady = 20)
    label_name4.grid(row = 3, column = 6, sticky = S)
    option_4a.grid(row = 1, column = 7, sticky = S)
    option_4b.grid(row = 2, column = 7, sticky = N)
    button_4.grid(row = 3, column = 7)
    label_100.grid(row = 4, columnspan = 7)
    ttk.Separator(frame_6).place(x = 0, y = 170, relwidth=2)

    #NonVeg_Pizzas-Pack
    frame_7.pack()
    label_heading2.grid(row = 0, columnspan = 7, sticky = N)
    label_5.grid(row = 1, rowspan = 3, column = 0, padx = 20, pady = 20)
    label_name5.grid(row = 3, column = 0, sticky = S)
    option_5a.grid(row = 1, column = 1, sticky = S)
    option_5b.grid(row = 2, column = 1, sticky = N)
    button_5.grid(row = 3, column = 1)
    label_6.grid(row = 1, rowspan = 3, column = 2, padx = 20, pady = 20)
    label_name6.grid(row = 3, column = 2, sticky = S)
    option_6a.grid(row = 1, column = 3, sticky = S)
    option_6b.grid(row = 2, column = 3, sticky = N)
    button_6.grid(row = 3, column = 3)
    label_7.grid(row = 1, rowspan = 3, column = 4, padx = 20, pady = 20)
    label_name7.grid(row = 3, column = 4, sticky = S)
    option_7a.grid(row = 1, column = 5, sticky = S)
    option_7b.grid(row = 2, column = 5, sticky = N)
    button_7.grid(row = 3, column = 5)
    label_8.grid(row = 1, rowspan = 3, column = 6, padx = 20, pady = 20)
    label_name8.grid(row = 3, column = 6, sticky = S)
    option_8a.grid(row = 1, column = 7, sticky = S)
    option_8b.grid(row = 2, column = 7, sticky = N)
    button_8.grid(row = 3, column = 7)
    label_200.grid(row = 4, columnspan = 7)
    ttk.Separator(frame_7).place(x = 0, y = 360, relwidth=2)

    #Sides-Pack
    frame_8.pack()
    label_heading3.grid(row = 0, columnspan = 7, sticky = N)
    label_9.grid(row = 1, rowspan = 3, column = 0, padx = 20, pady = 20)
    label_name9.grid(row = 3, column = 0, sticky = S)
    option_9a.grid(row = 1, column = 1, sticky = S)
    option_9b.grid(row = 2, column = 1, sticky = N)
    button_9.grid(row = 3, column = 1)
    label_10.grid(row = 1, rowspan = 3, column = 2, padx = 20, pady = 20)
    label_name10.grid(row = 3, column = 2, sticky = S)
    option_10a.grid(row = 1, column = 3, sticky = S)
    option_10b.grid(row = 2, column = 3, sticky = N)
    button_10.grid(row = 3, column = 3)
    label_11.grid(row = 1, rowspan = 3, column = 4, padx = 20, pady = 20)
    label_name11.grid(row = 3, column = 4, sticky = S)
    option_11a.grid(row = 1, column = 5, sticky = S)
    option_11b.grid(row = 2, column = 5, sticky = N)
    button_11.grid(row = 3, column = 5)
    label_12.grid(row = 1, rowspan = 3, column = 6, padx = 20, pady = 20)
    label_name12.grid(row = 3, column = 6, sticky = S)
    option_12a.grid(row = 1, column = 7, sticky = S)
    option_12b.grid(row = 2, column = 7, sticky = N)
    button_12.grid(row = 3, column = 7)
    label_300.grid(row = 4, columnspan = 7)
    ttk.Separator(frame_8).place(x = 0, y = 540, relwidth=2)

    #Beverages-Pack
    frame_9.pack()
    label_heading4.grid(row = 0, columnspan = 7, sticky = N)
    label_13.grid(row = 1, rowspan = 3, column = 0, padx = 20, pady = 20)
    label_name13.grid(row = 3, column = 0, sticky = S)
    option_13a.grid(row = 1, column = 1, sticky = S)
    option_13b.grid(row = 2, column = 1, sticky = N)
    button_13.grid(row = 3, column = 1)
    label_14.grid(row = 1, rowspan = 3, column = 2, padx = 20, pady = 20)
    label_name14.grid(row = 3, column = 2, sticky = S)
    option_14a.grid(row = 1, column = 3, sticky = S)
    option_14b.grid(row = 2, column = 3, sticky = N)
    button_14.grid(row = 3, column = 3)
    label_15.grid(row = 1, rowspan = 3, column = 4, padx = 20, pady = 20)
    label_name15.grid(row = 3, column = 4, sticky = S)
    option_15a.grid(row = 1, column = 5, sticky = S)
    option_15b.grid(row = 2, column = 5, sticky = N)
    button_15.grid(row = 3, column = 5)
    label_16.grid(row = 1, rowspan = 3, column = 6, padx = 20, pady = 20)
    label_name16.grid(row = 3, column = 6, sticky = S)
    option_16a.grid(row = 1, column = 7, sticky = S)
    option_16b.grid(row = 2, column = 7, sticky = N)
    button_16.grid(row = 3, column = 7)
    button_17.grid(row = 4, column = 7)
    label_200.grid(row = 5, columnspan = 7)
    ttk.Separator(frame_9).place(x = 0, y = 730, relwidth=2)

#Order-History Display
def Step_OrderHistory_Cust():

    global root, frame_5, frame_10, customerID, Dict_Name, Dict_smallPrice, Dict_mediumPrice, Dict_largePrice

    #Lists
    Timestamp_List = []
    Item_List = []
    Total_List = []
    OrderItems_List = []
    OrderTimestamps_List = []
    OrderTotals_List = []

    #Label-Lists
    Label_Timestamps_List = []
    Label_Items_List = []
    Label_Totals_List = []

    Count_List = []

    #Variables for Grid Manipulation
    k = 0
    x = 2
    m = 2
    n = 2
    y = 0
    z = 0
    q = 0

    c.execute('''SELECT orderSummary, orderTotal, orderDateTime
                 FROM Orders
                 WHERE custID = ?''', (customerID,))
    a = c.fetchall()

    for i in a:
        OrderItems = eval(a[k][0])
        OrderItems_List.append(OrderItems)
        OrderTotals = a[k][1]
        OrderTotals_List.append(OrderTotals)
        OrderTimestamps = a[k][2]
        OrderTimestamps_List.append(OrderTimestamps)
        k += 1

    frame_5.destroy()

    label_header = Label(frame_10, text = "Here are your most recent orders : ")
    label_tableheader = Label(frame_10, text = "Date                                Order-Items                     Order-Total")

    #Generating Multiple StringVars
    for i in OrderItems_List:
        p = 0
        for j in i:
            if j[1] == 'Small':
                Item = StringVar()
                Item.set(str(Dict_Name[j[0]]) + " (" + j[1] + ") X " + str(j[2]) + " = " + str(Dict_smallPrice[j[0]] * j[2]))
            elif j[1] == 'Medium':
                Item = StringVar()
                Item.set(str(Dict_Name[j[0]]) + " (" + j[1] + ") X " + str(j[2]) + " = " + str(Dict_mediumPrice[j[0]] * j[2]))
            else:
                Item = StringVar()
                Item.set(str(Dict_Name[j[0]]) + " (" + j[1] + ") X " + str(j[2]) + " = " + str(Dict_largePrice[j[0]] * j[2]))
            Item_List.append(Item)
            p += 1
        Count_List.append(p)
    print(Count_List)
    for i in OrderTimestamps_List:
        Timestamp = IntVar()
        Timestamp.set(i)
        Timestamp_List.append(Timestamp)

    for i in OrderTotals_List:
        Total = IntVar()
        Total.set(i)
        Total_List.append(Total)
    print(OrderItems_List)

    #Labels
    for i in Item_List:
        label_Item = Label(frame_10, textvariable = i,)
        Label_Items_List.append(label_Item)

    for i in Timestamp_List:
        label_Timestamp = Label(frame_10, textvariable = i,)
        Label_Timestamps_List.append(label_Timestamp)

    for i in Total_List:
        label_Total = Label(frame_10, textvariable = i,)
        Label_Totals_List.append(label_Total)


    #Packing
    frame_10.pack()
    label_header.grid(row = 0, columnspan = 3)
    label_tableheader.grid(row = 1, columnspan = 3)


    for i in Label_Timestamps_List:
        i.grid(row = m, rowspan = Count_List[y], column = 0, sticky = W+N)
        m = m + Count_List[y]
        y += 1

    for i in Count_List:
        for j in range(0, i):
            Label_Items_List[q].grid(row = x, column = 1)
            q += 1
            x += 1

    for i in Label_Totals_List:
        i.grid(row = n, rowspan = Count_List[z], column = 2, sticky = E+N)
        n = n + Count_List[z]
        z +=1

#Bill Display
def Step_Bill_Cust(order_list, amount_list):

    global root, frame_6, frame_7, frame_8, frame_9, frame_11, Order_Total

    k = 0
    Bill_List = []
    Label_List = []

    frame_6.destroy()
    frame_7.destroy()
    frame_8.destroy()
    frame_9.destroy()

    for i in amount_list:
        Order_Total += i

    Total = StringVar()
    Total.set("Your total payable amount is: " + str(Order_Total))

    for i in order_list:
        Bill = StringVar()
        Bill.set("Item No " + str(i[0]) + " (" + i[1] + " ) X " + str(i[2]) + " = " + str(amount_list[k]))
        Bill_List.append(Bill)
        k += 1

    #Labels
    label_1 = Label(frame_11, text = "Total Bill")

    for i in Bill_List:
        label_Bill = Label(frame_11, textvariable = i,)
        Label_List.append(label_Bill)

    label_Total = Label(frame_11, textvariable = Total)

    #Packing
    frame_11.pack()
    label_1.pack()

    for i in Label_List:
        i.pack()

    label_Total.pack()

    Orderdata_entry(order_list, amount_list)


#Create-Table
def Create_Tables():

    c.execute('''CREATE TABLE IF NOT EXISTS Customers(custID INTEGER PRIMARY KEY,
                                                      custName TEXT,
                                                      custPassword	TEXT,
	                                                  custEmail	TEXT,
                                                      custPhone INTEGER)''')

    c.execute('''CREATE TABLE IF NOT EXISTS Orders(orderNo INTEGER PRIMARY KEY,
                                                   custID INTEGER,
                                                   orderSummary TEXT,
                                                   orderTotal REAL,
                                                   orderDateTime TEXT,
                                                   FOREIGN KEY(custID) REFERENCES Customers(custID))''')

def ID_check(phone):

    if phone == '':
        return 0

    else:

        c.execute('''SELECT custID
                     FROM Customers
                     WHERE custPhone = ?''', (phone,))
        a = c.fetchone()
        print(a)
        if a == None:
            return 1
        else:
            return 2

def Password_Check(phone, Password_entered):

    if Password_entered == '':
        return 0
    else:
        c.execute('''SELECT custPassword
                     FROM Customers
                     WHERE custPhone = ?''', (phone,))
        a = c.fetchone()
        print(a)
        Password_retrived = a[0]

        if Password_entered != Password_retrived:
            return 1
        else:
            return 2

def Phone_Email_check(phone, email):

    c.execute('''SELECT custName
                 FROM Customers
                 WHERE custPhone = ?''', (phone,))
    a = c.fetchone()

    c.execute('''SELECT custName
                 FROM Customers
                 WHERE custEmail = ?''', (email,))
    b = c.fetchone()

    if a != None:
        return 0, a

    elif b != None:
        return 1, b

    else:
        return 2

def Custdata_entry(phone, name, email, password):

    c.execute('''SELECT custID
                 FROM Customers
                 WHERE custID = (SELECT MAX(custID) FROM Customers)''')
    a = c.fetchone()
    customerID = int(a[0] + 1)

    c.execute('''INSERT INTO Customers(custID, custPhone, custName, custEmail, custPassword)
                 VALUES(?, ?, ?, ?, ?)''', (customerID, phone, name, email, password))

    conn.commit()


def Custdata_retrival(phone):

    global customerID

    c.execute('''SELECT custName
                 FROM Customers
                 WHERE custPhone = ?''', (phone,))
    name = c.fetchone()

    c.execute('''SELECT custID
                 FROM Customers
                 WHERE custPhone = ?''', (phone,))
    b = c.fetchone()
    customerID = b[0]

    return name


def Orderdata_entry(order_list, amount_list):

    global Order_Total, customerID

    c.execute('''SELECT orderNo
                 FROM Orders
                 WHERE orderNo = (SELECT MAX(orderNo) FROM Orders)''')
    a = c.fetchone()
    order_no = int(a[0] + 1)

    order_summ = json.dumps(order_list)
    t = datetime.datetime.now()
    timestamp = t.strftime('%d-%m-%Y %H:%M:%S')
    print(order_no, customerID, order_list, Order_Total, timestamp)
    c.execute('''INSERT INTO Orders(orderNo, custID, orderSummary,
                                    orderTotal, orderDateTime)
                 VALUES(?,?,?,?,?)''', (order_no, customerID, order_summ, Order_Total, timestamp))

    conn.commit()


Step_Home()
