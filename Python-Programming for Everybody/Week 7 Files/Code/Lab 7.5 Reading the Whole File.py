__author__ = 'Kevin'
# 24/03/2015

# We can read the whole file (newlines and all) into a single string

# Should only be done when data is small as all data will be memory. Reads in all the characters

aFile = open("/Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt", "r")
inp = aFile.read()

print len(inp)
# 94626 count all the charaters in the file

print inp[:20]
# From stephen.marquar, slice taking the from 0 up to but not including 20.

