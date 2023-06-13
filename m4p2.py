#Adam Gboyega_dixon
#5/9/2023
#
#def type_postive_number(num):
PI = 3.14
radius = int(input("enter a positive number for the  radius: "))
Area = PI * radius**2
while True:  #the while loop function here to create infinite
    if radius < 0:
        print('enter a positive number for the  radius: "')
        exit() # i use this statement to stop loop statement from continously running
    else:
        print("the area of a cirle is", Area)
        exit()
#type_postive_number(num)
