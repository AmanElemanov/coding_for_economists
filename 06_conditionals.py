#Introduce packages
import random

#Generate a random integer between 20 and 34
random_number = random.randint(20, 34)
print(random_number) #We get a different integre number each time we run the script

#First look at conditional statements
if random_number < 25: #If this condition is met, it is not considering below else statements
  print("The number is less than 25")
elif random_number < 30:
  print("The number is less than 30")
else: #In all other cases compared to previous two if and elif statements
  print("The number is less than 34")

#Nested if statements
a = random.randint(0, 10)
b = random.randint(10, 20)

if a < 9:
  print(f'a is less than 9.')
  if b < 19: #Only gest evalued if a is less than 9
    print(f'b is smaller than 19.')

#Equivalently, we can combine the logical conditions
if a < 9 and b < 19:
  print(f'a is less than 9 and b is less than 19.')