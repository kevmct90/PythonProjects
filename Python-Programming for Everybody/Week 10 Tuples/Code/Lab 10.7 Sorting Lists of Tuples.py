__author__ = 'Kevin'
# 08/04/2015

# We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
# First we sort the dictionary by the key using the items() method

# create a dictionary
d = {'a':10, 'b':1, 'c':22}

# The method items() returns a list of dict's (key, value) tuple pairs
t = d.items()

print t     # [('a', 10), ('c', 22), ('b', 1)]
t.sort()
print t     # [('a', 10), ('b', 1), ('c', 22)]