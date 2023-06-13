#Adam Gboyega-dixon
#4/27/2023
#Predicting the return day
weekDays = ["sunday", "monday", "tuesday", "wednessday", "thursday", "friday", "saturday"]
Num_days = 7
#my_List = list(range(6))
Starting_Day = int(input("what is the starting day number(0-6)?", ))
Stay_length = int(input(" what is the lenghth of the stay", ))
return_Home = (Starting_Day + Stay_length) % 7
#for i in range(len(weekDays)):
    #if return_Home > 6:
print('you should be returning on the', return_Home,'th day of the weekdays')
