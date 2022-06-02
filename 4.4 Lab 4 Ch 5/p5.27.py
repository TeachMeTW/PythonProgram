
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
    
    # indexes
    stringIndex = 0
    tupleIndex = 0
    
    # resulting number
    result = 0
    
    # Loop through user input characters
    while stringIndex < len(userIn):
        
        # Loop through tuple and check if the tuple word starts at the current index
        # startswith returns true if string starts with specified value in this case the character at a given index
        while tupleIndex < len(numDict) and not userIn.startswith(numDict[tupleIndex][0], stringIndex):
            # up the index count if not at end of dict and it doesn't start at the given index
            # print('Current char ' + str(numDict[tupleIndex][0]))
            # print('\n')
            # print('Current string ind ' + str(stringIndex))
            # print('\nTuple Index: ' + str(tupleIndex))
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



#######################################
#   Ex: MMXXII -> 2022 expected
#   1st: Current character matching -> M | Found yes -> 1000
#   2nd: Current character matching -> M | Found yes -> 1000
#   3rd: Curent char match -> CM | index string 2 | tuple index 0 | found no
#   4th: Current char match -> D | index string 2 | tuple index 1 | found no
#   5th: Current char match -> CD | index string 2 | tuple index 2 | found no
#   6th: Current char match -> C | index string 2 | tuple index 3 | found no
#   7th: Current char match -> XC | index string 2| tuple index 4 | found no
#   8th: Current char match -> L | index string 2 | tuple index 5 | found no
#   9th: Current char match -> XL | index string 2 | tuple index 6 | found no
#   10th: Current char match -> X | index string 2 | tuple index  7 | found yes -> 10
#   11th: Current char match -> X | index string 3 | tuple index  7 | found yes -> 10
#   12th: Current char match -> IX | index string 4 | tuple index  8 | found no
#   13th: Current char match -> V | index string 4 | tuple index  9 | found no
#   14th: Current char match -> IV | index string 4 | tuple index  10 | found no
#   15th: Current char match -> I | index string 4 | tuple index  11 | found yes -> 1
#   16th: Current char match -> I | index string 5 | tuple index  11 | found yes -> 1
#
#                           DONE
#   Roman: MMXXII
#   Decimal: 2022