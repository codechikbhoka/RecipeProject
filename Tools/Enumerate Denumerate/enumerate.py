import sys
import shutil


def enumerate(file):
    shutil.move(file, file+"~")
    source = open(file+"~", "r")
    destination = open(file, "w")
    i = 0
    for line in source:
        arr = line.split()
        for s in arr:
            destination.write(str(i)+'_'+s+' ')
            i = i+1
        destination.write('\n')
    source.close()
    destination.close()

enumerate(sys.argv[1])
