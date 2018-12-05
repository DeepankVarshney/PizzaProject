import sqlite3                  #Database
import PIL.Image as img         #PIL
import PIL.ImageTk as imgtk     #PIL
import datetime                 #Date&Time
import json                     #JSON
import sys                      #System
import re                       #Regex
import smtplib                  #SMTP
from tkinter import *           #GUI
from tkinter import ttk         #TkinterToolkit
from tkinter import messagebox  #MessageBox


#RootWindow
root = Tk()
image = img.open('Icons&Images/Background.jpg')
image = image.resize((1400, 750), img.ANTIALIAS)
bcg = imgtk.PhotoImage(image)
bcgl = Label(root, image=bcg)
bcgl.place(x=0, y=0)

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
Order_No = 0


#Frame Globals
frame_menu = Frame(root)
frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(root)
frame_4 = Frame(root)
frame_5 = Frame(root)
frame_6 = Frame(frame_menu)
frame_7 = Frame(frame_menu)
frame_8 = Frame(frame_menu)
frame_9 = Frame(frame_menu)
frame_10 = Frame(root)
frame_11 = Frame(root)
frame_12 = Frame(root)
frame_13 = Frame(frame_11)
frame_14 = Frame(frame_11)
frame_15 = Frame(frame_11)


#List Globals
Size_List = []
Quantity_List = []

#Dictionary Globals
Dict_1 = {}
Dict_2 = {}
Dict_Name = {1:"Double Cheese Margherita", 2:"Cheese & Corn", 3:"Peppy Panner", 4:"Veg Extravaganza", 5:"Chicken Sausage", 6:"Pepper Barbeque & Onion", 7:"Chicken Dominator", 8:"Non Veg Supreme", 9:"Garlic Bread",
             10:"Taco Mexicana", 11:"Pasta Italiano", 12:"Choco Lava Cake", 13:"Cocacola", 14:"Sprite", 15:"Mountain Dew", 16:"Pepsi"}
Dict_smallPrice = {1:100, 2:110, 3:125, 4:135, 5:150, 6:170, 7:175, 8:190,
                   9:85, 10:75, 11:130, 12:60, 13:40, 14:45, 15:45, 16:40}

Dict_mediumPrice = {1:215, 2:210, 3:235, 4:270, 5:300, 6:345, 7:350, 8:365,
                   9:110, 10:95, 11:170, 12:80, 13:60, 14:70, 15:80, 16:60}

Dict_largePrice = {1:280, 2:305, 3:315, 4:385, 5:450, 6:480, 7:535, 8:595,
                   9:65, 10:105, 11:140, 12:170, 13:80, 14:95, 15:95, 16:80}

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


#Password Recovery
def Password_Recovery(info):

    email = info.get()
    flag = Email_Check(email)

    if flag == 0:
        Display_MessageBox("Email_missing")

    elif flag == 1:
        ans = Display_MessageBox("Email_notfound")

        if ans == 'yes':
            Step_SignUp_Cust()
        else:
            pass

    else:
        password = Password_retrival(email)

        gmail_user = 'pizzapalace1339@gmail.com'
        gmail_password = 'Pizza@Pizza'

        sent_from = gmail_user
        to = email
        subject = "Password Reset for Pizza Palace"
        body = "The password for your account is: " + str(password)

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, to, subject, body)

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

        except:

            Display_MessageBox("Internet_issue")


        Display_MessageBox("Email_sent")
        Step_SignIn_Cust()

#Input for SignUp
def Input_SignUp():

    global SignUp_entry_phone, SignUp_entry_name, SignUp_entry_email, SignUp_entry_password, SignUp_entry_repassword

    e1 = SignUp_entry_phone.get()
    e2 = SignUp_entry_name.get()
    e3 = SignUp_entry_email.get()
    e4 = SignUp_entry_password.get()
    e5 = SignUp_entry_repassword.get()
    digit = e1.isdigit()
    alpha = e2.isalpha()

    if e1 == '' or e2 == '' or e3 == '' or e4 == '' or e5 == '':
        Display_MessageBox("Info_missing")

    elif digit != True or len(e1) != 10:
        Display_MessageBox("Phone_error")

    elif alpha != True:
        Display_MessageBox("Name_invalid")

    elif e4 != e5:
        Display_MessageBox("Password_mismatch")

    else:
        flag_id, name = Phone_Email_check(e1, e3)

        if flag_id == 0:
            ans = Display_MessageBox("Phone_exists", name[0])
            if ans == 'yes':
                Display_MessageBox("Redirecting")
                Step_SignIn_Cust()

            else:
                pass

        elif flag_id == 1:

            ans = Display_MessageBox("Email_exists", name[0])
            if ans == 'yes':
                Display_MessageBox("Redirecting")
                Step_SignIn_Cust()

            else:
                pass

        else:
            name = Custdata_entry(e1, e2, e3, e4)
            Step_SignIn_Cust()


#Input for SignIn
def Input_SignIn():

    global SignIn_entry_phone, SignIn_entry_password, customerID

    e1 = SignIn_entry_phone.get()
    e2 = SignIn_entry_password.get()

    flag_id = Phone_check(e1)
    digit = e1.isdigit()

    if flag_id == 0:

        Display_MessageBox("Phone_missing")

    elif digit != True or len(e1) != 10:
        Display_MessageBox("Phone_error")

    else:

        if flag_id == 1:

            ans = Display_MessageBox("Phone_wrong")
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

def Input_PlacedOrder(Name, PhoneNo, Email, HouseNo, Locality, City):

    global root

    e1 = Name.get()
    e2 = PhoneNo.get()
    e3 = Email.get()
    e4 = HouseNo.get()
    e5 = Locality.get()
    e6 = City.get()
    alpha = e1.isalpha()
    digit = e2.isdigit()

    if e1 == '' or e2 == '' or e3 == '' or e4 == '' or e5 == '' or e6 == '':
        Display_MessageBox("Info_missing")

    elif alpha != True:
        Display_MessageBox("Name_invalid")

    elif digit != True or len(e2) != 10:
        Display_MessageBox("Phone_error")

    else:
        messagebox.showinfo("Order Placed", "Dear " + e1 + " your order has been placed to\n\t" + e4 + ", " + e5 + ",\n\t" + e6 + "\nYou can expect delivery within the hour")
        Addrdata_entry(e1, e2, e3, e4, e5, e6)
        root.destroy()


