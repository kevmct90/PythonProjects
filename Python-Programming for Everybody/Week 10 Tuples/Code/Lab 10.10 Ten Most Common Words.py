__author__ = 'Kevin'
# 10/04/2015

# /Users/Kevin/Desktop/Programming for Everybody/Week 8/Data/romeo.txt
fhand = open('/Users/Kevin/Desktop/Programming for Everybody/Week 8 Lists/Data/romeo.txt')
counts = dict()

for line in fhand:
    # split the words in each line
    words = line.split()
    for word in words:
        # for each word if it is not in the dictionary add, if it is add 1 to the count
        # The method get() returns a value for the given key. If key is not available then returns default value None.
        counts[word] = counts.get(word, 0) + 1

lst = list()
# The method items() returns a list of dict's (key, value) tuple pairs
for key, val in counts.items():
    lst.append((val, key))

lst.sort(reverse=True)

# once sorted take the top ten value
for val, key in lst[:10]:
    print key, val
    
# Even Shorter Version
# http://wiki.python.org/moin/HowTo/Sorting
# List comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.

c = {'a':10, 'b':1, 'c':22}
print sorted([(v, k) for k, v in c.items()])      # [(1, 'b'), (10, 'a'), (22, 'c')]

tup = c.items()
print sorted(tup, key=lambda tup1: tup1[1])   # [('b', 1), ('a', 10), ('c', 22)]
print sorted(tup, key=lambda tup1: tup1[1], reverse=True)   # [('c', 22), ('a', 10), ('b', 1)]

# Summary
# - Tuple syntax
# - Immutability
# - Comparability
# - Sorting
# - Tuples in assignment statements
# - Sorting dictionaries by either key or value