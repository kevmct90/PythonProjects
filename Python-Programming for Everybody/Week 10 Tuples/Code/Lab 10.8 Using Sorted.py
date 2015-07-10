__author__ = 'Kevin'
# 10/04/2015

# We can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a
# sorted sequence

d = {'a':10, 'b':1, 'c':22}

print d.items()       # [('a', 10), ('c', 22), ('b', 1)]
t = sorted(d.items())
print t     # [('a', 10), ('b', 1), ('c', 22)]
for k, v in sorted(d.items()):
    print k, v
    # a 10
    # b 1
    # c 22