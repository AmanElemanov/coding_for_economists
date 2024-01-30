#Task 1: Find headers/idx for relevant vars: ISO_COUNTRY_CODE, WIN_COUNTRY_CODE
f = open("data/raw/european_commission/ted_sample.csv", "r")

#Grab headers
headers = f.readline().strip().split(",")
print(headers)

#Make sure to close the file
f.close()

for idx, head in enumerate(headers):
  print(idx, head)
#WIN_COUNTRY_CODE is at idx 61

#Tak 2: Instantiate an ampty list called data
data = []

#Task 3: Use the context manager open() and
#3.1:  iterate through each row in ted_sample.csv and
#3.2:  append each row to the data list using (in the loop body) data.append(list(line.split(",")))
with open("data/raw/european_commission/ted_sample.csv") as f:
  for line in f:
    data.append(list(line.split(",")))

print(data[0])
#We don't need headers (line 0) => get rid of it
data = data[1:]
    
#Task 4: Count the number of wins by country
d = {}
for row in data:
  country = row[61] #Careful: some tenders are won by more than one country
  countries = country.split("---") #Returns a list of winning countries
  for winning_country in countries:
    if not winning_country in d:
      d[winning_country] = 0
    d[winning_country] += 1

print(d)