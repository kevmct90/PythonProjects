__author__ = 'Kevin'
# 05/04/2015
# A List is an Ordered Sequence

# A list can hold many items and keeps those items in the order until we do something to  change the order

friends = [ 'Joseph', 'Glenn', 'Sally' ]
print friends       # [ 'Joseph', 'Glenn', 'Sally' ]

friends.sort()
print friends       # ['Glenn', 'Joseph', 'Sally']

print friends[0]

# A list can be sorted (i.e., change its order)

# The sort method (unlike in strings) means "sort yourself"