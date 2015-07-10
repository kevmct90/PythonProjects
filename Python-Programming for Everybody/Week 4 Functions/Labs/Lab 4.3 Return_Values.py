## Return Values

## Often a function will take its arguments, do some computation, and
## return a value to be used as the value of the function call in the calling 
## expression. The return keyword is used for this.

## A fruitful function is one that produces a result (or return values)

## The return statement ends the fuctions execution and 'sends back' the result of that function.

def greet(lang):
	if lang =='es':
		return 'Hola'
	elif lang =='fr':
		return 'Bonjour'
	else:
		return 'Hello'

print greet('en'),'Glenn'

print greet('es'),'Sally'

print greet('fr'),'Michael'
