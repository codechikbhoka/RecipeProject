import sys
import shutil
import re
# <I>salted</I>

dict = {'I': 'Ingredients', 'mI': 'Modified Ingredients', 'U': 'Utensils', 'iI': 'Intermediate Ingredients', 'CA': 'Cooking Action'}

li = ['I', 'mI', 'iI', 'U', 'CA']


def compare(file1, file2, s):
    enumerate(file1)
    enumerate(file2)

    output = open(file1 + "_" + file2 + "_comparison.txt", "a")
    output.write(dict[s] + " : " + "\n[")
    source1 = open(file1, "r")
    source2 = open(file2, "r")
    list1 = []
    list2 = []

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

    flag = 5
    for line in source2:
        arr2 = line.split()
        for s2 in arr2:
            if flag == 10 and not s2.endswith("</"+s+">"):
                # print s2,
                list2[-1] = list2[-1] + " " + s2
            if flag == 10 and s2.endswith("</"+s+">"):
                # print s2
                list2[-1] = list2[-1] + " " + s2
                flag = 5
            elif flag == 5 and s2.startswith("<"+s+">"):
                if not s2.endswith("</"+s+">"):
                    flag = 10
                    # print s2,
                list2.append(s2)

    source1.close()
    source2.close()
    denumerate(file1)
    denumerate(file2)

    manual = len(list1)
    programmedTotal = len(list2)
    skipped = 0
    wrong = 0

    if list1 != list2:
        output.write("\n     In " + file1 + " but NOT in " + file2 + "\n")
        for k in list1:
            if k not in list2:
                output.write("         " + k + "\n")
                skipped = skipped + 1
        output.write("\n")
        output.write("     In " + file2 + " but NOT in " + file1 + "\n")
        for k in list2:
            if k not in list1:
                output.write("         " + k + "\n")
                wrong = wrong + 1
    output.write("]\n")
    output.close()

    result = open("result.txt", "a")
    result.write(file1 + ',' + dict[s] + ',' + str(manual) + ',' + str(programmedTotal) + ',' + str(skipped) + ',' + str(wrong) + '\n')
    result.close()



def enumerate(file):
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
                    destination.write("<"+t+">"+str(i)+'_'+s[len("<"+t+">"):]+' ')
                    sNotTagged = False
            if sNotTagged:
                destination.write(str(i)+'_'+s+' ')
            i = i+1
        destination.write('\n')
    source.close()
    destination.close()


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


if len(sys.argv) < 3:
    print "Wrong command, sample commands are :\nfor tagging all kinds : python compare.py file_1.txt file_2.txt\nfor tagging ingredient : python compare.py file_1.txt file_2.txt I\nfor tagging cooking action : python compare.py file_1.txt file_2.txt CA\nfor tagging intermediate ingredient : python compare.py file_1.txt file_2.txt iI\nfor tagging modified ingredient : python compare.py file_1.txt file_2.txt mI\nfor tagging utensils : python compare.py file_1.txt file_2.txt U"

elif len(sys.argv) == 3:  # if no argument like I, mI, U is passed
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output = open(file1 + "_" + file2 + "_comparison.txt", "w")
    output.write('')
    output.close()
    for s in li:
        # print s
        compare(file1, file2, s)
else:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output = open(file1 + "_" + file2 + "_comparison.txt", "w")
    output.write('')
    output.close()
    for s in sys.argv[3:]:
        # print s
        compare(file1, file2, s)

result = open("result.txt", "a")
result.write('\n')
result.close()
