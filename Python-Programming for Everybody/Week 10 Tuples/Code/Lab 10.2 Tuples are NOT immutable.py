__author__ = 'Kevin'
# 08/04/2015

# Tuples are NOT immutable

# Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string
x = [9, 4, 7]
print x     # [9, 4, 7]
x[2] = 6
print x     # [9, 4, 6]

# cannot convert string variable
# y = 'ABC'
# y[2] = 'D'      # Traceback:'str' object does not support item Assignment

# z = (5, 4, 3)
# z[2] = 0        # Traceback:'tuple' object does not support item Assignment