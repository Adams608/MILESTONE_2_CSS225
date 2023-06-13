#ADAM GBOYEGA-DIXON
#6/8/2023
#a Python function to multiply all the numbers in a lis
def list_multiply(numbers):
    result = 1
    for x in numbers:
        result = result * x
    return result


numbers = [1, 2, 3, 4, 500]
print(list_multiply(numbers))