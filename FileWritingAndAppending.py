f = open("Anvi.txt", "w")
f.write("Hello World")  #overwritten
"""
O/P:-
(The text gets overwritten in the file)
"""

# f = open("Anvi.txt", "w")
# a = f.write("Hello World")
# print(a)
"""
O/P:-
11
"""

# f = open("Anvi2.txt", "w")  #file gets added
# f.write("Hello World")
"""
O/P:-
(File gets added with the text in it as mentioned)
"""

# f = open("Anvi2.txt", "a")  #appends
# f.write("Hello World\n")
"""
O/P:-
(Appends the text as many times the program is executed)
"""

# f = open("Anvi2.txt", "a")
# a = f.write("Hello World")
# print(a)
"""
O/P:-
11
(Appends the text as many times the program is executed and gives the count of the no. of characters in the text)
"""

#Handle read and write both
# f = open("Anvi2.txt", "r+")
# print(f.read())
# f.write("Thank you")  #writes in the file by appending the text
"""
O/P:-
Hello WorldHello World
Hello WorldHello World
"""

f.close()