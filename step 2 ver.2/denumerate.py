import sys
import shutil
import re


def Denumerate(file):
    shutil.move(file, file+"~")
    source = open(file+"~", "r")
    destination = open(file, "w")
    i = 0
    for line in source:
        arr = line.split()
        for s in arr:
            m = re.search("_", s)
            s = s[m.start() + 1:]
            destination.write(s+' ')
            i = i+1
        destination.write('\n')
    source.close()
    destination.close()


Denumerate(sys.argv[1])
