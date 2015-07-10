__author__ = 'Kevin'
# 19/04/2015

import re
hand = open('/Users/Kevin/Desktop/Programming for Everybody/Week 7 Files/Data/mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    # [0-9.] matches numbers from zero to nine and dots
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)

print 'Maximum:', max(numlist)