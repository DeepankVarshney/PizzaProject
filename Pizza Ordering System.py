import os
import sys
import winsound
import time
#Pizza Order System 2.0
#R.M.Bacon
#Home Version
cost = 0.00
r = open("toppings.txt")
bases = ["small","medium","large"]
toppings = ["pepperoni","chicken","cajun-chicken","mushrooms",
            "red-onions","sweetcorn","ham","cheese","spicy-minced-beef",
            "anchovies","tuna","peppers","jalapenos","green-chillies"] #0-13

def smalltopp():
    os.system('cls')
    print("You have selected TO add toppings.")
    print("Your toppings are: ")
    print("\n" + toppings[0] + ", " + toppings[1] + ", " + toppings[2] + ", " + toppings[3] + ", " + toppings[4] + ", " + toppings[5] + ", " + toppings[6] + ", " + toppings[7] + ", ")
    print(toppings[8] + ", " + toppings[9] + ", " + toppings[10] + ", " + toppings[11] + ", " + toppings[12] + ", " + toppings[13])#0-13

    count = -1
    checkout = False
    while checkout == False:
        count += 1
        f = open("toppings.txt", "a")
        i = open("currentTopps.txt", "a")
        topps = input("Please select a topping or press enter/return to pay: ")
        f.write(topps + "\n")
        i.write(topps + " ")
        i.close()
        f.close()
        if topps == toppings[0]:
            print("----- " + toppings[0] + " added -----")
        elif topps == toppings[1]:
            print("----- " + toppings[1] + " added -----")
        elif topps == toppings[2]:
            print("----- " + toppings[2] + " added -----")
        elif topps == toppings[3]:
            print("----- " + toppings[3] + " added -----")
        elif topps == toppings[4]:
            print("----- " + toppings[4] + " added -----")
        elif topps == toppings[5]:
            print("----- " + toppings[5] + " added -----")
        elif topps == toppings[6]:
            print("----- " + toppings[6] + " added -----")
        elif topps == toppings[7]:
            print("----- " + toppings[7] + " added -----")
        elif topps == toppings[8]:
            print("----- " + toppings[8] + " added -----")
        elif topps == toppings[9]:
            print("----- " + toppings[9] + " added -----")
        elif topps == toppings[10]:
            print("----- " + toppings[10] + " added -----")
        elif topps == toppings[11]:
            print("----- " + toppings[11] + " added -----")
        elif topps == toppings[12]:
            print("----- " + toppings[12] + " added -----")
        elif topps == toppings[13]:
            print("----- " + toppings[13] + " added -----")
        elif topps == '':
            checkout = True
    h = open("currentTopps.txt")
    print("\nYou have ordered a small pizza base with " + h.read())
    p = open("currentTopps.txt", "w")
    p.write("toppings: ")
    p.close()
    afterTopps = count * 75 / 100
    endTotal = afterTopps + 2.50
    print("Your total cost is now £{:.2f} ".format(endTotal))
    print("\nDo you want to have your pizza delivered or do you want to collect it.")
    print("THERE IS A 10% DISCOUNT WHEN YOU COLLECT!")
    deliverOrCollect = input("'d' for deliver, 'c' for collect: ")
    if deliverOrCollect == "d":
        correctAddress = False
        while correctAddress == False:
            address = input("\nPlease enter your address line for delivery: ")
            postCode = input("Please enter your post code for delivery: ")
            print("\nYour chosen address is " + address + ", " + postCode + ".")
            correct = input("\nIs this correct? (y/n) ")
            if correct == "y":
                correctAddress = True
            elif correct == "n":
                os.system('cls')
                correctAddress = False
        os.system('cls')
        print("Your order is on it's way! Please have £{:.2f} ".format(endTotal) + " ready for the driver.")
    elif deliverOrCollect == "c":
        os.system('cls')
        print("You have chosen to collect your pizza.")
        discount = endTotal / 10
        discountTotal = endTotal - discount
        print("\nWhen you collect you pizza please have £{:.2f} ".format(discountTotal) + " ready to pay.")

    leave = input("\nType 'e' to exit: ")
    if leave == "e":
        sys.exit(0)

