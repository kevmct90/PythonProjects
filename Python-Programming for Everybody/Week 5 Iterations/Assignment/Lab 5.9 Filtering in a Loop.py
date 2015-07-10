__author__ = 'Kevin'
# 06/03/2015
# Filtering in a Loop

# We use an if statement in the loop to catch / filter the values we are looking for.

print 'Before'
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20:
        print 'Large number', value
print 'After'