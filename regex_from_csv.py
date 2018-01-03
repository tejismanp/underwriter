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



def reg(st,i):
	x=0
	x1=0
	y=0
	z=0
	w=0
	for line in st: #iterate through every line
		#return list of entities in that line
		if(re.search(Date.decode('utf-8'), line.decode('utf-8'), re.I | re.U)):
			x = re.search(Date.decode('utf-8'), line.decode('utf-8'), re.I | re.U) 
			print x.group(0)+"\n"
			#print x.groups()
			data[i][0]=(x.group(0))
		else:
			data[i][0]=-1
		
		
		if(re.search(year.decode('utf-8'), line.decode('utf-8'), re.I | re.U)):
			x1 = re.search(year.decode('utf-8'), line.decode('utf-8'), re.I | re.U)
			print x1.group(0)
			data[i][1]=x1.group(0)
		else:
			data[i][1]=-1
		
		if(x1 and re.search(DOB.decode('utf-8'), line.decode('utf-8'), re.I | re.U)):
			print "DOB:"+x1.group(0)
			currentYear = datetime.now().year
			print (currentYear-(int)(x1.group(0)))
			data[i][2]=((currentYear-(int)(x1.group(0))))
		else:
			data[i][2]=-1
		 
		if(re.search(gender.decode('utf-8'), line.decode('utf-8'), re.I | re.U)):
			y = re.search(gender.decode('utf-8'), line.decode('utf-8'), re.I | re.U)
			print y.group(0)+"\n"
			data[i][3]=(y.group(0))
		else:
			data[i][3]=-1
			
		if(re.search(product_type.decode('utf-8'), line.decode('utf-8'), re.I | re.U)): 
			z=re.search(product_type.decode('utf-8'), line.decode('utf-8'), re.I | re.U)
			print z.group(0)+"\n"
			data[i][4]=(z.group(0))
		else:
			data[i][4]=-1
		
		if(re.search(faceamount.decode('utf-8'), line.decode('utf-8'), re.I | re.U)):
			w = re.search(faceamount.decode('utf-8'), line.decode('utf-8'), re.I | re.U)
			print w.group(0)+"\n"
			data[i][5]=(w.group(0))
		else:
			data[i][5]=-1
			 
	wtr.writerows(data)

'''
columns = defaultdict(list) # each value in each column is appended to a list

with open('under.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # 
                                

print(columns['Contents'])
print(columns['Offer'])
'''
i=0
w, h = 8, 1;
data = [[-1 for x in range(w)] for y in range(h)]
#data = [[0,0,0,0,0,0,0,0,0,0] for line in range(10)]
st = []
out = open('out.csv', 'w')
wtr= csv.writer( out )
wtr.writerow(['Date','Year','DOB','Gender','Product Type','Face Amount'])
#strs = ["" for x in range(size)]

with open('under.csv') as f:
	rows = csv.reader(f)
	for row in rows:
		print('\n----------------------------------------------')
		st.append(row[8])
		reg(st,i)
		#i+=1
		st=[]
		print row[8]  

out.close()


