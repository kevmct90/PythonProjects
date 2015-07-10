__author__ = 'Kevin'
# 06/03/2015

# Finishing an Iteration with continue

# The continue statement ends the current iteration and jumps to
# the top of the loop and starts the next iteration

# The continue statement ends the current iteration and jumps
# to the top of the loop and starts the next iteration

while True:
    line = raw_input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print line
print 'Done'

# Test inputs
#   Input              Output
#   hello there        hello there
#   #dont print this
#   # will send the loop back to start and look for input again
#   print this!         print this!
#   done                Done!

# These loops with while keyword are called 'indefinite loops' because they keep going until a logical condition
# becomes False The loops we have seen so far are pretty easy to examine to see if they will terminate or if
# they will be 'infinite loops'
# Sometimes it is a little harder to be sure if a loop will terminate
