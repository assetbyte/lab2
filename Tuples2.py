a = ("apple" , "banana" , "cherry")
green, yellow, red = a;
print(green, yellow, red)
b = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = b
print(green, red)
print(*tropic) #convert to the list
for x in b:
    print (x)
for i in range(len(b)):
    print(b[i])
i = 0
while i < len(a):
    print(a[i])
    i+=1
tuple1 = ("a" , "b" , "c")
tuple2 = (1, 2, 3)
print(tuple1 + tuple2)
