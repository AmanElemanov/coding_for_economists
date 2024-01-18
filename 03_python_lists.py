#In this file we will look at lists, dictionary, set, tuples, range

#List 
myList = [1, 2, 3, 4, 5]
print(myList)
print(type(myList))

#Grab first object of the list
print(myList[0])

#Grab last object of the list
print(myList[-1])

#Slicing
print(myList[1:4])

#How many objects are in the list
print(f'Our list object myList has {len(myList)} elements')

#Mixed list
mixedList = [1, 'two', 3.0, [4, 'four'], 5]
print(mixedList)

#We can also add or remove objects from the list
#Adding
mixedList.append(6)
print(mixedList)
#Removing
mixedList.pop() #Without argument removes last object from the list
print(mixedList)

#How many times does the integer 1 appear?
print(mixedList.count(1))

#Reverse a list
mixedList.reverse()
print(mixedList)