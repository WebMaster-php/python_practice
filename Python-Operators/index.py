#Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

#Python Arithmetic Operators
x = 5
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y) #same as 5*5*5
print(x // y)#the floor division // rounds the result down to the nearest whole number

# Assignment operators
x = 5
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x%=3
print(x)
x//=3
print(x)
x **= 3
print(x)
x &= 3
print(x)
x |= 3
print(x)
x ^= 3
print(x)
x >>= 3
print(x)
x <<= 3
print(x)

# Comparison operators
x = 5
y = 3
print(x == y) # returns False because 5 is not equal to 3
print(x != y) # returns True because 5 is not equal to 3
print(x > y) # returns True because 5 is greater than 3
print(x < y) # returns False because 5 is not less than 3
print(x >= y) # returns True because five is greater, or equal, to 3
print(x <= y) # returns False because 5 is neither less than or equal to 3


# Logical operators
x = 5
print(x > 3 and x < 10) # returns True because 5 is greater than 3 AND 5 is less than 10
print(x > 3 or x < 4) # returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
print(not(x > 3 and x < 10)) # returns False because not is used to reverse the result

# Identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)# returns True because z is the same object as x
print(x is y)# returns False because x is not the same object as y, even if they have the same content
print(x == y)# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not z)# returns False because z is the same object as x
print(x is not y)# returns True because x is not the same object as y, even if they have the same content
print(x != y)# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# Membership operators
x = ["apple", "banana"]

print("banana" in x) # returns True because a sequence with the value "banana" is in the list
print("pineapple" not in x)# returns True because a sequence with the value "pineapple" is not in the list


