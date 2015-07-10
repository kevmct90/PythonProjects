__author__ = 'Kevin'
# 23/03/2015

str  = 'Test'

# Return a copy of the string with its first character capitalized and the rest lowercased.
# For 8-bit strings, this method is locale-dependent.
print str.capitalize()

# Return centered in a string of length width. Padding is done using the specified fillchar (default is a space).
# Changed in version 2.4: Support for the fillchar argument.
# str.center(width[, fillchar])


# Return True if the string ends with the specified suffix, otherwise return False.
# suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position.
# With optional end, stop comparing at that position.
# Changed in version 2.5: Accept tuples as suffix.
# str.endswith(suffix[, start[, end]])

# Return the lowest index in the string where substring sub is found, such that sub is contained in the slice
# s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
# str.find(sub[, start[, end]])

# Return a copy of the string with leading characters removed. The chars argument is a string specifying the set
# of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace.
# The chars argument is not a prefix; rather, all combinations of its values are stripped:
# str.lstrip([chars])

# Return a copy of the string with all occurrences of substring old replaced by new.
# If the optional argument count is given, only the first count occurrences are replaced.
# str.replace(old, new[, count])

# Return a copy of the string with all the cased characters [4] converted to lowercase.
# For 8-bit strings, this method is locale-dependent.
# str.lower()

# Return a copy of the string with trailing characters removed.
# The chars argument is a string specifying the set of characters to be removed.
# If omitted or None, the chars argument defaults to removing whitespace.
# The chars argument is not a suffix; rather, all combinations of its values are stripped:
# str.rstrip([chars])

# Return a copy of the string with the leading and trailing characters removed.
# The chars argument is a string specifying the set of characters to be removed.
# If omitted or None, the chars argument defaults to removing whitespace.
# The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:
# str.strip([chars])

# Return a copy of the string with all the cased characters [4] converted to uppercase.
# Note that str.upper().isupper() might be False if s contains uncased characters or if the Unicode category
# of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. “Lt” (Letter, titlecase).
# For 8-bit strings, this method is locale-dependent.
# str.upper()
