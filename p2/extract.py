import sys
from sets import Set
import string
ingredients = Set()
f_ingredients = open('./ingredients/ingredients.txt','r')
f_new=open('ingredients2.txt','w')
line = f_ingredients.readline()
while line:
	arr=line.strip('\n').split(',')
	for item in arr:
		if item not in ingredients:
			ingredients.add(item.lstrip().lower())
	line=f_ingredients.readline()
f_ingredients.close()
man = list(set(ingredients))
man.sort()
string = ''
for item in man:
	current = str(item)
	if current != string:
		string=str(item)
		f_new.write(string+"\n")
f_new.close()