__author__ = 'Kevin'
# 24/03/2015
# Searching through a File

# We can put an if statement in our for loop to only print lines that meet some criteria
aFile = open("/Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt", "r")
for line in aFile:
    if line.startswith("From:"):
        print line

# output reveals that print statement adds a newline
# From: louis@media.berkeley.edu
#
# From: zqian@umich.edu
#
# From: rjlowe@iupui.edu
#
# From: zqian@umich.edu
#
# From: rjlowe@iupui.edu

# What are all these blank lines doing here?
# Each line from the file has a newline at the end
# The print statement adds a newline to each line


# We can strip the whitespace from the right-hand side of the string using rstrip() from the string library
# The newline is considered "white space" and is stripped
aFile = open("/Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt", "r")
for line in aFile:
    line = line.rstrip() # Strips the newline character from each line in the loop, new line will then be added by print
    if line.startswith("From:"):
        print line
# output
# From: stephen.marquard@uct.ac.za
# From: louis@media.berkeley.edu
# From: zqian@umich.edu
# From: rjlowe@iupui.edu
# From: zqian@umich.edu