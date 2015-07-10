__author__ = 'Kevin'
# 22/03/2015

# This is a simple loop that loops through each letter in a string and counts the number of times the loop encounters
# the 'a' character

word = "banana "
count = 0
for letter in word:
    if letter == "a" or letter =="b":
        count = count + 1
print count

# Looking deeper into in

# The iteration variable 'iterates' through the sequence (ordered set)
# The block (body) of code is executed once for each value in the sequence
# The iteration variable moves through all of the values in the sequence

# The iteration variable 'iterates' through the string and the block (body) of code is executed once for each
# value in the sequence