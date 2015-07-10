__author__ = 'Kevin'
# 23/03/2015

# Sometimes we want to take a string and remove whitespace at the beginning and/or end

# lstrip() and rstrip() remove whitespace at the left or right

# strip() removes both beginning and ending whitespace

greet = "      Hello     Bob   "

print greet.lstrip()

print greet.rstrip().lstrip()
