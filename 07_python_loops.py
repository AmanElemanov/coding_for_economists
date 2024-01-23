#Let's have a look at loop syntax

#for loop operate on "iterables"

#Let's create an iterable object
myList = [1, 2, 'abc']

#Let's iterate over the object
for banana in myList:
  #Loop body needs to be intended once
  if banana == 1:
    print(banana)
  else:
    print("item not equal to 1")

#Looping over a range of values
for i in range(5): #range() generates values on the fly
  print(i)

#Anothe way
range_vals = [0, 1, 2, 3, 4] #Not memory efficient
print("Using a list to display values 0-4")
for i in range_vals:
  print(i)

#Looping over a list of strings
for name in ["Alice", "Bob", "Charlie"]:
  print(name)
  #Iterate for each string (iterate each name by letters)
  for letter in name:
    print(letter)

#Using the enumerate() function to get both index and value
print("Using enumerate()")
for index, name in enumerate(["Alice", "Bob", "Charlie"]):
  print(index, name)

#Anotehr way
print("Using range() and indexig")
myList = ["Alice", "Bob", "Charlie"]
for index in range(len(myList)): #equivalent to range(3)
  print(index, myList[index])

#Use a loop to create a list of capital letters from A to Z
print("Using a loop to create a list of capital letters from A to Z")
#Make an empty list to append to
alphabet = []

for i in range(65, 91):
  print(i, chr(i))
  alphabet.append(chr(i))

print(alphabet)

#while loops
#while loops are used when you don't know how many times you want to loop
i = 0
while i < 10: #Make some restrictions, otnerwise it will loop forever
  print(i)
  #Increment out counter every iteration
  i += 1

#List comprehensions

#Let's have a look at a for loop creating a list of squares from 0 to 10
squares = []
for num in range(0, 11):
  squares.append(num**2)

print(squares)

#Doind the same thing as above in a single line using list comprehension
squares = [num**2 for num in range(0, 11)]
print(squares)

#Using if statements in list comprehension to get squared of even numbers only
even_squares = [num**2 for num in range(0, 11) if num % 2 ==0] #It will square numbers only if the remainder after the divison by 2 is 0, i.e., an even number
print(even_squares)