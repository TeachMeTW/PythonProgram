

print('\nWelcome to P2.7 radius into area, circumpherence, volume, and surface area')
pi = 3.14159265359
while(True):
    try:
        radius = float(input('Please enter radius of a circle/sphere (m): '))
        break
    except ValueError:
        print('Invalid Input!')

def area():
    print('Area:         %10.2f' % (pi*(radius**2))+' meters')
    
def circum():
    print('Circumference:%10.2f' % (2*pi*radius)+' meters')
    
def vol():
    print('Volume:       %10.2f' % ((4/3)*pi*(radius**3))+' meters')
    
def sarea():
    print('Surface Area: %10.2f' % (4*pi*(radius**2))+' meters')
    
def runall():
    area()
    circum()
    vol()
    sarea()
    
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