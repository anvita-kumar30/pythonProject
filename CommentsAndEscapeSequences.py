# This is a single line comment

"""
This is a
multiline
comment
"""

#print statements
print("Hello", end=", ")
print("Printed on the same line")
print("Hello","Printed on the same line") #space between the two lines
print("next line")

#Escape Sequences
print("C:\nope")  #Inserts a new line in the text at the point
print("C:\\nope") #Inserts a backslash character in the text at the point
print("C:\"nope") #Inserts a double quote character in the text at that point
print("C:\'nope") #Inserts a single quote character in the text at that point
print("This is an escape \t sequence") #Inserts a tab in the text at that point
print("Hello \bagain") #Inserts a backspace in the text at that point

"""
OUTPUT:-
Hello, Printed on the same line
Hello Printed on the same line
next line
C:
ope
C:\nope
C:"nope
C:'nope
This is an escape 	 sequence
Helloagain

Process finished with exit code 0
"""
