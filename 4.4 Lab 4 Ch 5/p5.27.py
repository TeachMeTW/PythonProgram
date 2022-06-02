
# this isnt really a dict, more like a tuple. Did this in order to sort the order
# Dict is unsorted
numDict = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
]

## Turns roman to int
# @param nothing, user input is taken inside function
# no return void funct prints out the value


def romanToInt():
    # get user input, change to upper just in case
    userIn = str(input("\nEnter roman numerals: ")).upper()
    
    stringIndex = 0
    tupleIndex = 0
    result = 0
    # Loop through user input characters
    while stringIndex < len(userIn):
        # Loop through tuple and check if the tuple word starts at the current index
        while tupleIndex < len(numDict) and not userIn.startswith(numDict[tupleIndex][0], stringIndex):
            tupleIndex += 1
        # if tuple is not at end
        if tupleIndex < len(numDict):
            # add current index value to final
            result += numDict[tupleIndex][1]
            # up the index value by checking the length of the roman character
            stringIndex += len(numDict[tupleIndex][0])
        # if tuple is at end
        else:
            # I thought of doing recursive down here but it looped out
            # raised an error instead to be caught by main
            raise ValueError('Not a valid roman numeral')
    print('\n')
    print('Roman: ' + str(userIn) + ' | Decimal: ' + str(result))
    print('\n')

## main function

def main():
    while True:
        try:
            romanToInt()
            break
        # catch the error from above
        except ValueError:
            print('Enter a valid roman numeral')
    
main()