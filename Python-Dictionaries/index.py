# Example
# Create and print a dictionary:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Access Dictionary Items
x = thisdict["model"]
print(thisdict)

#Change Dictionary Items
thisdict["year"] = 2018
print(thisdict)

#Add Dictionary Items
thisdict["color"] = "red"
print(thisdict)

#Remove Dictionary Items
thisdict.pop("model")
print(thisdict)

#Loop Dictionaries
for x in thisdict:
  print(x)

#Copy Dictionaries
mydict = thisdict.copy()
print(mydict)

#Nested Dictionaries
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

print(myfamily)

#Dictionary Methods
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#clear() Method
car.clear()
print(car)

#copy() Method
x = car.copy()
print(x)

#fromkeys() Method
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#get() Method
x = car.get("model")
print(x)

#items() Method
x = car.items()
print(x)

#keys() Method
x = car.keys()
print(x)

#pop() Method
car.pop("model")
print(car)

#popitem() Method
car.popitem()
print(car)

#setdefault() Method
x = car.setdefault("model", "Bronco")
print(x)

#update() Method
car.update({"color": "White"})
print(car)

#values() Method
x = car.values()
print(x)
