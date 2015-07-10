__author__ = 'Kevin'
# 24/03/2015
# Counting Lines in a File

# Open a file read-only
# Use a for loop to read each line
# Count the lines and print out the number of lines

count = 0
aFile = open("/Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt", "r")
for line in aFile:
    count = count + 1
print "Line Count", count
# Line Count 1910, count each line in file


# cannot to len(aFile) to get the number of files because in reality this is not really accessing the data so it has
# to be read to do something with it.



