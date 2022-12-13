var1 = 6
var2 = 56

print("Enter var3:")
var3 = int(input())

if var3>var2:
    print("Greater")
if var3==var2:           #use of multiple if statements increases the time for the completion of the program
    print("Equal")
else:
    print("Lesser")

print("Enter age:")
age = int(input())
if age>18:
    print("You are an adult")
    print("You can drive")
elif age==18:
    print("Cannot decide whether you can drive or not as your age is 18 so be present physically")
elif age<18 and age>3:
    print("You are in school")
    print("You cannot drive")
else:
    print("You are a child")
    print("You cannot drive")
print("Thank you")

list1 = [5, 7, 3]
print(5 in list1)
print(15 not in list1)
if 5 in list1:
    print("Yes it is in the list")

"""
OUTPUT:-
Enter var3:
34
Lesser
Enter age:
19
You are an adult
You can drive
Thank you
True
True
Yes it is in the list

Process finished with exit code 0
"""