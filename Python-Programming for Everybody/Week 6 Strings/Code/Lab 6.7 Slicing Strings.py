__author__ = 'Kevin'
# 22/03/2015

# We can also look at any continuous section of a string using a colon operator
# The second number is one beyond the end of the slice - 'up to but not including'

s = 'Monty Python'
print s[0:4]
# Mont

print s[6:7]
# P

print s[6:20]
# Python

# If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of
# the string respectively
print s[:2]
# Mo

print s[8:]
# thon

print s[:]
