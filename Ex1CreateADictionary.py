#Create a dictionary and take input from the user and return the meaning of the word from the dictionary

print("Welcome to My Dictionary\n")
print("Following are the words in my dictionary:-")
print("House\nChair\nTable\nPen")
print()
a = input("Enter the word to get the meaning of it: ")
word = a.capitalize()
d1 = {"House" : "The place where any person lives",
      "Chair" : "An object where a person sits",
      "Table" : "A solid object where anything can be placed",
      "Pen" : "It is a thing which can be used to write something"}
print()
print(d1[word])
print(word, "means", d1[word])

"""
OUTPUT:-
Welcome to My Dictionary

Following are the words in my dictionary:-
House
Chair
Table
Pen

Write the word to get the meaning of it: Table

A solid object where anything can be placed
Table means A solid object where anything can be placed

Process finished with exit code 0
"""