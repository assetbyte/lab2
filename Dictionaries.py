thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
anotherdict = dict(name = "John", age = 36 , country = "Norway")
print(anotherdict)
a = anotherdict.get("age")
print(a)
b = thisdict.keys()
print(b)
thisdict["something"] = "sth"
print(b)
print(thisdict.values())
c = thisdict.values()
thisdict["year"] = 2040
print(c)
print(thisdict.items())  #as tuple in a list
d = thisdict.items()
thisdict["brand"] = "BMW"
print(d)
thisdict.update({"year": 2050})
thisdict.update({"key":"some_key"})
print(thisdict)
thisdict.pop("model")
print(thisdict)
thisdict.popitem() #removes last element
print(thisdict)
del thisdict["brand"]
print(thisdict)
thisdict.clear()
print(thisdict)