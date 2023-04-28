def change_number():
    """This function changes the value passed in to 1 (global)"""
    global number
    number = 1
    print("In the Function: the number is:", number)

number = 5
print ("In Calling module, Global number is:", number)
change_number()
print ("After call to Function module, number is now:", number)

