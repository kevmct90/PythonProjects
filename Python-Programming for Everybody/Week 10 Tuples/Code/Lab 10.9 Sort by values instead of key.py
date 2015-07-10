__author__ = 'Kevin'
# 10/04/2015

# If we could construct a list of tuples of the form (value, key) we could sort by value.
# We do this with a for loop that creates a list of tuples.

c = {'a':10, 'b':1, 'c':22}

tmp = list()

for k, v in c.items() :
    tmp.append( (v, k) )
print tmp       # [(10, 'a'), (22, 'c'), (1, 'b')]

tmp.sort(reverse=True)

print tmp       # [(22, 'c'), (10, 'a'), (1, 'b')]