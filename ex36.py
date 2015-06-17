# designing and debugging
# all if statements need to have an else! 
# if else never needs to go = die()
# never nest more than two if statements deep
# if booleans are getting trickier, store them in a variable
# use while when you want to loop forever
# use for-loop for fixed looping or a limited number of iterations

response = raw_input("are you hungo?? \n")

if response != "no" :

	gauge = raw_input("how hungo are you? \n")

	if "very" in gauge or "so" in gauge:
		food_picks = []
		food_picks = raw_input("well what do you want? \n")
		print "ok here is your grocery list: %s " % food_picks	

	else:
		print "maybe u should drink some water"

else:
	print "well bully for you :p"