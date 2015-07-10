__author__ = 'Kevin'
# 19/04/2015

# Warning: Greedy Matching
# The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string

import re

x = 'From: Using the : character'
y = re.findall("^F.+:", x)
print y     # From: Using the :

# ^F.+:
# ^F, First character in the match is an F
# .+, One or more
# :, Last character in the match is a :

