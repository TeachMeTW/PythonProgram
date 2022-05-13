

print('\nWelcome to P2.7 radius into area, circumpherence, volume, and surface area')

# constant pi
pi = 3.14159265359


while(True):
    try:
        # What are the inputs?
        # Get user input radius, cast it into a float just in case decimals are used
        radius = float(input('Please enter radius of a circle/sphere (m): '))
        
        # if a valid input, break from loop
        break
    
    # if invalid, catch error and print invalid
    except ValueError:
        print('Invalid Input!')

# What are the desired outputs?

def area():
    # print string area, add space, area is pi radius squared
    print('Area:         %10.2f' % (pi*(radius**2))+' meters')
    
def circum():
    # print string circumference, add space, circumference is 2pi*radius
    print('Circumference:%10.2f' % (2*pi*radius)+' meters')
    
def vol():
    # print string volume, add space, volume is 4/3pi*radius cubed
    print('Volume:       %10.2f' % ((4/3)*pi*(radius**3))+' meters')
    
def sarea():
    # print string volume, add space, surface area is 4pi*radius squared
    print('Surface Area: %10.2f' % (4*pi*(radius**2))+' meters')

# run all functions    
def runall():
    area()
    circum()
    vol()
    sarea()

# Switch just in case the user wants a specific output    
def switch(val):
    match val:
        case 'circumference':
            return circum()
        case 'volume':
            return vol()
        case 'surface area':
            return sarea()
        case 'area':
            return area()
        case 'all':
            return runall()
        case _:
            print('Invalid input, please try again')
            choice = input('What would you like? \nEnter AREA, CIRCUMFERENCE, VOLUME, SURFACE AREA, or ALL: ').lower()
            switch(choice)

def main():
    choice = input('What would you like? \nEnter AREA, CIRCUMFERENCE, VOLUME, SURFACE AREA, or ALL: ').lower()
    switch(choice)
    
main()