def smallcheckout():
    os.system('cls')
    print("You have slected NOT TO add toppings.")
    print("Your current total cost is £2.50")
    print("\nDo you want to have your pizza delivered or do you want to collect it.")
    print("THERE IS A 10% DISCOUNT WHEN YOU COLLECT!")
    deliverOrCollect = input("'d' for deliver, 'c' for collect: ")
    if deliverOrCollect == "d":
        correctAddress = False
        while correctAddress == False:
            address = input("\nPlease enter your address line for delivery: ")
            postCode = input("Please enter your post code for delivery: ")
            print("\nYour chosen address is " + address + ", " + postCode + ".")
            correct = input("\nIs this correct? (y/n) ")
            if correct == "y":
                correctAddress = True
            elif correct == "n":
                os.system('cls')
                correctAddress = False
        os.system('cls')
        print("Your order is on it's way! Please have £2.50 ready for the driver.")
    elif deliverOrCollect == "c":
        os.system('cls')
        print("You have chosen to collect your pizza.")
        print("\nWhen you collect you pizza please have £2.25 ready to pay.")

    leave = input("\nType 'e' to exit: ")
    if leave == "e":
        sys.exit(0)

def medtopp():
    os.system('cls')
    print("You have selected TO add toppings.")
    print("Your toppings are: ")
    print("\n" + toppings[0] + ", " + toppings[1] + ", " + toppings[2] + ", " + toppings[3] + ", " + toppings[4] + ", " + toppings[5] + ", " + toppings[6] + ", " + toppings[7] + ", ")
    print(toppings[8] + ", " + toppings[9] + ", " + toppings[10] + ", " + toppings[11] + ", " + toppings[12] + ", " + toppings[13])#0-13

    count = -1
    checkout = False
    while checkout == False:
        count += 1
        f = open("toppings.txt", "a")
        i = open("currentTopps.txt", "a")
        topps = input("Please select a topping or press enter/return to pay: ")
        f.write(topps + "\n")
        i.write(topps + " ")
        i.close()
        f.close()
        if topps == toppings[0]:
            print("----- " + toppings[0] + " added -----")
        elif topps == toppings[1]:
            print("----- " + toppings[1] + " added -----")
        elif topps == toppings[2]:
            print("----- " + toppings[2] + " added -----")
        elif topps == toppings[3]:
            print("----- " + toppings[3] + " added -----")
        elif topps == toppings[4]:
            print("----- " + toppings[4] + " added -----")
        elif topps == toppings[5]:
            print("----- " + toppings[5] + " added -----")
        elif topps == toppings[6]:
            print("----- " + toppings[6] + " added -----")
        elif topps == toppings[7]:
            print("----- " + toppings[7] + " added -----")
        elif topps == toppings[8]:
            print("----- " + toppings[8] + " added -----")
        elif topps == toppings[9]:
            print("----- " + toppings[9] + " added -----")
        elif topps == toppings[10]:
            print("----- " + toppings[10] + " added -----")
        elif topps == toppings[11]:
            print("----- " + toppings[11] + " added -----")
        elif topps == toppings[12]:
            print("----- " + toppings[12] + " added -----")
        elif topps == toppings[13]:
            print("----- " + toppings[13] + " added -----")
        elif topps == '':
            checkout = True
    h = open("currentTopps.txt")
    print("\nYou have ordered a medium pizza base with " + h.read())
    p = open("currentTopps.txt", "w")
    p.write("toppings: ")
    p.close()
    afterTopps = count * 75 / 100
    endTotal = afterTopps + 3.00
    print("Your total cost is now £{:.2f} ".format(endTotal))
    print("\n Do you want to have your pizza delivered or do you want to collect it.")
    print("THERE IS A 10% DISCOUNT WHEN YOU COLLECT!")
    deliverOrCollect = input("'d' for deliver, 'c' for collect: ")
    if deliverOrCollect == "d":
        correctAddress = False
        while correctAddress == False:
            address = input("\nPlease enter your address line for delivery: ")
            postCode = input("Please enter your post code for delivery: ")
            print("\nYour chosen address is " + address + ", " + postCode + ".")
            correct = input("\nIs this correct? (y/n) ")
            if correct == "y":
                correctAddress = True
            elif correct == "n":
                os.system('cls')
                correctAddress = False
        os.system('cls')
        print("Your order is on it's way! Please have £{:.2f} ".format(endTotal) + " ready for the driver.")
    elif deliverOrCollect == "c":
        os.system('cls')
        print("You have chosen to collect your pizza.")
        discount = endTotal / 10
        discountTotal = endTotal - discount
        print("\nWhen you collect you pizza please have £{:.2f} ".format(discountTotal) + " ready to pay.")

    leave = input("\nType 'e' to exit: ")
    if leave == "e":
        sys.exit(0)

