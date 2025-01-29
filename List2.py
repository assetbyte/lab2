thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #tropical and thislist will be combined as a one list
print(thislist) #extend works with tuples,list even with dictionaries
mylist = ["orange" , "papaya"]
mytuple = ["kiwi" , "pineapple"]
mylist.extend(mytuple)
print(mylist)
thislist.remove("apple") #remove only one element which will occurant first
print(thislist)
thislist.pop(1) #if there is no index in POP method last element will be deleted
print(thislist)
del thislist[0] 
print(thislist)
thislist.clear() #clear full list
for x in thislist: # 1st method
    print(x)
for i in range(len(thislist)): # 2nd method
    print(thislist[i])
i = 0 
while i < len(thislist): # 3th method
    print(thislist[i])
    i +=1
[print(x) for x in thislist] # 4th method. Same as 1st one
newlist = [x for x in mylist if "p" in x]
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
anotherlist = [x if x != "banana" else "orange" for x in fruits]
print(anotherlist)
