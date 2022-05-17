# Works on python 3.10 and above!

print('\nWelcome to P2.16 Input to spaced sequence')


def main():
    # A while(True) statement continues until the loop is broken out of via break, return, or other means
    # This means it infinitly loops so BE CAREFUL!
    while(True):
        # a try statement lets me test a block of code to check for errors
        try:
            # get user input of a 5 digit number
            inp = (input('Enter a 5 digit number: '))
            # check if it is 5 digits (length) and check if it can be casted into an int
            if (len(inp) == 5 and int(inp)):
                # loop through the input and space it out
                for x in inp: print(x, end=' ')
                break
            else:
            # if not 5 digit, error 
                print('Not a 5 digit number!')
        # if not convertible to an int, error out and ask for a valid entry (aka numbers only)
        # if invalid, catch error and print invalid
        # So what the except ValueError line does is if I try to case my input into a int and it doesn't work
        # aka int(21a4f) this clearly cannot become an int
        # Even though this is 5 DIGITS its still NOT VALID
        # and tells the user to actually put a number that works then retry
        except ValueError:
            print('Invalid Input!')
    
main()