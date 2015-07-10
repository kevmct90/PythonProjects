__author__ = 'Kevin'
# 05/04/2015

line = 'A lot of spaces'
etc = line.split()
print etc
# ['A', 'lot', 'of', 'spaces']

line = 'first;second;third'
thing = line.split()
print thing
# ['first;second;third']

print len(thing)
# 1

thing = line.split(';')
print thing
# ['first', 'second', 'third']

print len(thing)
# 3

# to split my multiple character the easiest solution may be to do a string replace and then split on one character?
# Do a str.replace('; ', ', ') and then a str.split(', ')


# When you do not specify a delimiter, multiple spaces are treated like one delimiter
# You can specify what delimiter character to use in the splitting