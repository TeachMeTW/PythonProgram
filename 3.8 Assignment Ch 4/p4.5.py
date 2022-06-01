# Yes I know this is recycled but thats what coders do

# get list data
def getData():
    # create empty list
    floatList = []
    done = False
    count = 0
    # runs while user is not done inputting integers
    while(not done):
        while(True):
            try:
                # gets input, validates that it needs to be an int
                userIn = float(input('\nPlease enter a floating point value: '))
                # adds ut ti tge kust
                floatList.append(userIn)
                print('Current: ')
                # loops and prints the current input/list
                for x in floatList: print(x, end=' ')
                break
            # if input was not an int
            except ValueError:
                print('\nEnter valid float')
        
        # up the count
        count = count+1
        # gets user choice
        done = choice()
    return floatList

            
def choice():
    decision = str(input('\nContinue? Y/n: '))
    # if yes do nothing
    if (decision.lower() == 'y'):
        done = False
        return done
    # if no, return false ends the data loop
    elif (decision.lower() == 'n'):
        done = True
        return done
    else:
    # if invalid
        print('\nEnter a valid input')
        choice()
        
def operations(list):
    # Max and min of the sequence
    # use python max and min functions
    print('\nMax num: ' + str(max(list)))
    print('Min num: ' + str(min(list)))
    
    # odd and even checker
    even = 0
    odd = 0
    # loop through the list
    for num in list:
        # if divisible by 2 it is even
        if num % 2 == 0:
            even = even + 1
        # if not, it is odd
        else:
            odd = odd + 1

    print('\nEven count: ' + str(even))
    print('Odd count: ' + str(odd))
    
    # cummulative add
    # create empty new list
    cumList = [] 
    # place holder
    toAdd = 0
    # loop through list starting from 0 to list length
    for n in range(0, len(list)):
        # add first value with stored value
       toAdd = toAdd + list[n]
       # add sumed value to the new list
       cumList.append(toAdd)
       
    print('\nCummulatitve addition: ')
    # print values with a space
    for x in cumList: print(x, end=' ')
    
    # duplication
    # sets cannot hold copys so we will use that
    # count everytime something occurs and if it does more than once add it to the set
    dups = set([x for x in list if list.count(x) > 1])
    print('\nDuplicates: ')
    print(dups)
    
    # average
    print('\nAvg: ' + str((sum(list)/len(list))))
    
    # range
    print('Range: ' + str(max(list) - min(list)))
        
        
def main():
    list = getData()
    operations(list)
    
main()


###################################################################################################
#           Design Document
#
#   1: Get user input in the loop, validate the input condition is while not finished inputting and valid
#   1b: get user  choice in the loop condition is while not done
#   1c: cummulatively add the numbers condition is until run out
#   1d: print out the numbers 1 by one condition is until run out
#
#   3: While loop and for loops
#   
#   4: list, done, count, odd, even, toAdd
#
#
#
#####################################################################################################