
# this isnt really a dict, more like a tuple. Did this in order to sort the order
# Dict is unsorted
# This is to match num to roman
numDict = [(1000, "M"),
           (900, "CM"),
           (500, "D"), 
           (400, "CD"), 
           (100, "C"),
            (90, "XC"),
            (50, "L"), 
            (40, "XL"), 
            (10, "X"), 
            (9, "IX"), 
            (5, "V"),
            (4, "IV"), 
            (1, "I")
            ]

## Converts number to roman numerals
# @param n (number)
# @return string of roman numerals
def romanDigit(n):
    # empty list of digits
    digit = []
    # cycle through the tuple
    # x is num y is char
    for x, y in numDict:
        # if empty
        if n == 0:
            break
        # divmod gets quotient and remainder
        # aka n / x and n % x tuple
        current, n = divmod(n,x)
        # split quotient and remainder
        
        # Debug
        # print('\n')
        # print('n '+ str(n))
        # print('curr '+ str(current))

        # join number/char that is present
        digit.append(y * current)
    return "".join(digit)

def main():
    while True:
        try:
            userIn = int(input('Enter a number to convert into roman: '))
            print('\n' + romanDigit(userIn))
            break
        except ValueError:
            print('Enter valid int')
    
main()

####################
#   Ex;
#   input = 55
#   
#   M in 55 (55/1000) = 0 and remainder (55%1000) = 55
#   CM in 55 (55/900) = 0 and remainder (55%900) = 55
#   D in 55 (55/500) = 0 and remainder (55%500) = 55
#   CD in 55 (55/400) = 0 and remainder (55%400) = 55
#   C in 55 (55/100) = 0 and remainder (55%100) = 55
#   XC in 55 (55/90) = 0 and remainder (55%90) = 55

#   L in 55 (55/50) = 1 and remainder (55%50) = 5

#   XL in 5 (5/40) = 0 and remainder (5%40) = 5
#   X in 5 (5/10) = 0 and remainder (5%10) = 5
#   IX in 5 (5/9) = 0 and remainder (5%9) = 5

#   V in 5 (5/5) = 1 and remainder (5%5) = 0
#
#   Thus the values are LV
#   The div is the quantity, remainder is the next value