# mapping the month to temperature
tempMap = {}

# mapping the input count to a month
monthName = dict({1: 'January',
                 2: 'Feburary',
                 3: 'March',
                 4: 'April',
                 5: 'May',
                 6: 'June',
                 7: 'July',
                 8: 'August',
                 9: 'September',
                 10: 'October',
                 11: 'November',
                 12: 'December'})

def getData():
    count = 1
    # since count starts at 1
    while(count != 13):
        while(True):
            try:
                # input validation float value, must be number
                userIn = float(input('Enter temperature for month ' + monthName[count] + ': '))
                # map current month with the inputted value
                tempMap[monthName[count]] = userIn
                break
            # if input was not a float/number
            except ValueError:
                print('Enter valid temperature')
        # up the count
        count = count+1
    # return the map when done
    return tempMap

# Not really needed since its only 2 lines
def printTemp(tempMap):
    # prints the month with highest temperature
    print('\nHottest month: ' + max(tempMap, key=tempMap.get)+ ' with the highest temperature being ' + str(tempMap[max(tempMap, key=tempMap.get)]) + ' degrees')\
    # bonus; prints the month with lowest temperature
    print('\nCoolest month: ' + min(tempMap, key=tempMap.get)+ ' with the lowest temperature being ' + str(tempMap[min(tempMap, key=tempMap.get)]) + ' degrees')

def main():
    # store the map
    dataMap = getData()
    # pass it to print function
    printTemp(dataMap)
    
main()