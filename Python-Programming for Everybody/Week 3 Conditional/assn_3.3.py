# 3.3
# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following # table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

try:
	score = float(raw_input("Please Enter a Value between 0.0 and 1.0:"))
except:
	print "Thats not a value between 0.0 and 1.0, Please try again"
	quit() #if except runs quit the program

if 0.9 <= score <= 1.0:
	print 'A'
elif 0.8 <= score < 0.90:
	print 'B'
elif 0.7 <= score < 0.80:
	print 'C'
elif 0.6 <= score < 0.70:
	print 'D'
elif 0.0 <= score < 0.60:
	print 'F'
else:
	print "some other error"			


	