import os
import itertools, collections
import re
import sys
from sets import Set
import string
def consume(iterator, n):
    collections.deque(itertools.islice(iterator, n))
filename=str(sys.argv[1])
ingredients_file='ingredients2.txt'
f_ingredients=open(ingredients_file)
ingredients=Set()
line=f_ingredients.readline()
while line:
	ingredients.add(line.strip('\n'))
	line=f_ingredients.readline()
f_ingredients.close()
#4 letters at a time
fopen=open(filename,'r')
final1="final1_"+filename
file1=open(final1,'w')
line = fopen.readline()
while line:
	line=line.lstrip().strip('\n')
	arr=line.split()
	length=len(arr)
	if length>=4:
		iterator=range(0,length-3).__iter__()
		for i in iterator:
			flag=False
			string=arr[i]+" "+arr[i+1]+" "+arr[i+2]+" "+arr[i+3]
			var1=re.sub(r'^[\W]+','',string)
			var2=re.sub(r'[\W]+$','',var1)
			var2=var2.lower()
			if [item for item in ingredients if item.lower()==var2]:
				file1.write('<I>'+string+'</I>'+' '),
				consume(iterator,3)
				flag=True
			else:
				file1.write(arr[i]+" "),
		if flag==False:
			file1.write(arr[length-3]+" "+arr[length-2]+" "+arr[length-1]),
		file1.write('\n')
	else:
		file1.write(line+'\n')
	line=fopen.readline()
file1.close()
fopen.close()
# 3 at a time
fopen=open(final1,'r')
final2="final2_"+filename
file1=open(final2,'w')
line = fopen.readline()
while line:
	line=line.lstrip().strip('\n')
	arr=line.split()
	length=len(arr)
	if length>=3:
		iterator=range(0,length-2).__iter__()
		for i in range(0,length-2):
			flag=False
			string=arr[i]+" "+arr[i+1]+" "+arr[i+2]
			var1=re.sub(r'^[\W]+','',string)
			var2=re.sub(r'[\W]+$','',var1)
			var2=var2.lower()
			if [item for item in ingredients if item.lower()==var2]:
				file1.write('<I>'+string+'</I>'+' '),
				consume(iterator,2)
				flag=True
			else:
				file1.write(arr[i]+" "),
		if flag==False:
			file1.write(arr[length-2]+" "+arr[length-1]),
		file1.write('\n')
	else:
		file1.write(line+'\n')
	line=fopen.readline()
file1.close()
fopen.close()
# 2 at a time
fopen=open(final2,'r')
final3="final3_"+filename
file1=open(final3,'w')
line = fopen.readline()
while line:
	line=line.lstrip().strip('\n')
	arr=line.split()
	length=len(arr)
	if length>=2:
		iterator=range(0,length-1).__iter__()
		for i in iterator:
			flag=False
			string=arr[i]+" "+arr[i+1]
			var1=re.sub(r'^[\W]+','',string)
			var2=re.sub(r'[\W]+$','',var1)
			var2=var2.lower()
			if [item for item in ingredients if item.lower()==var2]:
				file1.write('<I>'+string+'</I>'+' '),
				consume(iterator,1)
				flag=True
			else:
				file1.write(arr[i]+" "),
		if flag==False:
			file1.write(arr[length-1]),
		file1.write('\n')
	else:
		file1.write(line+'\n')
	line=fopen.readline()
file1.close()
fopen.close()
# 1 at a time
fopen=open(final3,'r')
final4="final4_"+filename
file1=open(final4,'w')
line = fopen.readline()
while line:
	line=line.lstrip().strip('\n')
	arr=line.split()
	length=len(arr)
	if length>=1:
		iterator=range(0,length).__iter__()
		for i in iterator:
			string=arr[i]
			var1=re.sub(r'^[\W]+','',string)
			var2=re.sub(r'[\W]+$','',var1)
			var2=var2.lower()
			if [item for item in ingredients if item.lower()==var2]:
				file1.write('<I>'+string+'</I>'+' '),
			else:
				file1.write(arr[i]+" "),
		file1.write('\n')
	else:
		file1.write(line+'\n')
	line=fopen.readline()
file1.close()
fopen.close()
os.remove(final1)
os.remove(final2)
os.remove(final3)