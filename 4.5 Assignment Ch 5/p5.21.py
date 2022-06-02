# convert number into roman digit
# @param number, char of roman numerals one five ten
# @return character or sequence

# I don't like this method like the book wants
# its... too weird and big
def romanDigit(n, one, five, ten):
    if (n==1): return one
    if (n==2): return one + one
    if (n==3): return one + one + one
    if (n==4): return one + five
    if (n==5): return five
    if (n==6): return five + one
    if (n==7): return five + one + one
    if (n==8): return five + one + one + one
    if (n==9): return one + ten
    if (n==0): return ten
    return ""

# convert number into roman digit
# @param number, char of roman numerals one five ten
# @return character or sequence

# this one just uses a list
# index is the floor division with the modulo
def romanDigit2(n):
    romanThousands = ["", "M", "MM", "MMM",] # whats after M
    romanHundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    romanTens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    romanOnes = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    # Using what the book says
    return (romanThousands[n // 1000] + romanHundreds[n % 1000 // 100] + romanTens[n % 100 // 10] + romanOnes[n % 10])
    
def main():
    while True:
        try:
            n = int(input('Enter number to turn into roman: '))
            roman = romanDigit(((n//100)%10),'C','D','M') + romanDigit(((n//10) % 10),'X','L','C') + romanDigit((n % 10),'I','V','X')
            roman2 = romanDigit2(n)
            print('\nRoman Numerals: ' + roman)
            print('\nRoman Numerals v2: ' + roman2)
            break
        except ValueError:
            print('Enter valid number')

main()

############################
#   EX;
#   input: 2022
#   
#   romanThousands[2022 // 1000] -> romanThousands[2] -> MM
#   romanHundreds[2022 % 1000 // 100] -> romanHundreds[0] -> " "
#   romanTens[2022 % 100 // 10] -> romanTens[2] -> XX
#   romanOnes[2022 % 10] -> romanOnes[2] -> II
#