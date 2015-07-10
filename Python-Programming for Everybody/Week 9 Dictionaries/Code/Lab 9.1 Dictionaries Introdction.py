__author__ = 'Kevin'
# 06/04/2015

# What is a Collection?

# A collection is nice because we can put more than one value in it and carry them all around in one convenient package
# We have a bunch of values in a single "variable"
# We do this by having more than one place "in" the variable
# We have ways of finding the different places in the variable

# WHAT IS NOT A "COLLECTION"

# Most of our variables have one value in them - when we put a new value in the variable - the old value is overwritten

x = 2
x = 4
print x


# A STORY OF TWO COLLECTIONS
# LIST
# - A linear collection of values that stay in order
# DICTIONARY
# - a "bag" of values each with its own label

# LINK
# http://en.wikipedia.org/wiki/Associative_array

# Dictionaries
# - Dictionaries are Pythons most powerful data collection
# - Dictionaries allow us to do fast database-like operations in Python
# - Dictionaries have different names in different languages
#     Associative Arrays - Perl / PHP
#     Properties or Map or HashMap - Java
#     Property Bag - C# / .Net

# http://en.wikipedia.org/wiki/Associative_array

# Lists index their entries based on the position in the list
purse = dict()
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75
print purse     # {'money': 12, 'tissues': 75, 'candy': 3}

# Dictionaries are like bags - no order

# So we index the things we put in the dictionary with a "lookup tag"
purse["candy"] = purse["candy"] + 100
print purse     # {'money': 12, 'tissues': 75, 'candy': 103}