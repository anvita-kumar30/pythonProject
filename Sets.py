s = set()
print(type(s))
s_from_list = set([1, 2, 3, 4])
print(s_from_list)
print(type(s_from_list))

marks = {95, 98, 97, 97, 97}
print(marks) #no duplicates

#Functions
s.add(1)
s.add(1)
s.add(2)
s1 = s.union({1, 2, 3})
print(s, s1)
s2 = s.intersection({1, 2, 3})
print(s, s2)
s3 = {4, 6}
print(s.isdisjoint(s3))
s.remove(2)
print(s)

print(len(s))
print(min(s))
print(max(s))

"""
OUTPUT:-
<class 'set'>
{1, 2, 3, 4}
<class 'set'>
{97, 98, 95}
{1, 2} {1, 2, 3}
{1, 2} {1, 2}
True
{1}
1
1
1

Process finished with exit code 0
"""

