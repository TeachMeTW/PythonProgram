# I know basic, but I was running out of time

# set a bool first to true
first = True
# get user in
userIn = input('Enter num sequence: ')
# start 
x = 0

# while another value read
while x < len(userIn):
    # if first is true, and not blank
    if (first == True and userIn[x] != ' '):
        # set min to val
        minim=userIn[x]
        # set first false
        first=False
    # if value less than min and not blank
    elif (userIn[x] < minim and userIn[x] != ' '):
        # set min to val
        minim = userIn[x]
    # increment
    else:
        x=x+1

print(minim)

###################################################################################################
#           Design Document
#   1: in the loop check if first is true or not, then set min to user input else increment
#   2: Condition is theres a valid input aka not blank
#   3: This is a for loop that is event controlled by a condition
#   4: variables set up was first,  user in, then x
#   5: prints minimum
#
#
#####################################################################################################=