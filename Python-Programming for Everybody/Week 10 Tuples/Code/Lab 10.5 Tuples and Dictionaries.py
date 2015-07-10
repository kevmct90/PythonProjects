__author__ = 'Kevin'
# 08/04/2015

# Tuples and Dictionaries

# The items() method in dictionaries returns a list of (key, value) tuples.

d = dict()
d['csev'] = 2
d['cwen'] = 4
print d     # print dictionary d = {'csev': 2, 'cwen': 4}

for (k,v) in d.items():
    print k, v
# csev 2
# cwen 4

# items returns a list which contains tuples (key, value)
tups = d.items()
print tups      # [('csev', 2), ('cwen', 4)]