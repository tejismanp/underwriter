import csv
from collections import defaultdict

import re
from datetime import datetime

gender = r'(\b[Mm]ale)|(\b[Ff]emale)|(\bFEMALE)|(\bMALE)'
#gender = 'Female'or'Male'or'female'or'male'or'FEMALE'or'MALE'

Date = r'(([A-Z0-9][A-Z0-9]?[/])?[A-Z0-9][A-Z0-9]?[/][A-Z0-9][A-Z0-9][A-Z0-9]?[A-Z0-9]?)|([A-Za-z][A-Za-z][A-Za-z]\s..?[,]\s....)'

DOB  = r'DOB|[Dd][aA][tT][eE]\s[oO][fF]\s[Bb][iI][rR][tT][hH]'

year=r'\b(19|20)\d{2}\b'

product_type = r'(\b[Pp]roduct\s[Tt]ype):\s?.*'

faceamount = r'(\b[Ff]ace\s?[Aa]mount:?\s?.*)'

def reg(st):
	for line in st: #iterate through every line
		#return list of entities in that line
		x = re.search(Date.decode('utf-8'), line.decode('utf-8'), re.I | re.U) 
		x1 = re.search(year.decode('utf-8'), line.decode('utf-8'), re.I | re.U)
		dob = re.search(DOB.decode('utf-8'), line.decode('utf-8'), re.I | re.U)
		 
		y = re.search(gender.decode('utf-8'), line.decode('utf-8'), re.I | re.U)
		z = re.search(product_type.decode('utf-8'), line.decode('utf-8'), re.I | re.U) 
		w = re.search(faceamount.decode('utf-8'), line.decode('utf-8'), re.I | re.U) 
		if x:
			print x.group(0)+"\n"
			#print x.groups()
		
		if x1 :
			print x1.group(0)
			currentYear = datetime.now().year
			print (currentYear-(int)(x1.group(0)))	
		
		if x1 and dob:
			print "DOB:"+x1.group(0)
			currentYear = datetime.now().year
			print (currentYear-(int)(x1.group(0)))
		
		if y:
			print y.group(0)+"\n"
		if z:
			print z.group(0)+"\n"
		if w:
			print w.group(0)+"\n"


columns = defaultdict(list) # each value in each column is appended to a list

with open('under.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # 
                                

print(columns['Contents'])
print(columns['Offer'])

datafile = open('under.csv', 'r')
datareader = csv.reader(datafile, delimiter=';')
data = []
for row in datareader:
    data.append(row)    
print (data[8])

i=0
st = []
#strs = ["" for x in range(size)]
with open('under.csv') as f:
	rows = csv.reader(f)
	for row in rows:
		st.append(row[8])
		reg(st)
		st=[]
		print row[8]  
	    
'''
csvfile = open('under.csv','rb')
csvFileArray = []
for row in csv.reader(csvfile, delimiter = ','): // Check your delimiter as well
		csvFileArray.append(row) // Storing the data into memory
print(csvFileArray[0][0]) //get the 'Time' over here, easily iterable 2Darray
'''

