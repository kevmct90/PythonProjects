__author__ = 'Kevin'
# 19/04/2015

# Regular Expression Quick Guide:
# ^ - Matches the beginning of a line
# $ - Matches the end of the line
# . - Matches any character
# \s - Matches whitespace
# \S - Matches any non-whitespace character
# * - Repeats a character zero or more times
# *? - Repeats a character zero or more times (non-greedy)
# + - Repeats a character one or more times
# +? - Repeats a character one or more times (non-greedy)
# [aeiou] - Matches a single character in the listed set
# [^XYZ] - Matches a single character not in the listed set
# [a-z0-9] - The set of characters can include a range
# ( - Indicates where string extraction is to start
# ) - Indicates where string extraction is to end


# Before you can use regular expressions in your program, you must import the library using "import re"
import re

# You can use re.search() to see if a string matches a regular expression, similar to using the find()
# method for strings
# You can use re.findall() extract portions of a string that match your regular expression similar to a
# combination of find() and slicing: var[5:10].

# Using re.search() like find()
hand = open('/Users/Kevin/Desktop/Programming for Everybody/Week 7 Files/Data/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print line, "paq"

hand = open('/Users/Kevin/Desktop/Programming for Everybody/Week 7 Files/Data/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print line, "mayweather"

# We fine-tune what is matched by adding special characters to the string
# ^ Matches the beginning of a line

hand = open('/Users/Kevin/Desktop/Programming for Everybody/Week 7 Files/Data/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print line, "mayweather2"