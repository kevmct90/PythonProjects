__author__ = 'Kevin'
# 24/03/2015
# File Processing

# A text file can be thought of as a sequence of lines
# A text file has newlines at the end of each line

# File Handle as a Sequence

# A file handle open for read can be treated as a sequence of strings where each line in the file is a string in
# the sequence

# We can use the for statement to iterate through a sequence

# Remember - a sequence is an ordered set

aFile = open("/Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt", "r")
for line in aFile:
    print line
