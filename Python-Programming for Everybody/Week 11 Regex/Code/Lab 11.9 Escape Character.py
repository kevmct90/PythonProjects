__author__ = 'Kevin'
# 19/04/2015

# If you want a special regular expression character to just behave normally (most of the time) you prefix it with '\'
# $, usually used to match the end of a line

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print y

# \$, a real dollar sign
# [0-9.], a digit or period
# +, at least one or more
