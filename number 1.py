def days():
    hour = eval(input("Enter number of hours: "))
    minute = eval(input("Enter number of minutes: "))
    second = eval(input(("Enter number of seconds: ")))
    
    day = get_days(hour,minute,second)
    print("The number of days is: ", format(day,'.4f'))

def get_days(hour,minute,second):
    result = hour / 24 + minute / 1440 + second / 86400
    return result
days()

# Input hour
# Input minute
# Input second
# Calculate result with the formula
# Store get_days def with variable "day"
# print result
