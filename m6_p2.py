import random

#random_number = random.randrange(1, 51) * 2 + 1
#print(random_number)
number = random.randrange(0, 100)
check = 2
if number % check != 0:
    print(number)
