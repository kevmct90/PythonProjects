## Parameters 

## A paramter is a variable which we use in the function definition.
## It is a "handle" that allows the code in the function to access the arguments for a particular function invocation.

def greet(lang):
	if lang =='es':
		print 'Hola'
	elif lang =='fr':
		print 'Bonjour'
	else:
		print 'Hello'

greet('dd')

greet('es')

greet('fr')