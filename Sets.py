thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


set1 = {"apple", "banana", "cherry", True, 1, 2}
print(set1)


set2 = {"apple", "banana", "cherry", False, True, 0}
print(set2)


set3 = set(("apple" , "banana" , "cherry"))
print(type(set3))


set4 = {"apple", "banana", "cherry", "mango"}
for x in set4:
  print(x)
print("banana" not in set4)


set5 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
set5.update(tropical)
print(set5)


set6 = {"apple", "banana", "cherry"}
mylist = ("kiwi", "orange","banana")
set6.update(mylist)
print(set6)
