__author__ = 'Kevin'
# 24/03/2015
# Opening a File

# Before we can read the contents of the file, we must tell Python which file we are going to work with and what we will
# be doing with the file

# This is done with the open() function

# open() returns a 'file handle' - a variable used to perform operations on the file

# Similar to 'File -> Open' in a Word Processor


# Using open()

# handle = open(filename, mode)
# returns a handle use to manipulate the file
# filename is a string
# mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file


# What is a Handle?
fhand = open("/Users/Kevin/Desktop/Programming for Everybody/Week 7/Data/mbox-short.txt", "r") # r is read access
print fhand

# below will not work
test = open("mbox-short.txt", "r") # r is read access
print test


