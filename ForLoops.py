list1 = ["Larry", "Carry", "Marie"]
print(list1[0], list1[1], list1[2])  #avoid
for item in list1:
    print(item)

list2 = [["Larry", 1], ["Carry", 2], ["Marie", 6]]
for item in list2:
    print(item)
for item, lollipop in list2:
    print(item, lollipop)

dict1 = dict(list2)
print(dict1)
for item in dict1:
    print(item)
for item, lollipop in dict1.items():
    print(item, lollipop)

#Check if in a list there are numbers and only print the numbers that are greater than or equal to 6
items = [int, float, "Anvita", 5, 3, 3, 22, 21, 64, 23, 233, 23, 6]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)

"""
OUTPUT:-
Larry Carry Marie
Larry
Carry
Marie
['Larry', 1]
['Carry', 2]
['Marie', 6]
Larry 1
Carry 2
Marie 6
{'Larry': 1, 'Carry': 2, 'Marie': 6}
Larry
Carry
Marie
Larry 1
Carry 2
Marie 6
22
21
64
23
233
23
6

Process finished with exit code 0
"""