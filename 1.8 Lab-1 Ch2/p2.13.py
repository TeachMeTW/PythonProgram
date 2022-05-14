print('\nWelcome to P2.13 string to int')

while (True):
    # What are the inputs?
    
    # Get user input and cast into a string
    val = str(input('\nEnter a number between 10,000 and 99,000 with comma: '))
    
    # After getting rid of the comma, check if number falls within the range
    # Make sure the comma is in the 2 index
    if ((10000 < int(val.replace(',','')) < 99000) and (',' in val[2])) :
        #if it is valid then break out of loop and print the value
        break
    # if not valid print invalid
    print('Invalid Input')

# get rid of ,
print(int(val.replace(',','')))
