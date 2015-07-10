__author__ = 'Kevin'
# 22/03/2015

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and
# put out an appropriate message and ignore the number.
# Enter the numbers from the book for problem 5.1 and Match the desired output as shown.

# None, The sole value of types.NoneType. None is frequently used to represent the absence of a value,
# as when default arguments are not passed to a function.

# Numbers 5,4,3,2,1

largest_value = None
smallest_value = None
#error = None

# infinite loop
while True:
    inp = raw_input("Enter an integer number: ")

    # condition to break loop.
    if inp == "Done":
        break

    # for crappy data need to add try accept, for invalid input
    try:
        # now do the work
        num = int(inp)
    except:
        #if error is None:
            #error = "Invalid input"
        # print "Please enter a valid integer number"
        print "Invalid input"
        # continue, done with this iteration its crappy, goes back to start of loop, will not do the work below.
        continue
    if largest_value is None:
        largest_value = num
    else:
        if num > largest_value:
            largest_value = num

    if smallest_value is None:
        smallest_value = num
    else:
        if num < smallest_value:
            smallest_value = num
# print error
print "Maximum is", largest_value
print "Minimum is", smallest_value