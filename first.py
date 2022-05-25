"""
Zach Bar
CS 3C
Practice Program 39, Ch 3
Input: PIN number
Processing: check if true and break if wrong 3x
Output: accept/decline
"""
numoftries=0
while (numoftries < 3): #makes sure process doesn't get repeated after third attempt
    pin = input("Please input your PIN number.")
    if (pin == "1234"):
        print("PIN is correct. Please proceed with your transaction")
        break #makes sure process doesnt get repeated after correct PIN input
    else:
        print("PIN is incorrect")
        numoftries= numoftries+1
if (numoftries == 3):
    print("You are locked from accessing this ATM. Have a good day!")