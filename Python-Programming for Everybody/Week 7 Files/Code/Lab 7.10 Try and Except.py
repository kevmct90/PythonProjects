__author__ = 'Kevin'
# 24/03/2015
# Try and except

# /Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt

# if file does not exist or cannot be accessed the below code will fail

# fileName = raw_input("Enter a fucking filename: ")
# aFile = open(fileName, "r")
# count = 0
# for line in aFile:
#     line = line.rstrip()
#     if line.startswith("Subject"):
#         count = count + 1
#         continue
# print "There were", count, "subject lines in", fileName

# need to add a try and except

fileName = raw_input("Enter a fucking filename: ")
try:
    aFile = open(fileName, "r")
except:
    print "haha try again next time", fileName
    exit()
count = 0
for line in aFile:
    line = line.rstrip()
    if line.startswith("Subject"):
        count = count + 1
        continue
print "There were", count, "subject lines in", fileName

# Summary
# Secondary storage
# Opening a file - file handle
# File structure - newline character
# Reading a file line by line with a for loop
# Searching for lines
# Reading file names
# Dealing with bad files
