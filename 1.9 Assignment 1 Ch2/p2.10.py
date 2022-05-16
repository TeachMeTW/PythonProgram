# Works on python 3.10 and above!
print('\nWelcome to P2.10 Car selector')

# What are the inputs?

def getcarcost():
    while(True):
        try:
            # Get user input of car cost, cast it float in case of decimals
            carCost = float(input('Please enter cost of car (num): '))
            return carCost
        # if not convertible to float, error out and ask for a valid entry (aka numbers only)
        except ValueError:
            print('Invalid Input!')
    
def getmiles():
    while(True):
        try:
            # Get user input of miles, cast it float in case of decimals
            totalMiles = float(input('Please enter miles (num): '))
            return totalMiles
        # if not convertible to float, error out and ask for a valid entry (aka numbers only)
        except ValueError:
            print('Invalid Input!')
        
def getgascost():
    while(True):
        try:
            # Get user input of gas cost, cast it float in case of decimals (since gas prices are usually dollar then cents)
            gasPrice = float(input('Please enter cost of gas (num): '))
            return gasPrice
        # if not convertible to float, error out and ask for a valid entry (aka numbers only)
        except ValueError:
            print('Invalid Input!')
            
def geteff():
    while(True):
        try:
            # Get user input of miles per gallon, cast it float in case of decimals
            milesPerGalon = float(input('Please enter mpg (num): '))
            return milesPerGalon
        # if not convertible to float, error out and ask for a valid entry (aka numbers only)
        except ValueError:
            print('Invalid Input!')
            
def est():
    while(True):
        try:
            # Get user input of restimated resale value, cast it float in case of decimals
            resaleValue = float(input('Please enter estimated resale value (num): '))
            return resaleValue
        # if not convertible to float, error out and ask for a valid entry (aka numbers only)
        except ValueError:
            print('Invalid Input!')

def total():
    estm = est()
    # total cost would be car cost + miles over efficiency times gas cost for x amount of years
    totalCost = getcarcost() + (((getmiles()/geteff())*getgascost())*float(input('How many years? ')))
    print('Total Cost of owning the car:         %10.2f' % totalCost+' dollars')     
    print('Resale value:                         %10.2f' % estm + ' dollars')
    # To get net loss/profit, subtract total from estimate
    print('Net profit/loss:                      %10.2f' % (estm-totalCost) + ' dollars')       

def main():
    total()
    
main()