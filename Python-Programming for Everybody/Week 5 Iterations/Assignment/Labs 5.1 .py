__author__ = 'Kevin'
# 06/03/2015

# Repeated Steps
# Loops (repeated steps) have iteration variables that change
# each time through a loop. Often these iteration variables go
# through a sequence of numbers.
n = 5
while n > 0:
    print n
    n = n - 1
print 'Blastoff'
print n


# An Infinite Loop
n = 6
while n > 5:
    print 'Lather'
    print 'Rinse'

print 'Dry off'
# n is not changing so loop will never stop

# Another Loop, also called a zero trip loop
n = 0
while n > 0:
    print 'Lather'
    print 'Rinse'
print 'Dry Off'