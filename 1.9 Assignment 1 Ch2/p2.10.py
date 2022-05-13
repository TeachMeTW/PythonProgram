


print('\nWelcome to P2.10 Car selector')


def getcarcost():
    while(True):
        try:
            ncost = float(input('Please enter cost of car (num): '))
            return ncost
        except ValueError:
            print('Invalid Input!')
    
def getmiles():
    while(True):
        try:
            mil = float(input('Please enter miles (num): '))
            return mil
        except ValueError:
            print('Invalid Input!')
        
def getgascost():
    while(True):
        try:
            gas = float(input('Please enter cost of gas (num): '))
            return gas
        except ValueError:
            print('Invalid Input!')
            
def geteff():
    while(True):
        try:
            eff = float(input('Please enter mpg (num): '))
            return eff
        except ValueError:
            print('Invalid Input!')
            
def est():
    while(True):
        try:
            estim = float(input('Please enter estimated resale value (num): '))
            return estim
        except ValueError:
            print('Invalid Input!')

def total():
    totalcost = getcarcost() + (((getmiles()/geteff())*getgascost())*float(input('How many years? ')))
    print('Total Cost of owning the car:         %10.2f' % totalcost+' dollars')            

def main():
    total()
    
main()