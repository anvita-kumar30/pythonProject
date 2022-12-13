#Exercise 2 - Faulty Calculator
#Design a calculator which will correctly solve all the problems except the following ones:-
#45*3 = 555, 56+9 = 77, 56/6 = 4
#Your program should take operator and the two numbers as input from the user and then return the result

first = input("Enter the first number: ")
operator = input("Enter operator(+,-,*,/,%): ")
second = input("Enter the second number: ")

first = int(first)
second = int(second)

if operator == "+":
    if first==56 and second==9:
        print("77")
    else:
        print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    if first==45 and second==3:
        print("555")
    else:
        print(first * second)
elif operator == "/":
    if first == 56 and second == 6:
        print("4")
    else:
        print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operator")

"""
OUTPUT:-
Enter the first number: 45
Enter operator(+,-,*,/,%): *
Enter the second number: 3
555

Process finished with exit code 0
"""