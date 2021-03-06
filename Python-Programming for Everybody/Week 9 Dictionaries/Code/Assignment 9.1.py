__author__ = 'Kevin'
# 06/04/2015

# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent
# the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of
# times they' \ ' appear in the file. After the dictionary is produced, the program reads through the dictionary
# using a' \' maximum loop ' \'to find the most prolific committer.

# Desired Output
# cwen@iupui.edu 5

# /Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt
name = raw_input('Enter file:')
handle = open(name)
counts = {}
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1
    # print counts

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount     # cwen@iupui.edu 5

# /Users/Kevin/Desktop/Programming for Everybody/Week 8/Data/romeo.txt
# name = raw_input('Enter file:')
# handle = open(name)
# text = handle.read()
# words = text.split()
# counts = dict()
# for word in words:
#     counts[word] = counts.get(word,0) + 1
#     print counts
#
# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
#
# print bigword, bigcount