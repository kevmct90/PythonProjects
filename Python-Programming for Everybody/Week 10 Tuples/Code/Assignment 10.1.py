__author__ = 'Kevin'
# 10/04/2015

# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the
# messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second
# time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# Note that the autograder does not have support for the sorted() function.

# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

# /Users/Kevin/Desktop/Programming for Everybody/Week 7 Files/Data/mbox-short.txt
name = raw_input("Enter file:")
handle = open(name)

counts = dict()

# From cwen@iupui.edu Thu Jan  3 16:29:07 2008
for line in handle:
    # print line
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    # print line
    contents = line.split()
    # print contents[5]
    time = contents[5]
    # print time
    hour = time[0:2]
    # print hour
    counts[hour] = counts.get(hour, 0) + 1
    # print counts

tup = counts.items()
# print tup
tup.sort()
# print tup
for k, v in tup:
    print k, v


