__author__ = 'Kevin'
# 08/04/2015

# Tuples are Comparable

# The comparison operators work with tuples and other sequences. If the first item is equal, Python goes on to the
# next element, and so on, until it finds elements that differ.

print (0, 1, 2) < (5, 1, 2)
# True
print (0, 1, 2000000) < (0, 3, 4)
# True
print ( 'Jones', 'Sally' ) < ('Jones', 'Sam')
# True
print ( 'Jones', 'Sally') > ('Adams', 'Sam')
# True
print ( 'Jones', 'Sally') < ('Adams', 'Sam')
# False




True
False