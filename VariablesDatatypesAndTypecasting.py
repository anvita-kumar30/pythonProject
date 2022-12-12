var1 = "hello "  #string
var2 = 4  #integer
var3 = 36.7  #float
var4 = "Anvita"
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
