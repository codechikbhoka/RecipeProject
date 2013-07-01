import sys


def extract(file1, s):
    source1 = open(file1, "r")
    list1 = []
    flag = 5
    for line in source1:
        arr1 = line.split()
        for s1 in arr1:
            if flag == 10 and not s1.endswith("</"+s+">"):
                list1[-1] = list1[-1] + " " + s1
            if flag == 10 and s1.endswith("</"+s+">"):
                list1[-1] = list1[-1] + " " + s1
                flag = 5
            elif flag == 5 and s1.startswith("<"+s+">"):
                if not s1.endswith("</"+s+">"):
                    flag = 10
                list1.append(s1)
    source1.close()

    output = open(sys.argv[1] + "_Extracted_Tags.txt", "a")
    for k in list1:
        output.write(k + '\n')

li = ['I', 'mI', 'iI', 'U', 'CA']

if len(sys.argv) < 2:
    print "Wrong command"

elif len(sys.argv) == 2:  # if no argument like I, mI, U is passed
    file1 = sys.argv[1]
    output = open(sys.argv[1] + "_Extracted_Tags.txt", "w")
    output.write('')
    output.close()
    for s in li:
        extract(file1, s)
else:
    file1 = sys.argv[1]
    output = open(sys.argv[1] + "_Extracted_Tags.txt", "w")
    output.write('')
    output.close()
    for s in sys.argv[2:]:
        extract(file1, s)
