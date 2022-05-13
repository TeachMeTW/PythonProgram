
print('\nWelcome to P2.16 Input to spaced sequence')

def main():
    while(True):
        try:
            inp = input('Enter a 5 digit number: ')
            if (len(inp) == 5):
                for x in inp: print(x, end=' ')
                return
            else:
                print('Not a digit number!')
        except ValueError:
            print('Invalid Input!')
    
main()