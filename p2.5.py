
print('\nWelcome to P2.4/2.5 two integer evaluator')
print('\nPlease selected 2 integer values')
firstvalue = int(input('Enter first integer: '))
secondvalue = int(input('Enter second integer: ')) 
print()
def sum():
    print('Sum:        %10d' % (firstvalue+secondvalue))
    
def diff():
    print('Difference: %10d' % (firstvalue-secondvalue))
    
def prod():
    print('Product:    %10d' % (firstvalue*secondvalue))

def avg():
    print('Average:       %10.2f' % ((firstvalue+secondvalue)/2))

def dist():
    print('Distance:   %10d' % abs(firstvalue-secondvalue))

def big():
    print('Maximum:    %10d' % max(firstvalue,secondvalue))
    
def small():
    print('Minimum:    %10d' % min(firstvalue,secondvalue))
    
def runall():
    sum()
    diff()
    prod()
    avg()
    dist()
    big()
    small()
    
def switch(val):
    match val:
        case 'sum':
            return sum()
        case 'difference':
            return diff()
        case 'product':
            return prod()
        case 'average':
            return avg()
        case 'distance':
            return dist()
        case 'maximum':
            return big()
        case 'minimum':
            return small()
        case 'all':
            return runall()
        case _:
            print('Invalid input, please try again')
            choice = input('What would you like? \nEnter SUM, DIFFERENCE, PRODUCT, AVERAGE, DISTANCE, MAXIUMUM, MINIMUM, or ALL: ').lower()
            switch(choice)

def main():
    choice = input('What would you like? \nEnter SUM, DIFFERENCE, PRODUCT, AVERAGE, DISTANCE, MAXIUMUM, MINIMUM, or ALL: ').lower()
    switch(choice)
    
main()