var1 = "hello "  #string
var2 = 4  #integer
var3 = 36.7  #float
var4 = "Anvita"
a = 3<1  #boolean
print(a)
print(var1)
print(type(var1))
print(type(var2))
print(type(var3))
print(var1 + var4)

var5 = "66"
var6 = "40"
print(int(var5) + int(var6)) #typecasting
"""
str()
int()
float()
boolean()
"""

print(10*"Anvita\n")
print(100 * str(int(var5) + int(var6)))
print(100 * int(var5) + int(var6))

#Taking input from user
print("Enter your number")
inp = input()
print("You entered", inp)
print("Adding 10 to the result we get", int(inp)+10)

#To add two numbers taking input from the user
print("Enter first number")
inp1 = input()
print("Enter second number")
inp2 = input()
print("The addition of the two numbers is", int(inp1)+int(inp2))

"""
OUTPUT:-
False
hello 
<class 'str'>
<class 'int'>
<class 'float'>
hello Anvita
106
Anvita
Anvita
Anvita
Anvita
Anvita
Anvita
Anvita
Anvita
Anvita
Anvita

106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106106
6640
Enter your number
20
You entered 20
Adding 10 to the result we get 30
Enter first number
3
Enter second number
4
The addition of the two numbers is 7

Process finished with exit code 0
"""
