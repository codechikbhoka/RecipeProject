import sys
import re
from sets import Set
import string
count=0
filename=sys.argv[1]
fopen=open(filename,'r')
if len(sys.argv)==3:
	word='<'+str(sys.argv[2])+'>'
	line = fopen.readline()
	while line:
		arr=line.strip('\n').split()
		for item in arr:
			matchobj=re.search("%s.*"%word,item,re.M | re.I)
			if matchobj:
				count=count+1
		line = fopen.readline()
	print word+" "+str(count)
else:
	word1='<CA>'
	count1=0
	word2='<I>'
	count2=0
	word3='<iI>'
	count3=0
	word4='<U>'
	count4=0
	line = fopen.readline()
	while line:
		arr=line.strip('\n').split()
		for item in arr:
			matchobj1=re.search("%s.*"%word1,item,re.M | re.I)
			matchobj2=re.search("%s.*"%word2,item,re.M | re.I)
			matchobj3=re.search("%s.*"%word3,item,re.M | re.I)
			matchobj4=re.search("%s.*"%word4,item,re.M | re.I)
			if matchobj1:
				count1=count1+1
			if matchobj2:
				count2=count2+1
			if matchobj3:
				count3=count3+1
			if matchobj4:
				count4=count4+1
		line = fopen.readline()
	print word1+" "+str(count1)
	print word2+" "+str(count2)
	print word3+" "+str(count3)
	print word4+" "+str(count4)