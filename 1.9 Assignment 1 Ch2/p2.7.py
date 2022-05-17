# Works on python 3.10 and above!

print('\nWelcome to P2.7 radius into area, circumpherence, volume, and surface area')

# constant pi
PI = 3.14159265359

# A while(True) statement continues until the loop is broken out of via break, return, or other means
# This means it infinitly loops so BE CAREFUL!
while(True):
    # a try statement lets me test a block of code to check for errors
    try:
        # What are the inputs?
        # Get user input radius, cast it into a float just in case decimals are used
        radius = float(input('Please enter radius of a circle/sphere (m): '))
        
        # if a valid input, break from loop
        break
    
    # if invalid, catch error and print invalid
    # So what the except ValueError line does is if I try to case my input into a float and it doesn't work
    # aka float(21a4f) this clearly cannot become a float number therefore this line catches it
    # and tells the user to actually put a number that works hence the try statement and its valid, continue on
    except ValueError:
        print('Invalid Input!')

# What are the desired outputs?

# this is a method/function declaration kinda like main
# it allows me to organize a block of code and even pass data into it if wanted
# these functions are unnecessary as they are one liners, you can just remove the def ___ and it will run if placed in main

# Think multiple individual programs in one
# You can run these individually and test each one for errors/easier debugging

# A function can have a return or no returns
# having a return means you can get the value of whatever operations you make in there.
# aka def add(num1, num2) can return the sum of two numbers
# ex: def add(num1, num2):
#         sum = num1+num2
#         return sum
# this 'pops out' the total 


# these don't return anything, they just print, in C++/Java these would be void functions
def area():
    # print string area, add space, area is pi radius squared
    print('Area:         %10.2f' % (PI*(radius**2))+' meters')
    
def circum():
    # print string circumference, add space, circumference is 2pi*radius
    print('Circumference:%10.2f' % (2*PI*radius)+' meters')
    
def vol():
    # print string volume, add space, volume is 4/3pi*radius cubed
    print('Volume:       %10.2f' % ((4/3)*PI*(radius**3))+' meters')
    
def sarea():
    # print string volume, add space, surface area is 4pi*radius squared
    print('Surface Area: %10.2f' % (4*PI*(radius**2))+' meters')

# run all functions  
# the way to run functions is calling them by name(). This just runs all of them  
def runall():
    area()
    circum()
    vol()
    sarea()

# Switch just in case the user wants a specific output    
# A switch statement checks user input and compares
# it is kind of like a dictionary
# this function takes in an argument/like an input which is the user's choice in this case
def switch(val):
    # It asks to match the user's input to one of these choices then runs the program it matches too
    match val:
        # checks vak and compares like a dict.; runs the function that matches
        case 'circumference':
            return circum()
        case 'volume':
            return vol()
        case 'surface area':
            return sarea()
        case 'area':
            return area()
        case 'all':
            return runall()
        # The default case
        # If the user's input doesn't match any of the choices it goes here
        # aka if they input "joe" or "asdasdasd" or "1234" it work work
        # only if they input "Circumference" or "CIRCUMFERENCE"....
        # basically runs this function again and again until the user's input is valide
        case _:
            # base case/invalid inputs ask for a retry
            print('Invalid input, please try again')
            choice = input('What would you like? \nEnter AREA, CIRCUMFERENCE, VOLUME, SURFACE AREA, or ALL: ').lower()
            switch(choice)

def main():
    # Just asks the user input and turns it into lowercase for adaptability
    choice = input('What would you like? \nEnter AREA, CIRCUMFERENCE, VOLUME, SURFACE AREA, or ALL: ').lower()
    # runs the dictionary-like function above
    switch(choice)
    
main()