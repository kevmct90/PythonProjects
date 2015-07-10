__author__ = 'Kevin'
# 19/04/2015

# Fine-Tuning String Extraction
# You can refine the match for re.findall() and separately determine which portion of the match is to be
# extracted by using parentheses
import re

x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('\S+@\S+', x)
print y     # ['stephen.marquard@uct.ac.za']

# \S+@\S+
# at least one white space before and after the @ sign.

# Parentheses are not part of the match - but they tell where to start and stop what string to extract

y1 = re.findall('^From:.*? (\S+@\S+)', x)
print y1