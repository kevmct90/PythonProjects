__author__ = 'Kevin'
# 06/03/2015

# Breaking Out of a Loop

# The break statement ends the current loop and jumps to the statement immediately following the loop
# It is like a loop test that can happen anywhere in the body of the loop

# break says if in a loop and condition not satisfied then get out of the loop, basically
# its going to prompt for strings of characters if you enter done it will break and print
# 'Done!' otherwise it will print what you input

while True:
    line = raw_input('> ')
    if line == 'done':
        break
    print line
print 'Done!'

# while true makes your loop infinite