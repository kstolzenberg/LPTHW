# returning values from functions with return

def add (a, b):
	print "adding %d + %d" % (a, b) # note just a string, not the operation
	return a + b # the actual operation

def subtract (a, b):
	print "subtracting %d - %d" % (a, b)
	return a - b

def multiply (a, b):
	print "multiplying %d * %d" % (a, b)
	return a * b

def divide (a, b):
	print "dividing %d / %d" % (a, b)
	return a / b

print "let's do some math with just functions!"

# you still need to stash the return value in a variable then you can access it later!!!
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)


print "age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)

print "here is a puzzle"
# yus you can nest!!! store result of several functions in a single variable
what = add( age, subtract(height, multiply(weight, divide(iq,2))))
print "that is: ", what, "check it."




