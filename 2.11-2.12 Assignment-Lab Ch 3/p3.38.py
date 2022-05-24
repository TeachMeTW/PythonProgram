

def initData(): 
    while(True):
        try:
            # gets user data
            workerName = str(input('Please enter your name: '))
            workerSalary = float(input('Enter hourly salary: '))
            print('Welcome ' + workerName + '. Your current hourly rate is $' + str(workerSalary) )
            hoursWorked = float(input('Enter hours worked weekly: '))
            # returns gathered data
            return hoursWorked, workerSalary
        # validates input, checks if name is string, salary is num, hours is num
        except ValueError:
            print('Please enter a valid input')
            
def payCalculation(totalHours, workerSalary):
    # if overtime
    if totalHours > 40:
        # gets overtime hours worked
        overtimeHours = totalHours-40
        # pay is overtime * 150% + base pay
        pay = (overtimeHours*(workerSalary*1.50)) + (40*workerSalary)
        print('Your weekly pay is: $' + str(pay) + ' with ' + str(overtimeHours) + ' overtime hours')
    else:
        print('Your weekly pay is: $' + str(totalHours*workerSalary))

def main():
    t, s = initData()
    # pass data into calculation
    payCalculation(t,s)
    

main()
        
