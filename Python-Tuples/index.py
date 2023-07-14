#Tuples are used to store multiple items in a single variable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Access Tuple Items
print(thistuple[1])

#Change Tuple Values
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple)

#Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

#Loop Through a Tuple
for x in thistuple:
  print(x)
  
#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Tuple Methods
#count =>  Returns the number of times a specified value occurs in a tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
#index => Searches the tuple for a specified value and returns the position of where it was found
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
