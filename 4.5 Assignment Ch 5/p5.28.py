
# Find financial aid based on parameters
# @param salary, child count
# @return finaid received
def finAid(salary, childCount):
    if (salary <= 20000) : return childCount*2000
    elif (20000 < salary < 30000 and childCount >= 2):
        return childCount*1500
    elif (30000 < salary < 40000 and childCount >=3):
        return childCount*1000
    else:
        print('You dont qualify for financial aid')
        return 0

def main():
    while True:
        try:
            userSalary = float(input('Enter salary: $'))
            userChildCount = int(input('Enter child count: '))
            # only qualify with children
            if userChildCount <= 0:
                print('Must have children to receive aid')
                # make it give an error which will be caught
                raise ValueError
            print('\nFinancial Aid Recieved: $' + str(finAid(userSalary, userChildCount)))
            break
        except ValueError:
            print('Enter valid input')
    
main()

##########################
#   EX; user in = 12000, child = 5
#   12000 < 20000
#   
#   2000 since lowest bracket
#   return 2000*child
#   = 10,000
#
#
#
