__author__ = 'Kevin'
# 24/03/2015
# Prompt for FileName

# /Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt

fileName = raw_input("Enter a fucking filename: ")
aFile = open(fileName, "r")
count = 0
for line in aFile:
    line = line.rstrip()
    if line.startswith("Subject"):
        count = count + 1
        continue
print "There were", count, "subject lines in", fileName


