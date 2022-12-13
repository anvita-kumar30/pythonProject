# a = 9
# b = 8
# c = sum((a,b))  #built-in function
# print(c)

#user defined
def function1(a, b):
    print("Hello you are in function 1:", a+b)
function1(5, 7)

def function2(a, b):
    """This is a function which will calculate average of two numbers
    this function does not work for three numbers"""
    average = (a+b)/2
    # print(average)
    return average

v = function2(5, 7)
print(v)
print(function2.__doc__)

"""
OUTPUT:-
Hello you are in function 1: 12
6.0
This is a function which will calculate average of two numbers
    this function does not work for three numbers

Process finished with exit code 0
"""