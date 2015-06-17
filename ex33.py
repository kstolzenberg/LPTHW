# danger zone - the while loop. always make an escape!
# while == true, the code will execute. usually a for-loop is better!
# in python - colons make the code block!!!

def looper(var, increment):

	i = 0 # while has to start someplace!
	numbers = []

	while i < var:
		print "at the top i is %d" % i
		numbers.append(i)

		i = i + increment # loop will stop when i = 5
		print "numbers now: " , numbers
		print "at the bottom i is %d" % i 

	print "the numbers: "

	for num in numbers:
		print num 

#looper(10,2)

#rewritten with for loops and range - wayyyy more efficient!
def looper2(var, increment):
	numbers = range(0, var, increment)
	for num in numbers:
		print num

looper2(20,2)