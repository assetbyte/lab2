print(10 == 9) #False
print(10 == 10) #True
print(10 < 9) #False

a = 200 
b = 33 
if b > a: 
    print("b is greater that a")
else:
    print("b is not greater that a")
    
print(bool("Hello")) #True
print(bool(15)) #False

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"])) 

""" Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

"""
c = 200 
print(isinstance(c,int)) #Trur