def medcheckout():
    os.system('cls')
    print("You have slected NOT TO add toppings.")
    print("Your current total cost is £3.00")
    print("\nDo you want to have your pizza delivered or do you want to collect it.")
    print("THERE IS A 10% DISCOUNT WHEN YOU COLLECT!")
    deliverOrCollect = input("'d' for deliver, 'c' for collect: ")
    if deliverOrCollect == "d":
        correctAddress = False
        while correctAddress == False:
            address = input("\nPlease enter your address line for delivery: ")
            postCode = input("Please enter your post code for delivery: ")
            print("\nYour chosen address is " + address + ", " + postCode + ".")
            correct = input("\nIs this correct? (y/n) ")
            if correct == "y":
                correctAddress = True
            elif correct == "n":
                os.system('cls')
                correctAddress = False
        os.system('cls')
        print("Your order is on it's way! Please have £3.00 ready for the driver.")
    elif deliverOrCollect == "c":
        os.system('cls')
        print("You have chosen to collect your pizza.")
        print("\nWhen you collect you pizza please have £2.70 ready to pay.")

    leave = input("\nType 'e' to exit: ")
    if leave == "e":
        sys.exit(0)

def largetopp():
    os.system('cls')
    print("You have selected TO add toppings.")
    print("Your toppings are: ")
    print("\n" + toppings[0] + ", " + toppings[1] + ", " + toppings[2] + ", " + toppings[3] + ", " + toppings[4] + ", " + toppings[5] + ", " + toppings[6] + ", " + toppings[7] + ", ")
    print(toppings[8] + ", " + toppings[9] + ", " + toppings[10] + ", " + toppings[11] + ", " + toppings[12] + ", " + toppings[13])#0-13

    count = -1
    checkout = False
    while checkout == False:
        count += 1
        f = open("toppings.txt", "a")
        i = open("currentTopps.txt", "a")
        topps = input("Please select a topping or press enter/return to pay: ")
        f.write(topps + "\n")
        i.write(topps + " ")
        i.close()
        f.close()
        if topps == toppings[0]:
            print("----- " + toppings[0] + " added -----")
        elif topps == toppings[1]:
            print("----- " + toppings[1] + " added -----")
        elif topps == toppings[2]:
            print("----- " + toppings[2] + " added -----")
        elif topps == toppings[3]:
            print("----- " + toppings[3] + " added -----")
        elif topps == toppings[4]:
            print("----- " + toppings[4] + " added -----")
        elif topps == toppings[5]:
            print("----- " + toppings[5] + " added -----")
        elif topps == toppings[6]:
            print("----- " + toppings[6] + " added -----")
        elif topps == toppings[7]:
            print("----- " + toppings[7] + " added -----")
        elif topps == toppings[8]:
            print("----- " + toppings[8] + " added -----")
        elif topps == toppings[9]:
            print("----- " + toppings[9] + " added -----")
        elif topps == toppings[10]:
            print("----- " + toppings[10] + " added -----")
        elif topps == toppings[11]:
            print("----- " + toppings[11] + " added -----")
        elif topps == toppings[12]:
            print("----- " + toppings[12] + " added -----")
        elif topps == toppings[13]:
            print("----- " + toppings[13] + " added -----")
        elif topps == '':
            checkout = True
    h = open("currentTopps.txt")
    print("\nYou have ordered a large pizza base with " + h.read())
    p = open("currentTopps.txt", "w")
    p.write("toppings: ")
    p.close()
    afterTopps = count * 75 / 100
    endTotal = afterTopps + 4.00
    print("Your total cost is now £{:.2f} ".format(endTotal))
    print("\n Do you want to have your pizza delivered or do you want to collect it.")
    print("THERE IS A 10% DISCOUNT WHEN YOU COLLECT!")
    deliverOrCollect = input("'d' for deliver, 'c' for collect: ")
    if deliverOrCollect == "d":
        correctAddress = False
        while correctAddress == False:
            address = input("\nPlease enter your address line for delivery: ")
            postCode = input("Please enter your post code for delivery: ")
            print("\nYour chosen address is " + address + ", " + postCode + ".")
            correct = input("\nIs this correct? (y/n) ")
            if correct == "y":
                correctAddress = True
            elif correct == "n":
                os.system('cls')
                correctAddress = False
        os.system('cls')
        print("Your order is on it's way! Please have £{:.2f} ".format(endTotal) + " ready for the driver.")
    elif deliverOrCollect == "c":
        os.system('cls')
        print("You have chosen to collect your pizza.")
        discount = endTotal / 10
        discountTotal = endTotal - discount
        print("\nWhen you collect you pizza please have £{:.2f} ".format(discountTotal) + " ready to pay.")

    leave = input("\nType 'e' to exit: ")
    if leave == "e":
        sys.exit(0)

