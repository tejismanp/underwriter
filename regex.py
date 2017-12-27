import re
from datetime import datetime

gender = r'(\b[Mm]ale)|(\b[Ff]emale)|(\bFEMALE)|(\bMALE)'
#gender = 'Female'or'Male'or'female'or'male'or'FEMALE'or'MALE'

Date = r'(([A-Z0-9][A-Z0-9]?[/])?[A-Z0-9][A-Z0-9]?[/][A-Z0-9][A-Z0-9][A-Z0-9]?[A-Z0-9]?)|([A-Za-z][A-Za-z][A-Za-z]\s..?[,]\s....)'

DOB  = r'DOB|[Dd][aA][tT][eE]\s[oO][fF]\s[Bb][iI][rR][tT][hH]'

year=r'\b(19|20)\d{2}\b'

product_type = r'(\b[Pp]roduct\s[Tt]ype):\s?.*'

faceamount = r'(\b[Ff]ace\s?[Aa]mount:?\s?.*)'

'''
text = open('1.txt') #open text file
for line in text: #iterate through every line
	x = re.findall(Date, line) 
	if len(x) != 0:
		print(x)
'''		
		
a=[0-9]

text = open('1.txt') #open text file
for line in text: #iterate through every line
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
		
	

		

	
		



