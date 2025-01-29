set1 = {"apple", "banana", "cherry"}
set1.remove("banana")
print(set1)

set2 = {"apple", "banana", "cherry"}
set2.discard("banana")
print(set2)

set3 = {"apple", "banana", "cherry"}

x = set3.pop()
print(x)
print(set3)

set4 = {"apple", "banana", "cherry"}
set4.clear()
print(set4)




set6 = {"apple", "banana", "cherry"}
for x in set6:
  print(x)


set7 = {"a", "b", "c"}
set8 = {1, 2, 3}
set9 = {"John", "Elena"}
set10 = {"apple", "bananas", "cherry"}
myset = set7.union(set8, set9, set10)
print(myset)


set11 = {"a", "b", "c"}
set12 = {1, 2, 3}
set13 = set11 | set12
print(set13)


set14 = {"a", "b", "c"}
set15 = (1, 2, 3)
set16 = set14.union(set15)  #union can be changed with update method
print(set16)


set17 = {"apple", "banana" , "cherry"}
set18 = {"google", "microsoft", "apple"}
set19 = set17 & set18  # & can be changed with intersection
print(set19)


set17.intersection_update(set18)
print(set17)


set20 = {"apple", "banana" , "cherry"}
set21 = {"google", "microsoft", "apple"}
set22 = set20 - set21
print(set22)



set20.difference_update(set21)
print(set20)


set23 = {"apple", "banana", "cherry"}
set24 = {"google", "microsoft", "apple"}
set25 = set23.symmetric_difference(set24) # ^ , update method also included

print(set25)