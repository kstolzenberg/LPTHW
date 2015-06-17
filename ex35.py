# branches and functions
from sys import exit

def gold_room():
	print "this room is full of gold. how much do you take?"

	choice = raw_input()
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("man learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("you greedy bastards")

def bear_room():
	print "there is a bear here."
	print "the bear has a bunch of honey"
	print "the fat bear is in front of another door."
	print "how are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")

		if choice == "take honey" :
			dead("the bear kills u")
		elif choice == "taunt bear" and not bear_moved:
			dead("the bear gets pissed off and chew you out")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means." # note you can stuck here!1

def cthulhu_room():
	print "here is cthulhu. do you flee for your life or eat ur head?"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why, "good jerb"
	exit(0)

def start():
	print "which door r/l do you take?"

	choice = raw_input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("you stumble around till u dead")

start()








