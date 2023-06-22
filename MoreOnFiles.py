f = open("anvi.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(10)
print(f.readline())
# print(f.tell())
print(f.readline())
# print(f.tell())
f.close()

"""
OUTPUT:-
Hello World

d

more line
"""