#Dictionary is a mutable datatype that stores mappings of unique keys to values(curly braces)
#keys are always unique
d1 = {}
print(type(d1))
d2 = {"hydrogen":1, "helium":2, "carbon":6}
print(d2)
print(d2["helium"])
d3 = {"Ram":"Burger", "Shyam":"Fish", "Sita":"Roti"}
print(d3)
print(d3["Ram"])
d4 = {"Ram":"Burger", "Shyam":"Fish", "Sita":"Roti", "Luv":{"B":"maggie", "L":"roti", "D":"Chicken"}}
print(d4["Luv"])
print(d4["Luv"]["B"])
d4["Anvita"] = "Junk Food"
d4["Aurangzeb"] = "Kebab"
print(d4)
del d4["Aurangzeb"]
print(d4)

d5 = d4
del d5["Ram"]  #deletes from d4 also
print(d4)
print(d5)
#for this we use copy function so that the elements in d4 are not modified
d5 = d4.copy()
del d5["Luv"]
print(d4)
print(d5)

print(d4.get("Sita"))
d4.update({"Siya":"Toffee"})
print(d4)

"""
OUTPUT:-
<class 'dict'>
{'hydrogen': 1, 'helium': 2, 'carbon': 6}
2
{'Ram': 'Burger', 'Shyam': 'Fish', 'Sita': 'Roti'}
Burger
{'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}
maggie
{'Ram': 'Burger', 'Shyam': 'Fish', 'Sita': 'Roti', 'Luv': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Anvita': 'Junk Food', 'Aurangzeb': 'Kebab'}
{'Ram': 'Burger', 'Shyam': 'Fish', 'Sita': 'Roti', 'Luv': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Anvita': 'Junk Food'}
{'Shyam': 'Fish', 'Sita': 'Roti', 'Luv': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Anvita': 'Junk Food'}
{'Shyam': 'Fish', 'Sita': 'Roti', 'Luv': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Anvita': 'Junk Food'}
{'Shyam': 'Fish', 'Sita': 'Roti', 'Luv': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Anvita': 'Junk Food'}
{'Shyam': 'Fish', 'Sita': 'Roti', 'Anvita': 'Junk Food'}
Roti
{'Shyam': 'Fish', 'Sita': 'Roti', 'Luv': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Anvita': 'Junk Food', 'Siya': 'Toffee'}

Process finished with exit code 0
"""