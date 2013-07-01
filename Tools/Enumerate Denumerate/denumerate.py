import sys
import shutil
import re

li = ['I', 'mI', 'iI', 'U', 'CA']


def denumerate(file):
    shutil.move(file, file+"~")
    source = open(file+"~", "r")
    destination = open(file, "w")
    i = 0
    for line in source:
        arr = line.split()
        for s in arr:
            sNotTagged = True
            for t in li:
                if s.startswith("<"+t+">"):
                    m = re.search("_", s)
                    s = "<"+t+">" + s[m.start() + 1:]
                    destination.write(s+' ')
                   # destination.write("<"+t+">"+str(i)+'_'+s[len("<"+t+">"):]+' ')
                    sNotTagged = False
            if sNotTagged:
                m = re.search("_", s)
                s = s[m.start() + 1:]
                destination.write(s+' ')
            i = i+1
        destination.write('\n')
    source.close()
    destination.close()


denumerate(sys.argv[1])
