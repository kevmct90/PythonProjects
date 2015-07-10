# sample try and excepts

rawstr = raw_input('Enter Number:')

try:
	ival = int(rawstr)
except:
	ival = -1

if ival > 0:
	print 'Nice Work'

else:
	print 'Not a number'