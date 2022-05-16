
def main():
    print('\nWelcome to P2.13 string to int')
    # What are the inputs?
    
    # Get user input and cast into a string
    val = (input('\nEnter a number between 10,000 and 99,999 with comma: '))
    
    # After getting rid of the comma, check if number falls within the range
    # Make sure the comma is in the 2 index
    while (not((10000 < int(val.replace(',','')) < 99999) and (',' in val[2]) and (len(val)) == 6)) :
            #if it is valid then break out of loop and print the value
            # get rid of ,
        print('Invalid Input')
        val = (input('\nEnter a number between 10,000 and 99,999 with comma: '))
        # if not valid print invalid
    
    print(int(val.replace(',','')))
    
main()