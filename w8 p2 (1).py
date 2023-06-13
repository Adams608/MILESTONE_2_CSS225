#Adam Gboyega-dixon
#6/6/2023
#A function that takes two inputs from a user and prints whether the sum is greater than 10, less than 10, or equal to 10.
def starter():
    john = int(input("enter a value"))
    gabe = int(input("what is the number"))
    sum =  john + gabe
    print (sum)
    if sum >10:
        print("greater than 10")
    elif sum <10:
        print("it is less than 10")
    else:
        print("it equal to 10")
starter()

