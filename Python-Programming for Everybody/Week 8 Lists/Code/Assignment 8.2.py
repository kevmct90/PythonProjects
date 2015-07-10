__author__ = 'Kevin'
# 06/04/2015

# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From '
# like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# You will parse the From line using split() and print out the second word in the line
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
#
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

# /Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt

fname = raw_input("Enter file name :")
fh = open(fname)

e_list = []
count  = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    # print line
    words = line.split()
    email = words[1]
    # print words     # ['From', 'cwen@iupui.edu', 'Thu', 'Jan', '3', '16:29:07', '2008']
    # print words[2]      # Thu
    # print email     # cwen@iupui.edu
    e_list.append(email)        # append email address to list
    count = count + 1
for email1 in e_list:
    print email1
print "There were", count, "lines in the file with From as the first word"