__author__ = 'Kevin'
# 24/03/2015
# Skipping with continue

aFile = open("/Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt", "r")
for line in aFile:
    line = line.rstrip() # Strips the newline character from each line in the loop, new line will then be added by print
    # skip uninteresting lines
    if not line.startswith("From:"):
        continue
    # process interesting lines
    print line
