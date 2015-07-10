__author__ = 'Kevin'
# 08/04/2015

# A Tale of Two Sequences
l = list()
# dir(l) what can you do with l, l is a list
print dir(l)        # ['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

t = tuple()
print dir(t)        # ['count', 'index']

# WHY WE USE TUPLES
# Tuples are more efficient

# Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms
# of memory use and performance than lists.
# So in our program when we are making 'temporary variables' we prefer tuples over lists.

# Things not to do with tuples
x = (3, 2, 1)
# x.sort()
# Traceback: AttributeError: 'tuple' object has no attribute 'sort'

# x.append(5)
# Traceback: AttributeError: 'tuple' object has no attribute 'append'

# x.reverse()
# Traceback: AttributeError: 'tuple' object has no attribute 'reverse'


