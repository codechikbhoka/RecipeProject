import itertools, collections
import re
import sys
from sets import Set
import string
def consume(iterator, n):
    collections.deque(itertools.islice(iterator, n))
ingredients=Set()
ingredients.add('girl')
ingredients.add('boy')
man='GIRL'
man2='bond'
var=";;mainak sethi,,,binh;;"
var1=re.sub(r'^[\W]+','',var)
var2=re.sub(r'[\W]+$','',var1)
print var2
if man in ingredients:
	print man
if 'boy' in ingredients:
	print 'boy'
man=man.lower()
if [item for item in ingredients if item.lower()==man]:
	print('<I>'+man+'</I>'+' '),
iterator = range(0,8).__iter__()
for i in iterator:
	if i==2:
		consume(iterator,3)
	print i