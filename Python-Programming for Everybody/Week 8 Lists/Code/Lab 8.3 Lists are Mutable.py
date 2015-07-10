__author__ = 'Kevin'
# 01/04/2015

# LISTS ARE MUTABLE

# Strings are immutable - we cannot change the contents of a string - we must make a new string to make any change
country = 'ireland'
print country[0]    # i

# country[0] = "T"
# Traceback (most recent call last):
#   File "/Users/Kevin/Desktop/Programming for Everybody/Week 8/Code/Lab 8.3 Lists are Mutable.py", line 10, in <module>
#     country[0] = "T"
# TypeError: 'str' object does not support item assignment


lotto = []
print lotto, "lotto"  # [] lotto

numlist = list()
print numlist, " numlist"  # []  numlist

# lotto and numlist demonstrate two methods of creating a list

lotto = lotto + [2, 3, 4, 5, 6, 7]
print lotto  # [2, 3, 4, 5, 6, 7]

# Lists are "MUTABLE"- we can change an element of a list using the index operator
lotto[2] = 50
print lotto  # [2, 3, 50, 5, 6, 7]

# add to
lotto = lotto + [56, 67, 70, 45]
print lotto  # [2, 3, 50, 5, 6, 7, 56, 67, 70, 45]

