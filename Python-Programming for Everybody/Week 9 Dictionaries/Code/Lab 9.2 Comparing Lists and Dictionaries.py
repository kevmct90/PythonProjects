__author__ = 'Kevin'
# 06/04/2015

# Dictionaries are like Lists except that they use keys instead of numbers to look up values

lst = []
lst.append("21")
lst.append("1000")
print lst       # ['21', '1000']

lst[0] = 23
print lst       # [23, '1000']

ddd = dict()
ddd["age"] = 21
ddd["course"] = 1000
print ddd       # {'course': 1000, 'age': 21}

ddd["age"] = 23
print ddd       # {'course': 1000, 'age': 23}

ddd1 = {}
ddd1["test"] = "hello"
print ddd1      # {'test': 'hello'}