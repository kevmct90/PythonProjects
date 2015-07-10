__author__ = 'Kevin'
# 24/03/2015
# Assignment 7.2

# Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values from each of the lines and compute the average of those
# values and produce an output as shown below.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing
# below enter mbox-short.txt as the file name.

# /Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt

fileName = raw_input("Enter a filename: ")
try:
    aFile = open(fileName, "r")
except:
    print "haha try again next time", fileName
    exit()
count = 0
totalSum = 0
index = 0
lenLine = 0
for line in aFile:
    line = line.rstrip() # Strips the newline character from each line in the loop, new line will then be added by print
    # skip uninteresting lines
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # process interesting lines
    count = count + 1
    index = line.index(" ")
    lenLine = len(line)
    totalSum = totalSum + float(line[index+1:lenLine])
    # print line[index+1:lenLine]
    # print index
    # print lenLine
print "Average spam confidence:", totalSum/count
# Average spam confidence: 0.750718518519