#DropDown-Input
def DropDown_Input(item_no):

    global Dict_1, Dict_2, Size_List, Quantity_List

    if item_no != 0:

        a = Size_List[item_no].get()
        b = Quantity_List[item_no].get()

        if a == "Size":
            Display_MessageBox("Size_error")

        elif b == "Quantity":
            Display_MessageBox("Quantity_error")

        else:
            Dict_1[item_no] = a
            Dict_2[item_no] = b

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

    elif info == 'Phone_missing':
        messagebox.showinfo("Phone No Missing", "Please enter your Phone No")

    elif info == 'Phone_wrong':
        ans = messagebox.askquestion("Are you a new user", "The entered phone no does not match any of our users,\n Would you like to SignUp?")
        return ans

    elif info == 'Info_missing':
        messagebox.showinfo("Fields Empty", "Please fill all the details")

    elif info == 'Phone_error':
        messagebox.showinfo("Not a Number", "Phone No can only be a 10-digit number")

    elif info == 'Name_invalid':
        messagebox.showinfo("Invalid Name", "Name can only contain Alphabets")

    elif info == 'Password_mismatch':
        messagebox.showinfo("Password Mismatch", "Your entered Password do not match")

    elif info == 'Phone_exists':
        ans = messagebox.askquestion("Phone No Exists", "This Phone No belongs to: " + name + "\nPlease SignIn or use a different Phone No\n Would you like to SignIn?")
        return ans

    elif info == 'Email_exists':
        ans = messagebox.askquestion("Email Exists", "This Email belongs to: " + name + "\nPlease SignIn or use a different Email\n Would you like to SignIn?")
        return ans

    elif info == 'Redirecting':
        messagebox.showinfo("Redirecting", "Your are being redirected to SignIn \nPress OK to continue")

    elif info == 'Email_missing':
        messagebox.showinfo("Email empty", "Please enter an email")

    elif info == 'Email_notfound':
        ans = messagebox.askquestion("Email not registered", "The email you entered is not registered with us \nWould you like to SignUp")
        return ans

    elif info == 'Email_sent':
        messagebox.showinfo("Email sent", "Your Password has been sent to your registered Email address \n You are now being directed to SignIn")

    elif info == 'Internet_issue':
        messagebox.showinfo("Internet Error", "Please check your internet connection")

    elif info == 'Size_error':
        messagebox.showinfo("Wrong size", "Please select a valid size")

    elif info == 'Quantity_error':
        messagebox.showinfo("Wrong Quantity", "Please select a valid quantity")

#The Home Frame
def Step_Home():

    global root, frame_1
    root.geometry("1400x750+75+20")
    root.config(bg = "#282827")

    label_1 = Label(frame_1, text = "Are you a Customer or an Employee?", font = ("Comic Sans", 19), bg ="#282827", fg = "ghostwhite", height = 3, width = 35)
    button_1 = Button(frame_1, text = "Customer", font = ("Comic Sans", 14), bg = "gray35", fg = "white", height = 3, width = 25, command = Step_Choice_Cust)
    button_2 = Button(frame_1, text = "Employee", font = ("Comic Sans", 14), bg = "gray25", fg = "white", height = 3, width = 25, command = a )

    frame_1.config(bg = "#282827")
    frame_1.place(x = 435, y = 190)
    label_1.grid(row = 1, column = 1)
    button_1.grid(row = 2, column = 1, sticky = W+E)
    button_2.grid(row = 3, column = 1, sticky = W+E)
    root.mainloop()


#User Choice, New or Existing
def Step_Choice_Cust():
    global root, frame_1, frame_2

    frame_1.destroy()

    label_1 = Label(frame_2, text = "SignIn / SignUp", font = ("Comic Sans", 19), bg ="#282827", fg = "ghostwhite", height = 3, width = 35)
    button_1 = Button(frame_2, text = "SignIn", font = ("Comic Sans", 14), bg = "gray35", fg = "white", height = 3, width = 25, command = Step_SignIn_Cust )
    button_2 = Button(frame_2, text = "SignUp", font = ("Comic Sans", 14), bg = "gray25", fg = "white", height = 3, width = 25, command = Step_SignUp_Cust )

    frame_2.config(bg = "#282827")
    frame_2.place(x = 435, y = 190)
    label_1.grid(row = 1, column = 1)
    button_1.grid(row = 2, column = 1, sticky = W+E)
    button_2.grid(row = 3, column = 1, sticky = W+E)


#User SignIn
def Step_SignIn_Cust():
    global root, frame_2, frame_3, SignIn_entry_phone, SignIn_entry_password

    frame_2.destroy()
    frame_4.pack_forget()
    frame_4.grid_forget()
    frame_4.place_forget()
    frame_12.pack_forget()
    frame_12.grid_forget()
    frame_12.place_forget()

    label_1 = Label(frame_3, text = "Phone No : ", font = ("Comic Sans", 14), bg = "gray35", fg = "white", height = 2, width = 15)
    label_2 = Label(frame_3, text = "Password : ", font = ("Comic Sans", 14), bg = "gray25", fg = "white", height = 2, width = 15)
    label_blank = Label(frame_3, text = "   ", font = ("Comic Sans", 14), bg = "#282827", fg = "white", height = 2, width = 15)
    label_header = Label(frame_3, text = "Please enter your Login Details", font = ("Comic Sans", 19), bg ="#282827", fg = "ghostwhite", height = 4, width = 35)
    SignIn_entry_phone = Entry(frame_3, font = ("Comic Sans", 25), bg = "white", fg = "gray11", width = 15)
    SignIn_entry_password = Entry(frame_3, show = "*", font = ("Comic Sans", 25), bg = "white", fg = "gray11", width = 15)
    button_1 = Button(frame_3, text = "Submit", font = ("Comic Sans", 12), bg = "gray30", fg = "white", height = 2, width = 15, command = Input_SignIn)
    button_2 = Button(frame_3, text = "Forgot Password?", font = ("Comic Sans", 12), bg = "gray30", fg = "white", height = 2, width = 15, command = Step_PasswordRecovery_Cust)

    frame_3.config(bg = "#282827")
    frame_3.place(x = 435, y = 150)
    label_header.grid(row = 1, column = 0, columnspan = 2)
    label_1.grid(row = 2, column = 0, sticky = E, padx = 10, pady = 10)
    label_2.grid(row = 3, column = 0, sticky = E, padx = 10)
    SignIn_entry_phone.grid(row = 2, column = 1, sticky = W, padx = 10)
    SignIn_entry_password.grid(row = 3, column = 1, sticky = W, padx = 10)
    label_blank.grid(row = 4, column = 0)
    button_1.grid(row = 5, column = 0, pady = 10, sticky = E)
    button_2.grid(row = 5, column = 1, pady = 10)


#User Email for Password Recovery
def Step_PasswordRecovery_Cust():

    global root, frame_3, frame_12

    frame_3.pack_forget()
    frame_3.grid_forget()
    frame_3.place_forget()

    label_1 = Label(frame_12, text = "Please enter your email", font = ("Comic Sans", 19), bg ="#282827", fg = "ghostwhite", height = 3, width = 35)
    label_2 = Label(frame_12, text = "Email", font = ("Comic Sans", 15), bg = "gray35", fg = "white", height = 2, width = 15)
    Email_entry = Entry(frame_12, font = ("Comic Sans", 25), bg = "white", fg = "gray11", width = 15)
    button_1 = Button(frame_12, text = "Submit", font = ("Comic Sans", 12), bg = "gray30", fg = "white", height = 2, width = 15, command = lambda : Password_Recovery(Email_entry))

    frame_12.config(bg = "#282827")
    frame_12.place(x = 435, y = 190)
    label_1.grid(row = 1, column = 0, columnspan = 2, padx = 10)
    label_2.grid(row = 2, column = 0, sticky = E, padx = 10)
    Email_entry.grid(row = 2, column = 1, sticky = W, padx = 10)
    button_1.grid(row = 3, column = 0, columnspan = 2, pady = 10)