def largecheckout():
    os.system('cls')
    print("You have slected NOT TO add toppings.")
    print("Your current total cost is £4.00")
    print("\nDo you want to have your pizza delivered or do you want to collect it.")
    print("THERE IS A 10% DISCOUNT WHEN YOU COLLECT!")
    deliverOrCollect = input("'d' for deliver, 'c' for collect: ")
    if deliverOrCollect == "d":
        correctAddress = False
        while correctAddress == False:
            address = input("\nPlease enter your address line for delivery: ")
            postCode = input("Please enter your post code for delivery: ")
            print("\nYour chosen address is " + address + ", " + postCode + ".")
            correct = input("\nIs this correct? (y/n) ")
            if correct == "y":
                correctAddress = True
            elif correct == "n":
                os.system('cls')
                correctAddress = False
        os.system('cls')
        print("Your order is on it's way! Please have £4.00 ready for the driver.")
    elif deliverOrCollect == "c":
        os.system('cls')
        print("You have chosen to collect your pizza.")
        print("\nWhen you collect you pizza please have £3.60 ready to pay.")

    leave = input("\nType 'e' to exit: ")
    if leave == "e":
        sys.exit(0)

#If user selected a small base
def small():
    os.system('cls')
    current = cost + 2.50
    print('Your current total cost is £{:.2f} '.format(current))
    topp = input("Do you want to add toppings to your pizza. EVERY TOPPING IS AN EXTRA 75P \n (y/n) ")
    if topp == "y":
        smalltopp()
    if topp == "n":
        smallcheckout()
    else:
        print("INVALID SELECTION")
        time.sleep(1)
        small()

    leave = input("Type 'e' to exit: ")
    if leave == "e":
        sys.exit(0)

#If user selected a medium base
def medium():
    os.system('cls')
    currentM = cost + 3
    print('Your current total cost is £{:.2f} '.format(currentM))

    topp = input("Do you want to add toppings to your pizza. EVERY TOPPING IS AN EXTRA 75P \n (y/n) ")
    if topp == "y":
        medtopp()
    if topp == "n":
        medcheckout()
    else:
        print("INVALID SELECTION")
        time.sleep(1)
        medium()

    leave = input("Type 'e' to exit: ")
    if leave == "e":
        sys.exit(0)

#If user selected a large base
def large():
    os.system('cls')
    currentL = cost + 4
    print('Your current total cost is £{:.2f} '.format(currentL))

    topp = input("Do you want to add toppings to your pizza. EVERY TOPPING IS AN EXTRA 75P \n (y/n) ")
    if topp == "y":
        largetopp()
    if topp == "n":
        largecheckout()
    else:
        print("INVALID SELECTION")
        time.sleep(1)
        large()

    leave = input("Type 'e' to exit: ")
    if leave == "e":
        sys.exit(0)


#Intro
def intro():
    print("------------------------------------------")
    print("--------Welcome To The Pauls Pizza--------")
    print("------------------------------------------")

#Customer Log-on
def customer():
    print("\nYou Have Chosen To Log-in As A Customer...")

    base = input("Select a base: " + bases[0] + "(s) (£2.50), " + bases[1] + "(m) (£3.00), " + bases[2] + "(l) (£4.00): ")
    if base == "s":
        print("You have selected a SMALL base...")
        time.sleep(.3)
        small()
    if base == "m":
        print("You have selected a MEDIUM base...")
        time.sleep(.3)
        medium()
    if base == "l":
        print("You have selected a LARGE base...")
        time.sleep(.3)
        large()


    #Allows user to choose to exit
    leave = input("Type 'e' to exit: ")
    if leave == "e":
        sys.exit(0)

#Employee Log-on
def employee():
    print("\n You Have Chosen To Log-in As An Employee...")
    password = "cheese"
    entPass = input("Please input the login PASSWORD: ")
    if entPass == password:
        print("Processing........ \n")
        time.sleep(.5)
        os.system('cls')
        print("Welcome Employee!")
    else:
        print("Processing........ \n")
        time.sleep(.3)
        print("------------Try again------------")
        time.sleep(.3)
        employee()


    #Allows user to choose to exit
    leave = input("\nType 't' to check the toppings file or 'e' to exit: ")
    if leave == "e":
        sys.exit(0)
    if leave == "t":
       print("\n" + r.read())
       leave1 = input("\nPRESS ENTER/RETURN TO EXIT")
       if leave1 == "w":
           print("\nBYE!")
           time.sleep(1)
           sys.exit(0)
       else:
           print("\nBYE!")
           time.sleep(1)
           sys.exit(0)


#Main Start
def main():
    print("\n")
    intro()
    print("\n")
    user = input("Are you a customer or an employee? Please enter c or e: ")
    if user == "c":
        customer()
    if user == "e":
        employee()
    else:
        print("INVALID LOGON..")
        time.sleep(.3)
        main()
main()
