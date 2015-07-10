__author__ = 'Kevin'
# 24/03/2015
# Using IN to select lines

# We can look for a string anywhere in a line as our selection criteria

aFile = open("/Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt", "r")
for line in aFile:
    line = line.rstrip()
    if not "@uct.ac.za" in line:
        continue
    print line