__author__ = 'Kevin'
# 19/04/2015

# Non-Greedy Matching
# Not all regular expression repeat codes are greedy! If you add a ? character - the + and * chill out a bit...

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)     # ['From:']
print y

# '^F.+?:'
# ^F, First character in the match is an F
# .+?, One or more characters but not greedy
# :, last character in the match is a:
