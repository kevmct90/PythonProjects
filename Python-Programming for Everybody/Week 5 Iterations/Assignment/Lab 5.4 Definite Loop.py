__author__ = 'Kevin'
# 06/03/2015
# Definite Loop

# Quite often we have a list of items of the lines in a file - effectively a finite set of things
# We can write a loop to run the loop once for each of the items in a set using the Python for construct
# These loops are called 'definite loops' because they execute an exact number of times
# We say that 'definite loops iterate through the members of a set'

# keyword in definite is the 'for' command

for i in [5, 4, 3, 2, 1]:
    print i
print 'Blastoff'


# Another Simple Definite Loop
friends = ['joe', 'glenn', 'sally']

for friend in friends:
    print 'Happy New Year', friend
print 'Done!'

# Definite loops (for loops) have explicit iteration variables that change each time through a loop. These iteration
# variables move through the sequence or set.

# LOOKING AT 'in'
# The iteration variable 'iterates' through the sequence (ordered set)
# The block (body) of code is executed once for each value in the sequence
# The iteration variable moves through all of the values in the sequence

# Quite often we have a list of items of the lines in a file - effectively a finite set of things
# We can write a loop to run the loop once for each of the items in a set using the Python for construct
# These loops are called 'definite loops'' because they execute an exact number of times
# We say that 'definite loops iterate through the members of a set'