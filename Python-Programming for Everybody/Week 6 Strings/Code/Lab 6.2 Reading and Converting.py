__author__ = 'Kevin'
# 22/03/2015

# We prefer to read data in using strings and then parse and convert the data as we need.
# This gives us more control over error situations and/or bad user input.
# Raw input numbers must be converted from strings.

name = raw_input('Enter:')
# Chuck

print name

apple = raw_input('Enter:')
# 100

# x = apple - 10
# Traceback (most recent call last):
#   File "/Users/Kevin/Desktop/Programming for Everybody/Week 6/Code/Lab 6.2 Reading and Converting.py", line 16, in
#  <module>
#     x = apple - 10
# TypeError: unsupported operand type(s) for -: 'str' and 'int'

x = int(apple) - 10
print x

