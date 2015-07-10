
# Rewrite your pay computation to give the employee
# 1.5 times the hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

inp = raw_input("Enter Hours:")
hrs = int(inp)

inp = raw_input("Enter Rate:")
rte=float(inp)

# print rte, hrs

if hrs <=40:
	pay = hrs*rte

else:
	pay = (hrs-40)*(rte*1.5)+(40*rte)
	
print pay


