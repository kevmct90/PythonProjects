__author__ = 'Kevin'
# 06/04/2015

# You can get a list of keys, values, or items (both) from a dictionary

jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100, 'jan': 200}

# print the keys in jjj using list and print
print list(jjj)     # ['jan', 'chuck', 'fred']
# or by using the keys function
print jjj.keys()        # ['jan', 'chuck', 'fred']

# to get the values use the values function
print jjj.values()

# and to get everything
print jjj       # {'jan': 200, 'chuck': 1, 'fred': 42}
# or
print jjj.items()       # [('jan', 200), ('chuck', 1), ('fred', 42)]
# What is a 'tuple'? - coming soon...