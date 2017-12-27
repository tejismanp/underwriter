import csv
datafile = open('under.csv', 'r')
datareader = csv.reader(datafile, delimiter=';')
data = []
for row in datareader:
    data.append(row)    
print (data[1:4])
