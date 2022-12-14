"""
Exercise 4
Pattern Printing
Input = Integer n (You have to take an integer type variable, and the input of the variable will define the length of the triangle.)
Boolean = True or False
When the value of Boolean is 1 i.e. True, the pattern will be printed as shown above.
But if the value of Boolean is 0 or false, then the triangle will be printed upside down.

True n=5
*
**
***
****

False n=5
****
***
**
*
"""

n = int(input("Enter the number of rows: "))
boolean = int(input("Enter 1 or 0(true or false): "))
while(boolean==1):
    i = 1
    while(i<=n):
        print(i * "*")
        i = i + 1
    break
while(boolean==0):
    while(n>=0):
        j = 0
        j = j + n
        print(j * "*")
        n = n - 1
    break

"""
OUTPUT 1:-
Enter the number of rows: 5
Enter 1 or 0(true or false): 1
*
**
***
****
*****

Process finished with exit code 0

OUTPUT 2:-
Enter the number of rows: 5
Enter 1 or 0(true or false): 0
*****
****
***
**
*


Process finished with exit code 0
"""
