# branching = decisions & user input via nested if loops.
# all that a game is a series of decisions and outcomes
# you need a condition to test for

print "you enter a dark room with two doors.  do you go through door #1, 2, 3, 4, 5"

door = raw_input("> ")

if door == "1":
	print "there's a giant bear here eating a cheese cake. what do you do?"
	print "1. take the cake."
	print "2. scream at the bear."

	# note: everything has to go someplace!
	bear = raw_input('> ')

	if bear == "1":
		print "the bear eats your face off. good job!"
	elif bear == "2":
		print "the bear eats your legs off. good jerb!"
	else:
		print "well doing %s is probably better. bear runs away." % bear

elif door == "2": 
	print "you state in to the endless abyss at cthulu's retina."
	print "1. blueberries"
	print "2. yellow jacket clothespins"
	print "3. understanding reolvers yelling melodies"

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "your body survives powered by a mind of jeloo. good jerb!"
	else:
		print "the insanity rots your eyes into a pool of mucj. good jerb."

elif door == "3":
	print "you mush be hungry - what do you want to eat"
	food_pref = raw_input("??")

	# rather than explicitly testing for truths, 'not' give you more options!
	if food_pref != "meat" and food_pref != "bones":
		print "ur a vegan thats why"
	elif food_pref == "bread":
		print "woah carbs"
	else:
		print "ok carry on."

else:
	print "you stumble around and fall on a knife and die. good herb."





