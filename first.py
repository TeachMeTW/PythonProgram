## Gets smallest of 3 nums
# @param 3 floats
# @return 1 float min
def smallest(x,y,z):
    nList = [x,y,z]
    return min(nList)


## Gets avg of 3 num
# @param 3 floats
# @return 1 float avg

def average(x,y,z):
    return ((x+y+z)/3)
    
def main():
    while True:
        try:
            x = float(input("Enter x value: "))
            y = float(input("Enter y value: "))
            z = float(input("Enter z value: "))
            print('\n')
            print('Smallest: ' + str(smallest(x,y,z)))
            print('Average: '+ '{:.2f}'.format(average(x,y,z)))
            print('\n')
            break
        except ValueError:
            print('Enter valid number')

main()