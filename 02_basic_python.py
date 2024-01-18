#Basic arithmetic operations in Python

#Add teo numbers
print(2 + 4)

#Divide two numbers
print (10/5)

#Careful: division returns a float (2.0 but not 2)
print (type(10/5))

#Exponentiation
print (2 ** 3)

#Assigning variables
x=5
y=x**2
print(y)

#For string variables
a="Hello " 

#Arithmetic operations
#Multiplication
print(a*5)

#Concatenation
b="I'm good, thank you"
print(a + "" + b)

#Subtraction
#print (a-b)

#Indexing
#First element
print(a[0])
#Last element
print(a[-1])

#Slicing
print(a[0:5])

#How many characters does oir string has?
print(f'Our string a has {len(a)} characters')
print('Our string a has {} characters'.format(len(a)))

#Logical statements
print (2==2) #True=1
print(2==3) #False=0
print(True==1)
print(True+True+True)

#Check equivalence of variables
print(a==b)

#Multiple logical statements
print(2==2 and 3==3) #True
print(2==2 and 3==4) #False
print(2==2 or 3==4) #True
print(2==3 or 3==4) #False