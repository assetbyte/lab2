thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
for y in thisdict:
    print(thisdict[y])
for z in thisdict.values():
    print(z)
for a in thisdict.keys():
    print(a)
for b,c in thisdict.items():
    print(b , c)
mydict = thisdict.copy()
print(mydict)
anotherdict = dict(mydict)
print(anotherdict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

