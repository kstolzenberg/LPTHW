# new game from scratch

print "this is a new gyme. what do you want to play?"

play = raw_input("..?")

if play != "kittens" or play >= 15:
	print "ok now we are cooking with gas"
	what = raw_input("what are we cooking? ")

	if what == "meat" or what == "bean":
		print "yah i can smell it"
	else: 
		print "time for groceries"

else:
	print "pet that cat!"

