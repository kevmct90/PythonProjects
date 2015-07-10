__author__ = 'Kevin'
# 05/04/2015

# BUILDING A LIST FROM SCRATCH

# We can create an empty list and then add elements using the append method
stuff = list()
print stuff

stuff.append("book")
print stuff


other_stuff = []
print other_stuff

other_stuff.append("other book")
print other_stuff

# The list stays in order and new elements are added at the end of the list
stuff.append("more")
other_stuff.append("junk")

print stuff
print other_stuff