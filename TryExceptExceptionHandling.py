print("Enter num 1:")
num1 = input()
print("Enter num 2:")
num2 = input()
try:
    print("The sum of these two numbers is", int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important")

"""
OUTPUT:-
Enter num 1:
3
Enter num 2:
wee
invalid literal for int() with base 10: 'wee'
This line is very important

Process finished with exit code 0
"""