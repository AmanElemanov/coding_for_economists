#Read text files

#Open
file = open('data/raw/european_commission/ted_sample.csv')

print(file.readline())
print(file.readline())

file.close()

#Context manager
with open('data/raw/european_commission/ted_sample.csv') as file:
  for line in line:
    print(line)