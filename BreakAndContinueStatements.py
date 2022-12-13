i = 0
# while(i<20):
#     print(i, end=" ")
#     if(i==15):
#         break  #stops
#     i = i + 1

# while(i<20):
#     i = i + 1
#     if(i==15):
#         continue  #skips
#     print(i, end=" ")

# while(True):
#     if i+1<5:
#         i=i+1
#         continue
#     print(i+1, end=" ")
#     if(i==44):
#         break  #stops
#     i = i + 1

#Take input from user until the number is not greater than 100
while(1):
    num = input("Enter a number: ")
    if int(num)<100:
        print(num)
        print("Try again!\n")
    else:
        print("Congrats you have entered a number greater than 100")
        break

"""
OUTPUT:-
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 17 18 19 20 
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45
Enter a number: 12
12
Try again!

Enter a number: 34
34
Try again!

Enter a number: 23
23
Try again!

Enter a number: 122
Congrats you have entered a number greater than 100

Process finished with exit code 0
"""