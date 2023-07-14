cars = ["Ford", "Volvo", "BMW"]
print(cars)

#Access the Elements of an Array
x = cars[0]
print(x)

#Modify the value of the first array item:
cars[0] = "Toyota"
print(cars)

#The Length of an Array
x = len(cars)
print(x)

#Looping Array Elements
for x in cars:
  print(x)
  
#Array Methods
fruits = ['apple', 'banana', 'cherry']

#append() Method
fruits.append("orange")

#clear() Method
fruits.clear()

#copy() Method
fruits.copy()

#count() Method
x = fruits.count("cherry")
print(x)
#extend() Method
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)

#index() Method

fruits.index("cherry")

#insert() Method
fruits.insert(1, "orange")

#pop() Method
fruits.pop(1)

#remove() Method
fruits.remove("orange")

#reverse() Method
fruits.reverse()

#sort() Method
fruits.sort()
