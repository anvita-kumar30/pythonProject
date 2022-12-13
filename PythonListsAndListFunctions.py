students = ["sam", "pam", "cam"]
print(students)
print(type(students))
print(students[0])
print(students[1])
print(students[2])

"""
Lists in Python (square brackets)

[]                             list with no member, empty list
[1, 2, 3]                      list of integers 
[1, 2.5, 3.7, 9]               list of numbers (integers and floating point)
['a', 'b', 'c']                list of characters
['a', 1, 'b', 3.5, 'zero']     list of mixed value types
['One', 'Two', 'Three']        list of strings 
"""

#List Slicing
grocery = ["deodrant", "lipstick", "sugar", "beans", "onions"]
print(grocery)
numbers = [2, 7, 9, 11, 3]
print(numbers[0:5])
print(numbers[:5])
print(numbers[:])
print(numbers[1:])
print(numbers[1:4])
print(numbers[::])
print(numbers[::1])
print(numbers[::2])
print(numbers[::3])
print(numbers[1:5:2])
print(numbers[::-2])
print(numbers[1:5:-2]) #do not use numbers less than -1 here as it gives an empty list

#lists are mutable(can be modified)
#List Functions
print(len(numbers))
print(max(numbers))
print(min(numbers))
numbers.append(7)
numbers.append(7)
print(numbers)
numbers.insert(1, 67)
print(numbers)
numbers.remove(9)
print(numbers)
numbers.pop()
print(numbers)
numbers.sort()   #changes the og list
print(numbers)   #changes the og list
numbers.reverse()
print(numbers)

#Tuples - immutable ordered sequences of elements (like strings) also a multiple assignment operator (parenthesis)
vector = (4, 5, 9)
print(vector)
print(type(vector))
tp = (1,) #for single element add a comma
print(tp)

#Traditional method to swap elements
a = 1
b = 8
temp = a
a = b
b = temp
print(a, b)
#Method in python
c = 2
d = 3
c, d = d, c
print(c, d)

#Method of tuple unpacking
location = 108.77, 92.55
latitude, longitude = location  #assigning it to a variable
print("The coordinates are {}x{}".format(latitude, longitude))

"""
OUTPUT:-
['sam', 'pam', 'cam']
<class 'list'>
sam
pam
cam
['deodrant', 'lipstick', 'sugar', 'beans', 'onions']
[2, 7, 9, 11, 3]
[2, 7, 9, 11, 3]
[2, 7, 9, 11, 3]
[7, 9, 11, 3]
[7, 9, 11]
[2, 7, 9, 11, 3]
[2, 7, 9, 11, 3]
[2, 9, 3]
[2, 11]
[7, 11]
[3, 9, 2]
[]
5
11
2
[2, 7, 9, 11, 3, 7, 7]
[2, 67, 7, 9, 11, 3, 7, 7]
[2, 67, 7, 11, 3, 7, 7]
[2, 67, 7, 11, 3, 7]
[2, 3, 7, 7, 11, 67]
[67, 11, 7, 7, 3, 2]
(4, 5, 9)
<class 'tuple'>
(1,)
8 1
3 2

Process finished with exit code 0
"""

