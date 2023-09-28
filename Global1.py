l = 10  #Global Variable
def function1(n):
    l = 5   #Local Variable
    m = 8   #Local Variable
    print(l, m)
    print(n, "I have printed")

function1("This is me")
# print(l)