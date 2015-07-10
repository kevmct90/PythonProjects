__author__ = 'Kevin'
# 05/04/2015

fhand = open("/Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt", "r")
# ['From', 'louis@media.berkeley.edu', 'Fri', 'Jan', '4', '18:10:48', '2008']
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    print words     # ['From', 'cwen@iupui.edu', 'Thu', 'Jan', '3', '16:29:07', '2008']
    print words[2]      # Thu
    print email     # cwen@iupui.edu

# Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again

pieces = email.split("@")
hostname = pieces[1]
print hostname  

# Concept of a collection
# - Lists and definite loops
# - Indexing and lookup
# - List mutability
# - Functions: len, min, max, sum
# - Slicing lists
# - List methods: append, remove
# - Sorting lists
# - Splitting strings into lists of words
# - Using split to parse strings
