mystr = "Hello"
"""
 0  1  2  3  4 
 H  e  l  l  o
-5 -4 -3 -2 -1    
"""
print(mystr)
print(mystr[4])
print(mystr[0:3]) #first index is included
print(mystr[0:22])
print(mystr[0:])
print(mystr[:5])
print(mystr[:])
print(mystr[::])
print(mystr[::2])   #skips one character between every two letters
print(mystr[0:5:2]) #skips one character between every two letters
print(mystr[-4:-2])
print(mystr[::-1]) #reverses the string
print(mystr[::-2]) #reverse and skip one character
print(len(mystr))

mystr2 = "Anvita k"
print(mystr.isalnum()) #alphanumeric string true
print(mystr2.isalnum()) #alphanumeric string false
print(mystr.isalpha()) #true
print(mystr.endswith("o")) #true
print(mystr.count("l"))  #2
print(mystr.capitalize()) #only the first letter
print(mystr.find("lo"))  #6
print(mystr2.lower()) #applies to the whole string
print(mystr2.upper()) #applies to the whole string
print(mystr.replace("lo", "l")) #Hell