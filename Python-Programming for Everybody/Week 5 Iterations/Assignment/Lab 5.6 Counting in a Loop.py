__author__ = 'Kevin'
# 06/03/2015
# Counting in a Loop

# To count how many times we execute a loop, we introduce a counter variable that starts at 0 and
# we add one to it each time through the loop.
zork = 0
print 'Before', zork
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print zork, thing
print 'After', zork