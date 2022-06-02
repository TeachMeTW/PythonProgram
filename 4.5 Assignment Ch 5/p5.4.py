
# Finds middle of string
# @param: string word
# @return: middle of the string that is one or two in length

def middle(string):
    
    # Debug: print('\nCurrent check: ' + string)
    # checks if length is less than or equal to 2 (two if even, one if odd)
    if len(string) <= 2:
        return string
    # recursively checks by removing first and last
    else :
        return middle(string[1:-1])
    
def main():
    userIn = str(input('Input string to find middle: '))
    print('Middle: '+ middle(userIn))
    
main()


##########
# EX:
# Input: Despacito                      AmongUs
# 
#
#   first iter: despacito               AmongUs
#   second iter: espacit                mongU
#   third iter: spaci                   ong
#   fourth iter: pac                    n
#   fifth iter: a
#   Middle found: a