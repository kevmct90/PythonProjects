__author__ = 'Kevin'
# 06/04/2015

# We loop through the key-value pairs in a dictionary using *two* iteration variables.

# Each iteration, the first variable is the key and the second variable is the corresponding value for the key.

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for aaa,bbb in jjj.items():
    print aaa, bbb
# jan 100
# chuck 1
# fred 42

# find the most common word in a text file.

# /Users/Kevin/Desktop/Programming for Everybody/Week 8/Data/romeo.txt
name = raw_input('Enter file:')
handle = open(name)
text = handle.read()
words = text.split()
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
    print counts

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount