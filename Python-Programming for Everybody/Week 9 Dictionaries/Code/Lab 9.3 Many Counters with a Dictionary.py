__author__ = 'Kevin'
# 06/04/2015

# One common use of dictionary is counting how often we "see" something

ccc = {}

ccc['csev'] = 1
ccc['cwen'] = 1
print ccc       # {'csev': 1, 'cwen': 1}

ccc['cwen'] = ccc['cwen'] + 1
print ccc       # {'csev': 1, 'cwen': 2}
