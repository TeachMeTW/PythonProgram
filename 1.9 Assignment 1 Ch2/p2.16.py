
print('\nWelcome to P2.16 Input to spaced sequence')


def main():
    while(True):
        try:
            # get user input of a 5 digit number
            inp = input('Enter a 5 digit number: ')
            # check if it is 5 digits
            if (len(inp) == 5):
                # loop space
                for x in inp: print(x, end=' ')
                return
            else:
                print('Not a digit number!')
        except ValueError:
            print('Invalid Input!')
    
main()