# intro to functions!
# define the function & note the different ways to format the arguments 
# 1 -stash in 1 variable and separate later /2- pass 2 separate values
# note that each function's variables are indpendent - they don't talk!
# function names must be 1 word!

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %s, arg2: %s" % (arg1, arg2)

# 2 args - more efficient!
def print_two_again(arg1, arg2):
	print "arg1: %s, arg2: %s" % (arg1, arg2)

# 1 argument
def print_one(arg1):
	print "arg1: %s" % arg1

# 0 args!
def print_none():
	print "I got nothing"

# run/call the functions with arguments!
print_two("hi", "krobe")
print_two_again("hi", "kron")
print_one("kron")
print_none()