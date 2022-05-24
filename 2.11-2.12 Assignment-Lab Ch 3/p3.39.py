
from pyrsistent import v

# const pin, changable
PIN = 1234

def checker():
    # given amount of tries, can be changed
    tries = 3
    # continues if limit not reached
    while(tries != 0):
        try:
            userin = int(input('Enter 4 digit pin code: '))
            # checks pin match
            if userin == 1234:
                print('Your PIN number is correct, enjoy your billion dollars')
                exit()
            # checks length 
            elif len(str(userin)) > 4 or len(str(userin)) < 4:
                print('Please enter a 4 digit code nothing more or less')
                # Not sure if it should cost them a try for this input validation
                
                # tries = tries - 1
            # if incorrect
            else:
                print('Your PIN is incorrect, please input the correct PIN')
                tries = tries-1
                print('Tries remaining: ' + str(tries))
        # if something other than num inputted
        except ValueError:
            print('Please enter a 4 digit pin')
    print('You have inputted the incorrect pin too many times, your bank account is locked')
    exit()


def main():
    checker()
    
main()