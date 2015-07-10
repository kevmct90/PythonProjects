__author__ = 'Kevin'
# 19/04/2015

# Wild-Card Characters

# The dot character matches any character
# If you add the asterisk character, the character is 'any number of times'

# X-Sieve: CMU Sieve 2.3
# X-DSPAM-Result: Innocent
# X-DSPAM-Confidence: 0.8475
# X-Content-Type-Message-Body: text/plain

# Regex:    ^X.*:
# At the start of the line match a big X, dot matches any character, * repeats a character zero or many times
# All the above match


# Fine-Tuning Your Match
# Depending on how 'clean' your data is and the purpose of your application, you may want to narrow your
# match down a bit


# X-Sieve: CMU Sieve 2.3
# X-Plane is behind schedule: two weeks
# X-DSPAM-Result: Innocent

# Regex:    ^X-\S+:
# This regex matches any lines that begin with X- and "\S" Match any non-whitespace character, "+" one or more times


