# ADAM GBOYEGA-DIXON
#6/8/2023
#a Python function that takes a list of numbers and returns a new list with unique elements of the first list
def numbers(my_list):
    new_list = [ ]
    for x in my_list:
        if x not in new_list:
            new_list.append(x)
        elif x in new_list:
            continue
    return new_list
print(numbers([1,2,2,3,4,4,4]))
numbers([1,2,3])