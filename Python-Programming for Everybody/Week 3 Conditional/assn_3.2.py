# Rewrite your pay program using try and except so
# that your program handles non-numeric input
# gracefully.
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

try:
	inp = raw_input("Enter Hours:")
	hrs = int(inp)	
	inp = raw_input("Enter Rate:")
	rte=float(inp)

except:
	print "please enter a numeric input"
	quit() #if except runs quit the program

if hrs <=40:
	pay = hrs*rte

else:
	pay = (hrs-40)*(rte*1.5)+(40*rte)

print pay