#User SignUp
def Step_SignUp_Cust():

    global root, frame_2, frame_3, frame_4, SignUp_entry_phone, SignUp_entry_name, SignUp_entry_email, SignUp_entry_password, SignUp_entry_repassword

    frame_2.destroy()
    frame_3.pack_forget()
    frame_3.grid_forget()
    frame_3.place_forget()

    label_1 = Label(frame_4, text = "Enter your Phone No : ", font = ("Comic Sans", 14), bg = "gray25", fg = "white", height = 2, width = 17)
    label_2 = Label(frame_4, text = "Enter your Name : ", font = ("Comic Sans", 14), bg = "gray35", fg = "white", height = 2, width = 17)
    label_3 = Label(frame_4, text = "Enter your Email : ", font = ("Comic Sans", 14), bg = "gray25", fg = "white", height = 2, width = 17)
    label_4 = Label(frame_4, text = "Set a Password : ", font = ("Comic Sans", 14), bg = "gray35", fg = "white", height = 2, width = 17)
    label_5 = Label(frame_4, text = "Retype Password : ", font = ("Comic Sans", 14), bg = "gray25", fg = "white", height = 2, width = 17)
    label_header = Label(frame_4, text = "Enter your Details : ", font = ("Comic Sans", 19), bg ="#282827", fg = "ghostwhite", height = 4, width = 35)
    label_blank = Label(frame_4, text = "   ", font = ("Comic Sans", 14), bg = "#282827", fg = "white", height = 2, width = 15)

    SignUp_entry_phone = Entry(frame_4, font = ("Comic Sans", 25), bg = "white", fg = "gray11", width = 15)
    SignUp_entry_name = Entry(frame_4, font = ("Comic Sans", 25), bg = "white", fg = "gray11", width = 15)
    SignUp_entry_email = Entry(frame_4, font = ("Comic Sans", 25), bg = "white", fg = "gray11", width = 15)
    SignUp_entry_password = Entry(frame_4, font = ("Comic Sans", 25), bg = "white", fg = "gray11", width = 15)
    SignUp_entry_repassword = Entry(frame_4, font = ("Comic Sans", 25), bg = "white", fg = "gray11", width = 15)

    button_1 = Button(frame_4, text = "Submit", font = ("Comic Sans", 12), bg = "gray30", fg = "white", height = 2, width = 15, command = Input_SignUp)

    frame_4.config(bg = "#282827")
    frame_4.place(x = 435, y = 105)
    label_header.grid(row = 1, column = 0, columnspan = 2)
    label_1.grid(row = 2, column = 0, sticky = E, padx = 10, ipadx = 10)
    label_2.grid(row = 3, column = 0, sticky = E, padx = 10, ipadx = 10, pady = 10)
    label_3.grid(row = 4, column = 0, sticky = E, padx = 10, ipadx = 10)
    label_4.grid(row = 5, column = 0, sticky = E, padx = 10, ipadx = 10, pady = 10)
    label_5.grid(row = 6, column = 0, sticky = E, padx = 10, ipadx = 10)

    SignUp_entry_phone.grid(row = 2, column = 1, sticky = W, padx= 10)
    SignUp_entry_name.grid(row = 3, column = 1, sticky = W, padx= 10)
    SignUp_entry_email.grid(row = 4, column = 1, sticky = W, padx= 10)
    SignUp_entry_password.grid(row = 5, column = 1, sticky = W, padx= 10)
    SignUp_entry_repassword.grid(row = 6, column = 1, sticky = W, padx= 10)

    label_blank.grid(row = 7, column = 0)
    button_1.grid(row = 8, column = 0, columnspan = 2, pady = 10)


#User Welcome
def Step_Welcome_Cust(name):

    global root, frame_3, frame_4, frame_5

    frame_3.destroy()
    frame_4.destroy()

    var_1 = StringVar()
    var_1.set("Welcome " + str(name[0]))

    label_1 = Label (frame_5, textvariable = var_1, font = ("Comic Sans", 19), bg ="#282827", fg = "ghostwhite", height = 3, width = 35)
    button_1 = Button(frame_5, text = "New Order", font = ("Comic Sans", 14), bg = "gray35", fg = "white", height = 3, width = 25, command = Step_Menu_Cust)
    button_2 = Button(frame_5, text = "Order History", font = ("Comic Sans", 14), bg = "gray25", fg = "white", height = 3, width = 25, command = Step_OrderHistory_Cust)

    frame_5.config(bg = "#282827")
    frame_5.place(x = 435, y = 190)
    label_1.grid(row = 1, column = 1)
    button_1.grid(row = 2, column = 1, sticky = W+E)
    button_2.grid(row = 3, column = 1, sticky = W+E)


