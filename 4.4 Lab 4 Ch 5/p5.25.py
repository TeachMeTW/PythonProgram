

# Dict to match num to barcode
# doesn't need to be sorted
digitBar = {
    1:':::||',
    2:'::|:|',
    3:'::||:',
    4:':|::|',
    5:':|:|:',
    6:':||::',
    7:'|:::|',
    8:'|::|:',
    9:'|:|::',
    0:'||:::'
}

## Take number, match it to dictionary
# @param is num
# @return is bar code

def printDigit(d):
    print(digitBar[int(d)], end='')

## Take the 5 digit zip code into a bar code
# @ param is 5 digit zip code
# @ return is barcode sequence

def printBarCode(zip):
    # begin
    print('|', end='')
    
    # Cycle through the zip code and match corresponding num
    for x in range(0,5):
        printDigit(zip[x])
        
    # Check digit calculation
    zipTotal = 0
    
    # Add up all digits and sum is multiple of 10
    for y in range(0, len(zip)):
        zipTotal+=int(zip[y])
    # finds remainder and missing num check
    # print(str(zipTotal))
    modulo = 10 - (zipTotal%10)
    # print('Check: ' + str(modulo))
    printDigit(abs(modulo))
    
    # end
    print('|')
    
def main():
    while True:
        try:
            # check if is number
            zip = int(input('Enter 5 digit zip code: '))
            # check if 5 digits
            if len(str(zip))!= 5:
                print('Not a valid zip code')
                raise ValueError
            else:
                printBarCode(str(zip))
                break
        except ValueError:
            print('\nEnter a valid zip code')
    
main()

#############################################
#   EX; Zip is 94510
#
#   1st: 9 -> |:|::
#   2nd: 4 -> :|::|
#   3rd: 5 -> :|:|:
#   4th: 1 -> :::||
#   5th: 0 -> ||:::
#   
#   Check = 10 - 19%10 -> 10 - 9 -> 1
#   Check: -> :::||
#
#   Final Bar -> ||:|:::|::|:|:|::::||||::::::|||
#
#