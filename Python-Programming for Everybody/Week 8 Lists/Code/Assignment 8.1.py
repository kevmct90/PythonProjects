__author__ = 'Kevin'
# 06/04/2015

# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the
# split() function. The program should build a list of words. For each word on each line check to see if the word is
# already in the list and if not append it to the list. When the program completes, sort and print the resulting words
# in alphabetical order. You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
#
# fname = raw_input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
# print line.rstrip()

# /Users/Kevin/Desktop/Programming for Everybody/Week 8/Data/romeo.txt
fname = raw_input("Enter file name :")
fh = open(fname)
lst = []

for line in fh:
    # print line
    words = line.split()        # split each line into a list of words
    for word in words:      # for each word in the the list of words
        if word in lst:     # if word is in the lst of words, continue, go back to the start of loop
            continue
        lst.append(word)        # otherwise append the word to the list of words
        # print word
    # print words
lst.sort()
print lst