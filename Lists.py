mylist = ["apple" , "banana" , "cherry"] #Lists is changable, duplicates are allowed
print(mylist)
print(len(mylist))


list1 = ["abc", 34, True, 40, "male"] #Different data types
print(type(list1))


thislist = list(("apple", "banana", "cherry" , "orange" , "banana" , "melon" , "mango")) 
print(thislist)
print(thislist[-1]) #cherry
print(thislist[1:3])
print(thislist[:2])
print(thislist[-3:-1]) #apple -> banana


if "apple" in thislist:
    print("Yes, apple is in this list")
    
    
thislist[1] = "blackcurrant"
thislist[1:3] = ["blackcurrant" , " orange"]
print(thislist)


thislist.insert(2, "watermelon") #after blackcurrant watermelon will be included
print(thislist)


thislist.append("fruits")

    