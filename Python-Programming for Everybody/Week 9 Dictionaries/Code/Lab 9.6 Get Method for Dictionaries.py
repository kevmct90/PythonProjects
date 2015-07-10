__author__ = 'Kevin'
# 06/04/2015

# This pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not
# there is so common, that there is a method called get() that does this for us.

# Default value if key does not exist (and no Traceback).

# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#
# if name in counts:
#     x = counts[name]
# else :
#     x = 0
# x = counts.get(name, 0)

# We can use get() and provide a default value of zero when the key is not yet in the dictionary - and then just add one

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print counts        # {'csev': 2, 'zqian': 1, 'cwen': 2}