#Predefined Menu
def Step_Menu_Cust():

    global root, frame_5, frame_6, frame_7, frame_8, frame_9, frame_menu, Size, Quantity, Size_List, Quantity_List, Dict_Name, Dict_Name, Dict_smallPrice, Dict_mediumPrice, Dict_largePrice
    PizzasPrices_List = []
    SidesPrices_List = []
    BeveragesPrices_List = []

    frame_5.destroy()

    for i in range(1, 9):
        Price = StringVar()
        Price.set("S : \u20B9" + str(Dict_smallPrice[i]) + "\nM : \u20B9" + str(Dict_mediumPrice[i]) + "\nL : \u20B9" + str(Dict_largePrice[i]))
        PizzasPrices_List.append(Price)

    for i in range(9, 13):
        Price = StringVar()
        Price.set("S : \u20B9" + str(Dict_smallPrice[i]) + "\nM : \u20B9" + str(Dict_mediumPrice[i]))
        SidesPrices_List.append(Price)

    for i in range(13, 17):
        Price = StringVar()
        Price.set("S : \u20B9" + str(Dict_smallPrice[i]) + "\nM : \u20B9" + str(Dict_mediumPrice[i]) + "\nL : \u20B9" + str(Dict_largePrice[i]))
        BeveragesPrices_List.append(Price)

    #Generating Multiple StringVars
    for i in range(0, 17):

        Size = StringVar(root)
        Size.set("Size")
        Size_List.append(Size)

        Quantity = StringVar(root)
        Quantity.set("Quantity")
        Quantity_List.append(Quantity)

    def Pizzas_Pack():

        frame_7.pack_forget()
        frame_7.grid_forget()
        frame_7.place_forget()
        frame_8.pack_forget()
        frame_8.grid_forget()
        frame_8.place_forget()

        label_header = Label(frame_6, text = "PIZZAS", font = ("Comic Sans", 18), bg ="#282827", fg = "ghostwhite", height = 2, width = 30)
        label_blank1 = Label(frame_6, text = "   ")
        label_blank2 = Label(frame_6, text = "   ")

        #Pizzas-ImageImport
        a_1 = img.open("Icons&Images/1.jpg")
        a_1 = a_1.resize((200, 200), img.ANTIALIAS)
        b_1 = imgtk.PhotoImage(a_1)
        a_2 = img.open("Icons&Images/2.jpg")
        a_2 = a_2.resize((200, 200), img.ANTIALIAS)
        b_2 = imgtk.PhotoImage(a_2)
        a_3 = img.open("Icons&Images/3.jpg")
        a_3 = a_3.resize((200, 200), img.ANTIALIAS)
        b_3 = imgtk.PhotoImage(a_3)
        a_4 = img.open("Icons&Images/4.jpg")
        a_4 = a_4.resize((200, 200), img.ANTIALIAS)
        b_4 = imgtk.PhotoImage(a_4)
        a_5 = img.open("Icons&Images/5.jpg")
        a_5 = a_5.resize((200, 200), img.ANTIALIAS)
        b_5 = imgtk.PhotoImage(a_5)
        a_6 = img.open("Icons&Images/6.jpg")
        a_6 = a_6.resize((200, 200), img.ANTIALIAS)
        b_6 = imgtk.PhotoImage(a_6)
        a_7 = img.open("Icons&Images/7.jpg")
        a_7 = a_7.resize((200, 200), img.ANTIALIAS)
        b_7 = imgtk.PhotoImage(a_7)
        a_8 = img.open("Icons&Images/8.jpg")
        a_8 = a_8.resize((200, 200), img.ANTIALIAS)
        b_8 = imgtk.PhotoImage(a_8)

        #Veg_Pizzas-Image_Ready
        label_1 = Label(frame_6, image = b_1)
        label_1.image = b_1
        label_name1 = Label(frame_6, text = str(Dict_Name[1]), font = ("Comic Sans", 11))
        label_2 = Label(frame_6, image = b_2)
        label_2.image = b_2
        label_name2 = Label(frame_6, text = str(Dict_Name[2]), font = ("Comic Sans", 11))
        label_3 = Label(frame_6, image = b_3)
        label_3.image = b_3
        label_name3 = Label(frame_6, text = str(Dict_Name[3]), font = ("Comic Sans", 11))
        label_4 = Label(frame_6, image = b_4)
        label_4.image = b_4
        label_name4 = Label(frame_6, text = str(Dict_Name[4]), font = ("Comic Sans", 11))
        label_5 = Label(frame_6, image = b_5)
        label_5.image = b_5
        label_name5 = Label(frame_6, text = str(Dict_Name[5]), font = ("Comic Sans", 11))
        label_6 = Label(frame_6, image = b_6)
        label_6.image = b_6
        label_name6 = Label(frame_6, text = str(Dict_Name[6]), font = ("Comic Sans", 11))
        label_7 = Label(frame_6, image = b_7)
        label_7.image = b_7
        label_name7 = Label(frame_6, text = str(Dict_Name[7]), font = ("Comic Sans", 11))
        label_8 = Label(frame_6, image = b_8)
        label_8.image = b_8
        label_name8 = Label(frame_6, text = str(Dict_Name[8]), font = ("Comic Sans", 11))

        #Price-Labels
        label_price1 = Label(frame_6, textvariable = PizzasPrices_List[0], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price2 = Label(frame_6, textvariable = PizzasPrices_List[1], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price3 = Label(frame_6, textvariable = PizzasPrices_List[2], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price4 = Label(frame_6, textvariable = PizzasPrices_List[3], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price5 = Label(frame_6, textvariable = PizzasPrices_List[4], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price6 = Label(frame_6, textvariable = PizzasPrices_List[5], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price7 = Label(frame_6, textvariable = PizzasPrices_List[6], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price8 = Label(frame_6, textvariable = PizzasPrices_List[7], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)

        #Option-Menus
        option_1a = OptionMenu(frame_6, Size_List[1], "Small", "Medium", "Large")
        option_1b = OptionMenu(frame_6, Quantity_List[1], "1", "2", "3")
        option_2a = OptionMenu(frame_6, Size_List[2], "Small", "Medium", "Large")
        option_2b = OptionMenu(frame_6, Quantity_List[2], "1", "2", "3")
        option_3a = OptionMenu(frame_6, Size_List[3], "Small", "Medium", "Large")
        option_3b = OptionMenu(frame_6, Quantity_List[3], "1", "2", "3")
        option_4a = OptionMenu(frame_6, Size_List[4], "Small", "Medium", "Large")
        option_4b = OptionMenu(frame_6, Quantity_List[4], "1", "2", "3")
        option_5a = OptionMenu(frame_6, Size_List[5], "Small", "Medium", "Large")
        option_5b = OptionMenu(frame_6, Quantity_List[5], "1", "2", "3")
        option_6a = OptionMenu(frame_6, Size_List[6], "Small", "Medium", "Large")
        option_6b = OptionMenu(frame_6, Quantity_List[6], "1", "2", "3")
        option_7a = OptionMenu(frame_6, Size_List[7], "Small", "Medium", "Large")
        option_7b = OptionMenu(frame_6, Quantity_List[7], "1", "2", "3")
        option_8a = OptionMenu(frame_6, Size_List[8], "Small", "Medium", "Large")
        option_8b = OptionMenu(frame_6, Quantity_List[8], "1", "2", "3")

        #AddtoCart Buttons
        button_1 = Button(frame_6, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(1))
        button_2 = Button(frame_6, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(2))
        button_3 = Button(frame_6, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(3))
        button_4 = Button(frame_6, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(4))
        button_5 = Button(frame_6, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(5))
        button_6 = Button(frame_6, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(6))
        button_7 = Button(frame_6, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(7))
        button_8 = Button(frame_6, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(8))


        #Packing
        frame_6.config(bg = "#282827")
        frame_6.grid(row = 2, column = 0, sticky = W+E)
        label_header.grid(row = 1, column = 0, columnspan = 8, sticky = W+E)
        label_blank1.grid(row = 2, rowspan = 11, column = 8)
        label_blank2.grid(row = 13, columnspan = 9, column = 0)


        #Label-Packing
        label_1.grid(row = 2, rowspan = 4, column = 0, padx = 20, pady = 20)
        label_name1.grid(row = 6, column = 0, sticky = S)
        label_2.grid(row = 2, rowspan = 4, column = 2, padx = 20, pady = 20)
        label_name2.grid(row = 6, column = 2, sticky = S)
        label_3.grid(row = 2, rowspan = 4, column = 4, padx = 20, pady = 20)
        label_name3.grid(row = 6, column = 4, sticky = S)
        label_4.grid(row = 2, rowspan = 4, column = 6, padx = 20, pady = 20)
        label_name4.grid(row = 6, column = 6, sticky = S)
        label_5.grid(row = 7, rowspan = 4, column = 0, padx = 20, pady = 20)
        label_name5.grid(row = 12, column = 0, sticky = S)
        label_6.grid(row = 7, rowspan = 4, column = 2, padx = 20, pady = 20)
        label_name6.grid(row = 12, column = 2, sticky = S)
        label_7.grid(row = 7, rowspan = 4, column = 4, padx = 20, pady = 20)
        label_name7.grid(row = 12, column = 4, sticky = S)
        label_8.grid(row = 7, rowspan = 4, column = 6, padx = 20, pady = 20)
        label_name8.grid(row = 12, column = 6, sticky = S)

        #Price-Labels Packing
        label_price1.grid(row = 4, column = 1, sticky = N)
        label_price2.grid(row = 4, column = 3, sticky = N)
        label_price3.grid(row = 4, column = 5, sticky = N)
        label_price4.grid(row = 4, column = 7, sticky = N)
        label_price5.grid(row = 9, column = 1, sticky = N)
        label_price6.grid(row = 9, column = 3, sticky = N)
        label_price7.grid(row = 9, column = 5, sticky = N)
        label_price8.grid(row = 9, column = 7, sticky = N)

        #Option-Menu Packing
        option_1a.grid(row = 2, column = 1, sticky = S)
        option_1a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_1b.grid(row = 3, column = 1, sticky = N)
        option_1b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_2a.grid(row = 2, column = 3, sticky = S)
        option_2a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_2b.grid(row = 3, column = 3, sticky = N)
        option_2b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_3a.grid(row = 2, column = 5, sticky = S)
        option_3a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_3b.grid(row = 3, column = 5, sticky = N)
        option_3b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_4a.grid(row = 2, column = 7, sticky = S)
        option_4a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_4b.grid(row = 3, column = 7, sticky = N)
        option_4b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_5a.grid(row = 7, column = 1, sticky = S)
        option_5a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_5b.grid(row = 8, column = 1, sticky = N)
        option_5b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_6a.grid(row = 7, column = 3, sticky = S)
        option_6a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_6b.grid(row = 8, column = 3, sticky = N)
        option_6b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_7a.grid(row = 7, column = 5, sticky = S)
        option_7a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_7b.grid(row = 8, column = 5, sticky = N)
        option_7b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_8a.grid(row = 7, column = 7, sticky = S)
        option_8a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_8b.grid(row = 8, column = 7, sticky = N)
        option_8b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)

        #Button Packing
        button_1.grid(row = 5, column = 1, sticky = N)
        button_2.grid(row = 5, column = 3, sticky = N)
        button_3.grid(row = 5, column = 5, sticky = N)
        button_4.grid(row = 5, column = 7, sticky = N)
        button_5.grid(row = 10, column = 1, sticky = N)
        button_6.grid(row = 10, column = 3, sticky = N)
        button_7.grid(row = 10, column = 5, sticky = N)
        button_8.grid(row = 10, column = 7, sticky = N)

    def Sides_Pack():
        frame_6.pack_forget()
        frame_6.grid_forget()
        frame_6.place_forget()
        frame_8.pack_forget()
        frame_8.grid_forget()
        frame_8.place_forget()

        label_header = Label(frame_7, text = "SIDES", font = ("Comic Sans", 18), bg ="#282827", fg = "ghostwhite", height = 2, width = 30)
        label_blank1 = Label(frame_7, text = "                ")
        label_blank2 = Label(frame_7, text = "   ")

        #Sides-ImageImport
        a_9 = img.open("Icons&Images/9.jpg")
        a_9 = a_9.resize((400, 200), img.ANTIALIAS)
        b_9 = imgtk.PhotoImage(a_9)
        a_10 = img.open("Icons&Images/10.jpg")
        a_10 = a_10.resize((400, 200), img.ANTIALIAS)
        b_10 = imgtk.PhotoImage(a_10)
        a_11 = img.open("Icons&Images/11.jpg")
        a_11 = a_11.resize((400, 200), img.ANTIALIAS)
        b_11 = imgtk.PhotoImage(a_11)
        a_12 = img.open("Icons&Images/12.jpg")
        a_12 = a_12.resize((400, 200), img.ANTIALIAS)
        b_12 = imgtk.PhotoImage(a_12)

        #Sides-Image_Ready
        label_9 = Label(frame_7, image = b_9)
        label_name9 = Label(frame_7, text = str(Dict_Name[9]), font = ("Comic Sans", 15))
        label_9.image = b_9
        label_10 = Label(frame_7, image = b_10)
        label_name10 = Label(frame_7, text = str(Dict_Name[10]), font = ("Comic Sans", 15))
        label_10.image = b_10
        label_11 = Label(frame_7, image = b_11)
        label_name11 = Label(frame_7, text = str(Dict_Name[11]), font = ("Comic Sans", 15))
        label_11.image = b_11
        label_12 = Label(frame_7, image = b_12)
        label_name12 = Label(frame_7, text = str(Dict_Name[12]), font = ("Comic Sans", 15))
        label_12.image = b_12

        #Price-Labels
        label_price9 = Label(frame_7, textvariable = SidesPrices_List[0], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price10 = Label(frame_7, textvariable = SidesPrices_List[1], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price11 = Label(frame_7, textvariable = SidesPrices_List[2], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price12 = Label(frame_7, textvariable = SidesPrices_List[3], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)

        #Option-Menus
        option_9a = OptionMenu(frame_7, Size_List[9], "Small", "Medium")
        option_9b = OptionMenu(frame_7, Quantity_List[9], "1", "2", "3")
        option_10a = OptionMenu(frame_7, Size_List[10], "Small", "Medium")
        option_10b = OptionMenu(frame_7, Quantity_List[10], "1", "2", "3")
        option_11a = OptionMenu(frame_7, Size_List[11], "Small", "Medium")
        option_11b = OptionMenu(frame_7, Quantity_List[11], "1", "2", "3")
        option_12a = OptionMenu(frame_7, Size_List[12], "Small", "Medium")
        option_12b = OptionMenu(frame_7, Quantity_List[12], "1", "2", "3")

        #AddtoCart Buttons
        button_9 = Button(frame_7, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(9))
        button_10 = Button(frame_7, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(10))
        button_11 = Button(frame_7, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(11))
        button_12 = Button(frame_7, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(12))


        #Packing
        frame_7.config(bg = "#282827")
        frame_7.grid(row = 2, column = 1, sticky = W+E)
        label_header.grid(row = 1, column = 0, columnspan = 4, sticky = W+E)
        label_blank1.grid(row = 2, rowspan = 11, column = 4)
        label_blank2.grid(row = 12, columnspan = 4, column = 0)

        #Labels-Packing
        label_9.grid(row = 2, rowspan = 4, column = 0, padx = 50, pady = 20)
        label_name9.grid(row = 6, column = 0, sticky = S)
        label_10.grid(row = 2, rowspan = 4, column = 2, padx = 50, pady = 20)
        label_name10.grid(row = 6, column = 2, sticky = S)
        label_11.grid(row = 7, rowspan = 4, column = 0, padx = 50, pady = 20)
        label_name11.grid(row = 11, column = 0, sticky = S)
        label_12.grid(row = 7, rowspan = 4, column = 2, padx = 50, pady = 20)
        label_name12.grid(row = 11, column = 2, sticky = S)

        #Price-Labels Packing
        label_price9.grid(row = 4, column = 1, sticky = N)
        label_price10.grid(row = 4, column = 3, sticky = N)
        label_price11.grid(row = 9, column = 1, sticky = N)
        label_price12.grid(row = 9, column = 3, sticky = N)

        #Option-Menu Packing
        option_9a.grid(row = 2, column = 1, sticky = S)
        option_9a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_9b.grid(row = 3, column = 1, sticky = N)
        option_9b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_10a.grid(row = 2, column = 3, sticky = S)
        option_10a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_10b.grid(row = 3, column = 3, sticky = N)
        option_10b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_11a.grid(row = 7, column = 1, sticky = S)
        option_11a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_11b.grid(row = 8, column = 1, sticky = N)
        option_11b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_12a.grid(row = 7, column = 3, sticky = S)
        option_12a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_12b.grid(row = 8, column = 3, sticky = N)
        option_12b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)

        #Button Packing
        button_9.grid(row = 5, column = 1, sticky = N)
        button_10.grid(row = 5, column = 3, sticky = N)
        button_11.grid(row = 10, column = 1, sticky = N)
        button_12.grid(row = 10, column = 3, sticky = N)

    def Beverages_Pack():
        print("d")
        frame_6.pack_forget()
        frame_6.grid_forget()
        frame_6.place_forget()
        frame_7.pack_forget()
        frame_7.grid_forget()
        frame_7.place_forget()

        label_header = Label(frame_8, text = "BEVERAGES", font = ("Comic Sans", 18), bg ="#282827", fg = "ghostwhite", height = 2, width = 30)
        label_blank1 = Label(frame_8, text = "                ")
        label_blank2 = Label(frame_8, text = "   ")

        #Sides-ImageImport
        a_13 = img.open("Icons&Images/13.png")
        a_13 = a_13.resize((400, 200), img.ANTIALIAS)
        b_13 = imgtk.PhotoImage(a_13)
        a_14 = img.open("Icons&Images/14.png")
        a_14 = a_14.resize((400, 200), img.ANTIALIAS)
        b_14 = imgtk.PhotoImage(a_14)
        a_15 = img.open("Icons&Images/15.jpg")
        a_15 = a_15.resize((400, 200), img.ANTIALIAS)
        b_15 = imgtk.PhotoImage(a_15)
        a_16 = img.open("Icons&Images/16.png")
        a_16 = a_16.resize((400, 200), img.ANTIALIAS)
        b_16 = imgtk.PhotoImage(a_16)

        #Sides-Image_Ready
        label_13 = Label(frame_8, image = b_13)
        label_name13 = Label(frame_8, text = str(Dict_Name[13]), font = ("Comic Sans", 15))
        label_13.image = b_13
        label_14 = Label(frame_8, image = b_14)
        label_name14 = Label(frame_8, text = str(Dict_Name[14]), font = ("Comic Sans", 15))
        label_14.image = b_14
        label_15 = Label(frame_8, image = b_15)
        label_name15 = Label(frame_8, text = str(Dict_Name[15]), font = ("Comic Sans", 15))
        label_15.image = b_15
        label_16 = Label(frame_8, image = b_16)
        label_name16 = Label(frame_8, text = str(Dict_Name[16]), font = ("Comic Sans", 15))
        label_16.image = b_16

        #Price-Labels
        label_price13 = Label(frame_8, textvariable = BeveragesPrices_List[0], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price14 = Label(frame_8, textvariable = BeveragesPrices_List[1], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price15 = Label(frame_8, textvariable = BeveragesPrices_List[2], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)
        label_price16 = Label(frame_8, textvariable = BeveragesPrices_List[3], font = ("Comic Sans", 10), bg ="gray95", fg = "gray10", height = 3, width = 10)

        #Option-Menus
        option_13a = OptionMenu(frame_8, Size_List[13], "Small", "Medium", "Large")
        option_13b = OptionMenu(frame_8, Quantity_List[13], "1", "2", "3")
        option_14a = OptionMenu(frame_8, Size_List[14], "Small", "Medium", "Large")
        option_14b = OptionMenu(frame_8, Quantity_List[14], "1", "2", "3")
        option_15a = OptionMenu(frame_8, Size_List[15], "Small", "Medium", "Large")
        option_15b = OptionMenu(frame_8, Quantity_List[15], "1", "2", "3")
        option_16a = OptionMenu(frame_8, Size_List[16], "Small", "Medium", "Large")
        option_16b = OptionMenu(frame_8, Quantity_List[16], "1", "2", "3")

        #AddtoCart Buttons
        button_13 = Button(frame_8, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(13))
        button_14 = Button(frame_8, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(14))
        button_15 = Button(frame_8, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(15))
        button_16 = Button(frame_8, text="Add To Cart", bg = "gray30", fg = "ghostwhite", command= lambda: DropDown_Input(16))


        #Packing
        frame_8.config(bg = "#282827")
        frame_8.grid(row = 2, column = 1, sticky = W+E)
        label_header.grid(row = 1, column = 0, columnspan = 4, sticky = W+E)
        label_blank1.grid(row = 2, rowspan = 11, column = 4)
        label_blank2.grid(row = 12, columnspan = 4, column = 0)

        #Labels-Packing
        label_13.grid(row = 2, rowspan = 4, column = 0, padx = 50, pady = 20)
        label_name13.grid(row = 6, column = 0, sticky = S)
        label_14.grid(row = 2, rowspan = 4, column = 2, padx = 50, pady = 20)
        label_name14.grid(row = 6, column = 2, sticky = S)
        label_15.grid(row = 7, rowspan = 4, column = 0, padx = 50, pady = 20)
        label_name15.grid(row = 11, column = 0, sticky = S)
        label_16.grid(row = 7, rowspan = 4, column = 2, padx = 50, pady = 20)
        label_name16.grid(row = 11, column = 2, sticky = S)

        #Price-Labels Packing
        label_price13.grid(row = 4, column = 1, sticky = N)
        label_price14.grid(row = 4, column = 3, sticky = N)
        label_price15.grid(row = 9, column = 1, sticky = N)
        label_price16.grid(row = 9, column = 3, sticky = N)

        #Option-Menu Packing
        option_13a.grid(row = 2, column = 1, sticky = S)
        option_13a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_13b.grid(row = 3, column = 1, sticky = N)
        option_13b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_14a.grid(row = 2, column = 3, sticky = S)
        option_14a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_14b.grid(row = 3, column = 3, sticky = N)
        option_14b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_15a.grid(row = 7, column = 1, sticky = S)
        option_15a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_15b.grid(row = 8, column = 1, sticky = N)
        option_15b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_16a.grid(row = 7, column = 3, sticky = S)
        option_16a.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)
        option_16b.grid(row = 8, column = 3, sticky = N)
        option_16b.config(bg ="gray93", fg = "gray10", width = 7, highlightthickness = 0)

        #Button Packing
        button_13.grid(row = 5, column = 1, sticky = N)
        button_14.grid(row = 5, column = 3, sticky = N)
        button_15.grid(row = 10, column = 1, sticky = N)
        button_16.grid(row = 10, column = 3, sticky = N)

    #Main
    button_VegPizza = Button(frame_9, text = "PIZZAS", font = ("Comic Sans", 14), bg = "gray20", fg = "white", height = 2, width = 27, command = Pizzas_Pack)
    button_Sides = Button(frame_9, text = "SIDES", font = ("Comic Sans", 14), bg = "gray20", fg = "white", height = 2, width = 27, command = Sides_Pack)
    button_Beverages = Button(frame_9, text = "BEVERAGES", font = ("Comic Sans", 14), bg = "gray20", fg = "white", height = 2, width = 27, command = Beverages_Pack)
    button_Bill = Button(frame_9, text = "BILL", font = ("Comic Sans", 14), bg = "gray20", fg = "ghostwhite", height = 2, width = 27, command = lambda: DropDown_Input(0))

    #Main-Packing
    frame_menu.config(bg = "#282827")
    frame_menu.place(x = 35, y = 25)

    #Frame-9(Header)
    frame_9.config(bg = "#282827")
    frame_9.grid(row = 1, column = 0, columnspan = 8, sticky = W+E)
    button_VegPizza.grid(row = 1, column = 0, sticky = W)
    button_Sides.grid(row = 1, column = 1,)
    button_Beverages.grid(row = 1, column = 2)
    button_Bill.grid(row = 1, column = 3, sticky = E)

    Pizzas_Pack()


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

    global root, frame_6, frame_7, frame_8, frame_9, frame_11, frame_13, frame_14, Order_Total

    k = 0
    Item_List = []
    Quantity_List = []
    Size_List = []
    Price_List = []
    Label_Item_List = []
    Label_Size_List = []
    Label_Quantity_List = []
    Label_Price_List = []

    frame_menu.destroy()
    frame_6.destroy()
    frame_7.destroy()
    frame_8.destroy()
    frame_9.destroy()

    for i in amount_list:
        Order_Total += i

    Total = StringVar()
    Total.set("Your total payable amount is : " + str(Order_Total))

    #StringVars
    for i in order_list:
        #Items Stringvars
        a = i[0]
        Item = StringVar()
        Item.set(str(Dict_Name[a]))
        Item_List.append(Item)

        #Size Stringvars
        Size = StringVar()
        Size.set(i[1])
        Size_List.append(Size)

        #Quantity Stringvars
        Quantity = StringVar()
        Quantity.set(str(i[2]))
        Quantity_List.append(Quantity)

        #Price Stringvars
        Price = StringVar()
        Price.set(str(amount_list[k]))
        Price_List.append(Price)
        k += 1

    label_header = Label(frame_11, text = "Total Bill", font = ("Comic Sans", 18), bg ="#282827", fg = "ghostwhite", height = 2, width = 30)

    #Sub-Frame-Bill Labels
    label_itemsheader = Label(frame_15, text = "Your Order Details", font = ("Comic Sans", 16), bg ="gray25", fg = "ghostwhite", height = 2, width = 20)
    label_name_itemheader = Label(frame_15, text = "Item", font = ("Comic Sans", 13), bg ="gray30", fg = "ghostwhite", height = 2, width = 20)
    label_name_sizeheader = Label(frame_15, text = "Quantity", font = ("Comic Sans", 13), bg ="gray30", fg = "ghostwhite", height = 2, width = 20)
    label_name_quantityheader = Label(frame_15, text = "Size", font = ("Comic Sans", 13), bg ="gray30", fg = "ghostwhite", height = 2, width = 20)
    label_name_priceheader = Label(frame_15, text = "Price", font = ("Comic Sans", 13), bg ="gray30", fg = "ghostwhite", height = 2, width = 20)

    for i in Item_List:
        label_Item = Label(frame_15, textvariable = i, font = ("Comic Sans", 12), bg = "gray35", fg = "white", height = 2, width = 20)
        Label_Item_List.append(label_Item)

    for i in Size_List:
        label_Size = Label(frame_15, textvariable = i, font = ("Comic Sans", 12), bg = "gray35", fg = "white", height = 2, width = 20)
        Label_Size_List.append(label_Size)

    for i in Quantity_List:
        label_Quantity = Label(frame_15, textvariable = i, font = ("Comic Sans", 12), bg = "gray35", fg = "white", height = 2, width = 20)
        Label_Quantity_List.append(label_Quantity)

    for i in Price_List:
        label_Price = Label(frame_15, textvariable = i, font = ("Comic Sans", 12), bg = "gray35", fg = "white", height = 2, width = 20)
        Label_Price_List.append(label_Price)

    label_Total = Label(frame_15, textvariable = Total, font = ("Comic Sans", 15), bg = "gray25", fg = "white", height = 2, width = 20)

    #Sub-Frame-Name Labels
    label_subheader_info = Label(frame_13, text = "Fill in the following Details :", font = ("Comic Sans", 16), bg ="gray25", fg = "ghostwhite", height = 2, width = 35)
    label_info_1 = Label(frame_13, text = "Name :", font = ("Comic Sans", 13), bg = "gray35", fg = "white", height = 2, width = 20)
    label_info_2 = Label(frame_13, text = "Phone :", font = ("Comic Sans", 13), bg = "gray35", fg = "white", height = 2, width = 20)
    label_info_3 = Label(frame_13, text = "Email :", font = ("Comic Sans", 13), bg = "gray35", fg = "white", height = 2, width = 20)

    Info_entry_name = Entry(frame_13, font = ("Comic Sans", 20), bg = "white", fg = "gray11", width = 15)
    Info_entry_phone = Entry(frame_13, font = ("Comic Sans", 20), bg = "white", fg = "gray11", width = 15)
    Info_entry_email = Entry(frame_13, font = ("Comic Sans", 20), bg = "white", fg = "gray11", width = 15)


    #Sub-Frame-Address Labels
    label_subheader_address = Label(frame_14, text = "Enter your address Details :", font = ("Comic Sans", 16), bg ="gray25", fg = "ghostwhite", height = 2, width = 35)
    label_address_1 = Label(frame_14, text = "House No: ", font = ("Comic Sans", 13), bg = "gray35", fg = "white", height = 2, width = 20)
    label_address_2 = Label(frame_14, text = "Locality: ", font = ("Comic Sans", 13), bg = "gray35", fg = "white", height = 2, width = 20)
    label_address_3 = Label(frame_14, text = "City: ", font = ("Comic Sans", 13), bg = "gray35", fg = "white", height = 2, width = 20)

    Address_entry_houseno = Entry(frame_14, font = ("Comic Sans", 20), bg = "white", fg = "gray11", width = 15)
    Address_entry_locality = Entry(frame_14, font = ("Comic Sans", 20), bg = "white", fg = "gray11", width = 15)
    Address_entry_city = Entry(frame_14, font = ("Comic Sans", 20), bg = "white", fg = "gray11", width = 15)

    button_1 = Button(frame_11, text = "Place Order", font = ("Comic Sans", 14), bg = "gray20", fg = "white", height = 2, width = 15, command = lambda : Input_PlacedOrder(Info_entry_name, Info_entry_phone, Info_entry_email,
                                                                                                                                                                           Address_entry_houseno, Address_entry_locality, Address_entry_city))

    #Packing
    frame_11.config(bg = "snow")
    frame_11.place(x= 90, y = 20)
    label_header.grid(row = 1, column = 0, columnspan = 3, sticky = W+E)

    frame_13.config(bg = "#282827")
    frame_13.grid(row = 2, column = 0, padx = 25, pady = 40)
    label_subheader_info.grid(row = 1, column = 0, columnspan = 3, sticky = W+E)
    label_info_1.grid(row = 2, column = 0, sticky = E, padx = 10, ipadx = 10, pady = 10)
    label_info_2.grid(row = 3, column = 0, sticky = E, padx = 10, ipadx = 10)
    label_info_3.grid(row = 4, column = 0, sticky = E, padx = 10, ipadx = 10, pady = 10)

    Info_entry_name.grid(row = 2, column = 1, sticky = W, padx = 10)
    Info_entry_phone.grid(row = 3, column = 1, sticky = W, padx = 10)
    Info_entry_email.grid(row = 4, column = 1, sticky = W, padx = 10)

    frame_14.config(bg = "#282827")
    frame_14.grid(row = 2, column = 2, padx = 25, pady = 40)
    label_subheader_address.grid(row = 1, column = 0, columnspan = 2, sticky = W+E)
    label_address_1.grid(row = 2, column = 0, sticky = E, padx = 10, ipadx = 10, pady = 10)
    label_address_2.grid(row = 3, column = 0, sticky = E, padx = 10, ipadx = 10)
    label_address_3.grid(row = 4, column = 0, sticky = E, padx = 10, ipadx = 10, pady = 10)

    Address_entry_houseno.grid(row = 2, column = 1, sticky = W, padx = 10)
    Address_entry_locality.grid(row = 3, column = 1, sticky = W, padx = 10)
    Address_entry_city.grid(row = 4, column = 1, sticky = W, padx = 10)

    #Order Details
    frame_15.config(bg = "#282827")
    frame_15.grid(row = 3, column = 0, columnspan = 3)
    label_itemsheader.grid(row = 1, column = 0, columnspan =  4, sticky = W+E)
    label_name_itemheader.grid(row = 2, column = 0, padx = 20, pady = 10)
    label_name_quantityheader.grid(row = 2, column = 1, padx = 15, pady = 10)
    label_name_sizeheader.grid(row = 2, column = 2, padx = 15, pady = 10)
    label_name_priceheader.grid(row = 2, column = 3, padx = 20, pady = 10)

    m = 3
    for i in Label_Item_List:
        i.grid(row = m, column = 0)
        m += 1
    m = 3
    for i in Label_Size_List:
        i.grid(row = m, column = 1)
        m += 1
    m = 3
    for i in Label_Quantity_List:
        i.grid(row = m, column = 2)
        m += 1
    m = 3
    for i in Label_Price_List:
        i.grid(row = m, column = 3)
        m += 1

    label_Total.grid(row = m, column = 0, columnspan = 4, sticky = W+E, pady = 15)

    button_1.grid(row = 2, column = 1)


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

    c.execute('''CREATE TABLE IF NOT EXISTS Addresses(orderNo INTEGER,
                                        	          custID INTEGER,
                                        	          addrName TEXT,
                                        	          addrPhone INTEGER,
                                        	          addrEmail TEXT,
                                        	          addrHouseno TEXT,
                                        	          addrLocality TEXT,
                                        	          addrCity TEXT,
                                        	          PRIMARY KEY(orderNo)
                                                      FOREIGN KEY(custID) REFERENCES Customers(custID))
                                                      FOREIGN KEY(orderNo) REFERENCES Orders(orderNo)))''')

def Email_Check(email):

    if email == '':
        return 0

    else:
        c.execute('''SELECT custID
                     FROM Customers
                     WHERE custEmail = ?''', (email,))
        a = c.fetchone()
        if a == None:
            return 1
        else:
            return 2

def Phone_check(phone):

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
        return 2, None


def Password_retrival(email):

    c.execute('''SELECT custPassword
                 FROM Customers
                 WHERE custEmail = ?''', (email,))
    password = c.fetchone()
    return password[0]

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


def Custdata_entry(phone, name, email, password):

    c.execute('''SELECT custID
    FROM Customers
    WHERE custID = (SELECT MAX(custID) FROM Customers)''')
    a = c.fetchone()
    customerID = int(a[0] + 1)

    c.execute('''INSERT INTO Customers(custID, custPhone, custName, custEmail, custPassword)
    VALUES(?, ?, ?, ?, ?)''', (customerID, phone, name, email, password))

    conn.commit()

def Orderdata_entry(order_list, amount_list):

    global Order_Total, customerID, Order_No

    c.execute('''SELECT orderNo
                 FROM Orders
                 WHERE orderNo = (SELECT MAX(orderNo) FROM Orders)''')
    a = c.fetchone()
    Order_No = int(a[0] + 1)

    order_summ = json.dumps(order_list)
    t = datetime.datetime.now()
    timestamp = t.strftime('%d-%m-%Y %H:%M:%S')
    print(Order_No, customerID, order_list, Order_Total, timestamp)
    c.execute('''INSERT INTO Orders(orderNo, custID, orderSummary,
                                    orderTotal, orderDateTime)
                 VALUES(?,?,?,?,?)''', (Order_No, customerID, order_summ, Order_Total, timestamp))

    conn.commit()

def Addrdata_entry(name, phone, email, houseno, locality, city):

    global cutomerID, Order_No

    c.execute('''INSERT INTO Addresses(orderNo, custID, addrName, addrPhone,
                                       addrEmail, addrHouseno, addrLocality, addrCity)
                 VALUES(?,?,?,?,?,?,?,?)''', (Order_No, customerID, name, phone, email, houseno, locality, city))

    conn.commit()

Step_Home()
