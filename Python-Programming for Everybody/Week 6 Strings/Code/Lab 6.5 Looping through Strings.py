__author__ = 'Kevin'
# 22/03/2015

# Looping Through Strings

# Using a while statement and an iteration variable, and the len function, we can
# construct a loop to look at each of the letters in a string individually.

fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print index, letter
    index = index + 1

# 0 b
# 1 a
# 2 n
# 3 a
# 4 n
# 5 a

# A definite loop using a for statement is much more elegant
# The iteration variable is completely taken care of by the for loop
fruit1 = 'banana'
for letter1 in fruit1:
    print letter1