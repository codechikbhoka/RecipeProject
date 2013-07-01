import sys
import shutil

mark = 0


def modifyMark(str, t):
    global mark
    if str.startswith("<"+t+">") and not str.endswith("</"+t+">"):
        mark = mark + 1
        if mark > 1:
            #str = str[len("<"+t+">"):]
            str = ''
    if not str.startswith("<"+t+">") and str.endswith("</"+t+">"):
        if mark > 1:
            #str = str[:len("</"+t+">")-1]
            str = ''
        mark = mark - 1
    if str.startswith("<"+t+">") and str.endswith("</"+t+">"):
        if mark > 0:
            str = str[len("<"+t+">"):(-1)*(len("</"+t+">"))]

    return str


def refine(file, t):
    shutil.move(file, file+"~")
    source = open(file+"~", "r")
    destination = open(file, "w")

    for line in source:
        arr = line.split()
        for s in arr:
            s = modifyMark(s, t)
            if s is not '':
                s = s + ' '
            destination.write(s)
        destination.write('\n')
    source.close()
    destination.close()

refine(sys.argv[1], 'I')
