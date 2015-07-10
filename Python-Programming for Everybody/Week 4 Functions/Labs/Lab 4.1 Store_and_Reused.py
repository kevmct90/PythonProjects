# Store (and reused)
# Stored and reusable pieces of code are called "functions"
x = 5
def hello():
	print 'Hello'
	print 'Fun'

hello()

print 'Zip'

hello()

print 'Zip2'


## ARGUEMMENTS
# built in function max that finds the largest value, this happens to be the lowercase w
big = max('Hello world')
print big

small = min('Helloworld')
print small


# Definition
def print_lyrics():
	# x in the definition is independent of the x globally
	x = 4
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."
	x = 4 + 2
	print x

# Call/Invoke
print_lyrics()
x = x + 2
print x