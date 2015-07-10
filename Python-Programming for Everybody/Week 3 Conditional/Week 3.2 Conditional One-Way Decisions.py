#Increase indent indent after an if statement or for statement (after : )
#Maintain indent to indicate the scope of the block (which lines are affected by the if/for)
#Reduce indent back to the level of the if statement or for statement to
#indicate the end of the block
#Blank lines are ignored - they do not affect indentation
#Comments on a line by themselves are ignored with regard to indentation


x = 6
print 'Before 5'

if x==5:
	print 'Is 5'
	print 'Is Still 5'
	print 'Third 5'

print 'Afterwards'

print 'Before 6'
if x==6:
	print 'is 6'
	print 'is still 6'
	print 'third 6'

print 'afterwards 6'