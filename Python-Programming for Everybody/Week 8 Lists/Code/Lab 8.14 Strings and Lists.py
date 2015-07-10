__author__ = 'Kevin'
# 05/04/2015

abc = "With three words"
print abc       # With three words
# split allow us to break up strings. Split by default uses white spaces or tabs to split the string.
stuff = abc.split()
print stuff     # ['With', 'three', 'words']

print stuff[0]      # With

# Split breaks a string into parts and produces a list of strings. We think of these as words. We can access
# a particular word or loop through all the words.

for words in stuff:
    print words
# With
# three
# words

