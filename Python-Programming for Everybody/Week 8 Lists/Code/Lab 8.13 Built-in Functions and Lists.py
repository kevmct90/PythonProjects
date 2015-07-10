__author__ = 'Kevin'
# 05/04/2015

# Built-in Functions and Lists

# There are a number of functions built into Python that take lists as parameters

# Remember the loops we built? These are much simpler.

nums = range(1, 10)
print nums
print len(nums)
print "max", max(nums)
print "min", min(nums)
print "sum", sum(nums)
print "average", sum(nums)/len(nums)

######################################

# Average using Loops VERSUS using built in functions
total = 0
count = 0
while True :
    inp = raw_input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print 'Average:', average

######################################

numlist = list()
while True :
    inp = raw_input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print 'Average:', average