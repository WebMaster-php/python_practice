#Strings in python are surrounded by either single quotation marks, or double quotation marks.'hello' is the same as "hello".
#You can use double or single quotes:

print("Hello")
print('Hello')

#Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Slicing Strings
b = "Hello, World!"
print(b[2:5])

#Modify Strings

#Upper Case
a = "Hello, World!"
print(a.upper())

#Lower Case
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Python - String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#Python - Format - Strings
#Example
age = 36
txt = "My name is John, I am " + age
print(txt)
#Example
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Python - Escape Characters
#Example
txt = "We are the so-called "Vikings" from the north."
print(txt) 
result: Invalid
#Example
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
result: Valid