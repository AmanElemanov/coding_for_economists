#Intro to data type set

#Set is a collection of well defined objects

mySet = {1, 2, 3}

#Check type
print(type(mySet))

#Set contains only unique values
mySet = {1, 2, 3, 3} #last 3 is removed
print(mySet)

#Check membership
print(1 in mySet)

print(set("aaaaaabbbbbbbccccc"))

#Define two sets and check out set operations
setA = {1, 2, 3}
listB = [3, 4, 5, 5, 5]
setB=set(listB)
print(setA, setB)

#Set union
unionAB = setA | setB
print(unionAB)

#Intercetion
intersecAB = setA & setB
print(intersecAB)