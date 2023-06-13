#Adam Gboyega-dixon
#6/6/2023
#A function that takes a year as a parameter and returns True if the year is a leap year, False if it is otherwise.
def start(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(start(16))