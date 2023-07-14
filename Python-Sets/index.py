#Sets are used to store multiple items in a single variable.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.

#Duplicates Not Allowed
#Example
#Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#Get the Length of a Set
print(len(thisset))

#Set Items - Data Types
#Example
#String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#Example
#What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))

#Example
#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry"))
print(thisset)

# Note: the set list is unordered, so the result will display the items in a random order.

#Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.
