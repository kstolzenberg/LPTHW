# review of what you know so far
# write down every symbol that you have used. review and recall from memory

print = print to command line
'' strings need to be in quotes
can print math directly, booleans
variable_name = x (then can pass through other statements)
"%r %s %d" = string operator functions - pass variables through strings
	syntax = print "hi %s %d" % (variable_name, age)
	you can also store string formatters in a variables
	formatter = "%r %r %r" // print formatter % (hi whats up)
'\n' = new line
'\t' = tabbed in 
'\\' helps with slashes and tricky characters
raw_input()  = prompt for user input / can store in a variable to manipulate further! & pass to strings
CLI - pydoc will give you automatic documentation about features
import modules
argv = argument variable - need to pass input along when you run the script
	can definite how many you want at the top of the script as variables
	then you can manipulate these with string formatters
can open/read/write files through python
	use raw_input() to avoid hard-coding the file variable_name
	process: open file, store in variable, read variable, close variable
	you can also write to a file, append/overwrite etc via variable.write
	when you write to a file you can pass string operators through as well that you get from user input
	can generate these files through CLI: touch/ echo > / cat
functions
	def name (arg, arg2):
		actions
	need to call them!!
	name(var1, var2)
	you can pass numbers, variabels, expressions, raw_input() as function args!
	return will be the final thing and can store the result in variable
		var = name(3,4)


