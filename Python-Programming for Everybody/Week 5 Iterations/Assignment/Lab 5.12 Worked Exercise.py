__author__ = 'Kevin'
# 22/03/2015
# Write a programs which reads a list of numbers until "Done" is encountered.
# Once "Done" is entered, print out the total, count, average, of the numbers. If
# the user enters anything other than a number, print an error message and
# skip to the next number.

# Example
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# Average: 5.33333333333


# want to count how often loop runs
count = 0
total = 0
# infinite loop
while True:
    inp = raw_input("Enter a number: ")
    # Don't want to implement count here

    # condition to break loop.
    if inp == "Done":
        break
    # Check for empty line, hitting enter key will make allow user to finish program
    if len(inp) < 1:
        break

    # for crappy data need to add try accept, for invalid input
    try :
    # now do the work
        num = float(inp)
    except:
        print "Invalid input data"
        # continue, done with this iteration its crappy, goes back to start of loop, will not do the work below.
        continue
    count = count + 1
    total = total + num
    print num, total, count

print "Average = ", total/count
print "Count = ", count
print "Done"



