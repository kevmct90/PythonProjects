__author__ = 'Kevin'
# 06/04/2015

# It is an error to reference a key which is not in the dictionary

# We can use the in operator to see if a key is in the dictionary

ccc = {}

print "csev" in ccc     # False

print ccc["ccccc"]
# Traceback (most recent call last):
# File "/Users/Kevin/Desktop/Programming for Everybody/Week 9/Code/Lab 9.4 Dictionary Tracebacks.py",
# line 9, in <module>
#     print ccc["ccccc"]
# KeyError: 'ccccc'

