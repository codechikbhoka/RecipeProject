import sys


def compare(str):
    pass

if len(sys.argv) < 3:
    print "Wrong command, sample commands are :\nfor tagging all kinds : python compare.py file_1.txt file_2.txt\nfor tagging ingredient : python compare.py file_1.txt file_2.txt I\nfor tagging cooking action : python compare.py file_1.txt file_2.txt CA\nfor tagging intermediate ingredient : python compare.py file_1.txt file_2.txt iI\nfor tagging modified ingredient : python compare.py file_1.txt file_2.txt mI\nfor tagging utensils : python compare.py file_1.txt file_2.txt U"

li = ['I', 'mI', 'iI', 'U', 'CA']

if len(sys.argv) == 3:  # if no argument like I, mI, U is passed
    for s in li:
        # print s
        compare(s)
else:
    for s in sys.argv[3:]:
        # print s
        compare(s)
