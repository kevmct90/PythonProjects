def computepay(h,r):
	if h<=40:
		pay = h*r
	else:
		pay = (h-40)*(r*1.5)+(40*r)
	return pay

hrs = float(raw_input("Enter Hours:"))
rte = float(raw_input("Enter Rate:"))

p = computepay(hrs,rte)
#print "Pay",p
print p
