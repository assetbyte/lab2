mytuple = ("apple" , "banana" , "orange")
print(len(mytuple)) #3


thistuple = ("apple" , "banana" , "orange" ) #Tuple
thisstr = ("apple" ) #Not a tuple 


newtuple = tuple(("apple" , "orange" , "banana"))
print(type(newtuple))


#Accessing tuples
print(mytuple[1])
print(mytuple[0:3])


if "apple" in mytuple:
    print("Yes, apple is in a tuple")
    
    
y = list(mytuple)
y[1] = "kiwi"
mytuple = tuple(y)
print(mytuple)


x = list(thistuple)
x.append("watermelon")
thistuple = tuple(x)
print(thistuple)


z = ("mango" , ) #Tuple, not a string
thistuple+=z;
print(thistuple)
#extend, pop, clear, insert, append is not usable for a tuples.
