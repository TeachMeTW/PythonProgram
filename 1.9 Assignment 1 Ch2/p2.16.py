
print('\nWelcome to P2.16 Input to spaced sequence')


def main():
    while(True):
        try:
            # get user input of a 5 digit number
            inp = (input('Enter a 5 digit number: '))
            # check if it is 5 digits (length)
            if (len(inp) == 5 and int(inp)):
                # loop through the input and space it out
                for x in inp: print(x, end=' ')
                return
            else:
            # if not 5 digit, error 
                print('Not a 5 digit number!')
        except ValueError:
            print('Invalid Input!')
    
main()