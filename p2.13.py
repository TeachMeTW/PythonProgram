print('\nWelcome to P2.13 string to int')

while (True):
    val = str(input('\nEnter an integer between 10,000 and 99,000 with comma: '))
    if ((10000 < int(val.replace(',','')) < 99000) and (',' in val[2])) :
        break
    print('Invalid Input')

print(val.replace(',',''))
