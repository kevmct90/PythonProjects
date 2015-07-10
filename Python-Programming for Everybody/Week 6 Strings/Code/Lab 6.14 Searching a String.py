__author__ = 'Kevin'
# 23/03/2015

# We use the find() function to search for a substring within another string
# Find() finds the first occurrence of the substring
# If the substring is not found, find() returns -1
# Remember that string position starts at zero

fruit = 'banana'
pos = fruit.find('na')
print pos
# 2

aa = fruit.find('zß')
print aa
# -1