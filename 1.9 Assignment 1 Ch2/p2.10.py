# Works on python 3.10 and above!
print('\nWelcome to P2.10 Car selector')

# What are the inputs?

# def name() or def add(num1, num2)
# this is a method/function declaration kinda like main
# it allows me to organize a block of code and even pass data into it if wanted
# Think multiple individual programs in one
# You can run these individually and test each one for errors/easier debugging

# A function can have a return or no returns
# having a return means you can get the value of whatever operations you make in there.
# aka def add(num1, num2) can return the sum of two numbers
# ex: def add(num1, num2):
#         sum = num1+num2
#         return sum
# this 'pops out' the total 


def getcarcost():
    # A while(True) statement continues until the loop is broken out of via break, return, or other means
    # This means it infinitly loops so BE CAREFUL!
    while(True):
        # a try statement lets me test a block of code to check for errors
        try:
            # Get user input of car cost, cast it float in case of decimals
            carCost = float(input('Please enter cost of car (num): '))
            # Since it did not error out, this function will 'pop out'/return/give back whatever you told it to do
            # thus the RETURN aspect
            return carCost
        
        # if not convertible to float, error out and ask for a valid entry (aka numbers only)
        # So what the except ValueError line does is if I try to case my input into a float and it doesn't work
        # aka float(21a4f) this clearly cannot become a float number therefore this line catches it
        # and tells the user to actually put a number that works hence the try statement and its valid, continue on
        except ValueError:
            print('Invalid Input!')
    
def getmiles():
    # A while(True) statement continues until the loop is broken out of via break, return, or other means
    # This means it infinitly loops so BE CAREFUL!
    while(True):
        # a try statement lets me test a block of code to check for errors
        try:
            # Get user input of miles, cast it float in case of decimals
            totalMiles = float(input('Please enter miles (num): '))
            # Since it did not error out, this function will 'pop out'/return/give back whatever you told it to do
            # thus the RETURN aspect
            return totalMiles
        
        # if not convertible to float, error out and ask for a valid entry (aka numbers only)
        # if invalid, catch error and print invalid
        # So what the except ValueError line does is if I try to case my input into a float and it doesn't work
        # aka float(21a4f) this clearly cannot become a float number therefore this line catches it
        # and tells the user to actually put a number that works hence the try statement and its valid, continue on
        except ValueError:
            print('Invalid Input!')
        
def getgascost():
    # A while(True) statement continues until the loop is broken out of via break, return, or other means
    # This means it infinitly loops so BE CAREFUL!
    while(True):
        # a try statement lets me test a block of code to check for errors
        try:
            # Get user input of gas cost, cast it float in case of decimals (since gas prices are usually dollar then cents)
            gasPrice = float(input('Please enter cost of gas (num): '))
            # Since it did not error out, this function will 'pop out'/return/give back whatever you told it to do
            # thus the RETURN aspect
            return gasPrice
        
        # if not convertible to float, error out and ask for a valid entry (aka numbers only)
        # if invalid, catch error and print invalid
        # So what the except ValueError line does is if I try to case my input into a float and it doesn't work
        # aka float(21a4f) this clearly cannot become a float number therefore this line catches it
        # and tells the user to actually put a number that works hence the try statement and its valid, continue on
        except ValueError:
            print('Invalid Input!')
            
def geteff():
    # A while(True) statement continues until the loop is broken out of via break, return, or other means
    # This means it infinitly loops so BE CAREFUL!
    while(True):
        # a try statement lets me test a block of code to check for errors
        try:
            # Get user input of miles per gallon, cast it float in case of decimals
            milesPerGalon = float(input('Please enter mpg (num): '))
            # Since it did not error out, this function will 'pop out'/return/give back whatever you told it to do
            # thus the RETURN aspect
            return milesPerGalon
        
        # if not convertible to float, error out and ask for a valid entry (aka numbers only)
        # if invalid, catch error and print invalid
        # So what the except ValueError line does is if I try to case my input into a float and it doesn't work
        # aka float(21a4f) this clearly cannot become a float number therefore this line catches it
        # and tells the user to actually put a number that works hence the try statement and its valid, continue on
        except ValueError:
            print('Invalid Input!')
            
def est():
    # A while(True) statement continues until the loop is broken out of via break, return, or other means
    # This means it infinitly loops so BE CAREFUL!
    while(True):
        # a try statement lets me test a block of code to check for errors
        try:
            # Get user input of restimated resale value, cast it float in case of decimals
            resaleValue = float(input('Please enter estimated resale value (num): '))
            # Since it did not error out, this function will 'pop out'/return/give back whatever you told it to do
            # thus the RETURN aspect
            return resaleValue
        
        # if not convertible to float, error out and ask for a valid entry (aka numbers only)
        # if invalid, catch error and print invalid
        # So what the except ValueError line does is if I try to case my input into a float and it doesn't work
        # aka float(21a4f) this clearly cannot become a float number therefore this line catches it
        # and tells the user to actually put a number that works hence the try statement and its valid, continue on
        except ValueError:
            print('Invalid Input!')

def total():
    # I call the est function and store the value it returns
    estm = est()
    # total cost would be car cost + miles over efficiency times gas cost for x amount of years
    # so what this basically does is it calls the functions necessary to get the total cost.
    # first it gets the car cost by calling its function, so now we have the value of the car from the return (if valid)
    # next it gets the miles value divided by mpg value the times the gas cost then times the year
    totalCost = getcarcost() + (((getmiles()/geteff())*getgascost())*float(input('How many years? ')))
    print('Total Cost of owning the car:         %10.2f' % totalCost+' dollars')     
    print('Resale value:                         %10.2f' % estm + ' dollars')
    # To get net loss/profit, subtract total from estimate
    print('Net profit/loss:                      %10.2f' % (estm-totalCost) + ' dollars')       

def main():
    total()
    
main()