__author__ = 'Kevin'
# 06/03/2015
# How to find the largest value

largest_so_far = -1
print 'Before', largest_so_far
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far:
        largest_so_far = the_num
    print largest_so_far, the_num
print 'After', largest_so_far

# How to find the smallest value
smallest_so_far = -1
print 'Before', smallest_so_far
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print smallest_so_far, the_num
print 'After', smallest_so_far
# Output
# Before -1
# -1 9
# -1 41
# -1 12
# -1 3
# -1 74
# -1 15
# After -1

# We still have a variable that is the smallest so far. The first time through the loop smallest is None,
# so we take the first value to be the smallest.
smallest = None
print 'Before'
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print smallest, value
print 'After', smallest

# Python has an is operator that can be used in logical expressions
# Implies 'is' the same as
# Similar to, but stronger than ==
# is not also is a logical operator