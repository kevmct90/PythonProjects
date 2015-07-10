__author__ = 'Kevin'
# 19/04/2015

# Matching and Extracting Data

# The re.search() returns a True/False depending on whether the string matches the regular expression
# If we actually want the matching strings to be extracted, we use re.findall()

# [0-9]+
# One or more digits

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print y
# ['2', '19', '42']

# [0-9]*
# Zero or more digits
x1 = 'My favorite numbers  are and '
y1 = re.findall('[0-9]*', x1)
print y1, "2"
# ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
# '', '', '', '', '']

# When we use re.findall(), it returns a list of zero or more sub-strings that match the regular expression
y2 = re.findall('[AEIOU]+', x)
print y2, "3"

