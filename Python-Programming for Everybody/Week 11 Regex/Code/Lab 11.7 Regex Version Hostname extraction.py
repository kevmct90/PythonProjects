__author__ = 'Kevin'
# 19/04/2015

import re

lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)', lin)
print y

# [^XYZ] - Matches a single character not in the listed set

# '@([^ ]*)'
# @, Look through the string until you find an at sign
# [^ ], Match non-blank character
# *, Match many of them



y2 = re.findall('^From .*@([^ ]*)', lin)
print y2

# '^From .*@([^ ]*)'
# ^From, Starting at the beginning of the line, look for the string 'From '
# .*@, Skip a bunch of characters, looking for an at sign
# (, start extracting
# [^ ]*), [^ ] Match non-blank character, * match many of them
# ), stop extracting






