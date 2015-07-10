#	You surround a dangerous section of code with try and except
#	If the code in the try works - the except is skipped
#	If the code in the try fails - it jumps to the except section

astr = 'Hello Bob'
try:
	istr = int(astr)
except:
	istr = -1

print "First",istr

astr = '123'
try:
	istr = int(astr)
except:
	istr = -1

print 'Secomd',istr