__author__ = 'Kevin'
# 05/04/2015

# A TALE OF TWO LOOPS

# each method will give you the same result

friends = ["Mary", "Thomas", "Conor"]

for friend in friends:
    print "Happy Easter Hunt", friend
# Happy Easter Hunt Mary
# Happy Easter Hunt Thomas
# Happy Easter Hunt Conor

for i in range(len(friends)):
    print "Happy Easter Hunt index", friends[i]
# Happy Easter Hunt index Mary
# Happy Easter Hunt index Thomas
# Happy Easter Hunt index Conor

for i in range(len(friends)):
    friend = friends[i]
    print "Happy Easter Hunt index2", friend
# Happy Easter Hunt index2 Mary
# Happy Easter Hunt index2 Thomas
# Happy Easter Hunt index2 Conor
