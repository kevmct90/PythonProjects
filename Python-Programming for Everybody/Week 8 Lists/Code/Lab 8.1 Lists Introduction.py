__author__ = 'Kevin'
# 01/04/2015

# A List is a kind of Collection
# - A collection allows us to put many values in a single "variable"
# - A collection is nice because we can carry all many values around in one convenient package.
friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']

print friends
print carryon


# WHAT IS NOT A COLLECTION
# Generally variables have one value in them, when we put a new value in them the olc one is overwritten
# Example
x = 2
x = 4
print x


# LIST CONSTANTS
# List constants are surrounded by square brackets and the elements in the list are separated by commas
print [1, 24, 76]
print ['red', 'yellow', 'blue']

# A list element can be any Python object - even another list
print [1, [5, 6], 7]

# A list can be empty
print []

# EXAMPLE USING LISTS ALREADY
for i in [1,2,3,4,5]:
    print i
print "i dont care"

# LISTS AND DEFINITE LOOPS WORK QUITE WELL TOGETHER
friends = ["lads", "college", "work"]
for friend in friends:
    print "Great bunch of lads", friend
print "well done"






