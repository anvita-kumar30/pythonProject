f = open("Anvi.txt", "rt")  #open("filename" ,"mode")

content = f.read()
print(content)
"""
O/P:-
Tom is a good boy
Cam is the king of this universe
Pam is very smart
"""

#to print line by line
# for line in f:
#     print(line, end="")
"""
O/P:-
Tom is a good boy
Cam is the king of this universe
Pam is very smart
"""

# print(f.readline())
# print(f.readline())
# print(f.readline())
"""
O/P:-
Tom is a good boy

Cam is the king of this universe

Pam is very smart
"""

# print(f.readlines())
"""
O/P:-
['Tom is a good boy\n', 'Cam is the king of this universe\n', 'Pam is very smart']
"""

# content = f.read(30)  #arguments are possible
# print("1.", content)
# content = f.read(3)
# print("2.", content)
"""
O/P:-
1. Tom is a good boy
Cam is the k
2. ing
"""

f.close()  #necessary