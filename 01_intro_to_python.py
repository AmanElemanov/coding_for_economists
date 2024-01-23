 -#Exercise: Indexing snd slicing

url = "https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv"

#Use indexing and slicing to fill in the following output
#Copy/paste is not allowed

file_name=url[start_index:last_index]
print(file_name) // "ted-sample.csv"

protocol=
print(protocol) // "https"

host_name=
print(host_name) // "github.com"

#Use string composition to construct http://github.com/ted-sample.csv
output = protocol + "://" + host_name + "/" + file_name
print(output) // "https://github.com/ted-sample.csv"