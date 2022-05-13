
print('\nWelcome to P2.4/2.5 two integer evaluator')
print('\nPlease select 2 integer values')

# What are the inputs?

# Get first integer and assign it to first value
firstvalue = int(input('Enter first integer: '))

# Get second integer and assign it to second value
secondvalue = int(input('Enter second integer: ')) 
print()

# What are the desired outputs?
def sum():
    # print the string sum, add a space, print first + second
    print('Sum:        %10d' % (firstvalue+secondvalue))
    
def diff():
    # print the string difference, add a space, print first - second
    print('Difference: %10d' % (firstvalue-secondvalue))
    
def prod():
    # print the string product, add a space, multiply first and second
    print('Product:    %10d' % (firstvalue*secondvalue))

def avg():
    # print the string product, add a space, add first and second, divide by two then print
    print('Average:       %10.2f' % ((firstvalue+secondvalue)/2))

def dist():
    # print the string distance, add a space, find the absolute value of the difference
    print('Distance:   %10d' % abs(firstvalue-secondvalue))

def big():
    # print the string maximum,  add a space, compare to find which one is bigger
    print('Maximum:    %10d' % max(firstvalue,secondvalue))
    
def small():
    # print the string maximum, add a space, compare to find which one is smaller
    print('Minimum:    %10d' % min(firstvalue,secondvalue))
    
# Running all functions
def runall():
    sum()
    diff()
    prod()
    avg()
    dist()
    big()
    small()
    
# Switch just in case the user wants a specific output
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