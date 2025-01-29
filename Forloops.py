adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
for x in range(2, 30, 3):
  print(x)