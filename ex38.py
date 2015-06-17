# doing things to lists
# intros to data structures! how to organize data to access in different ways
# lists as a deck of cards example, they are ordered and have indicies
# when to use lists


ten_things = "apples oranges crows telephones light sugar" # a simple string

print "wait there are not 10 things in that list. let's fix that.\n"

stuff = ten_things.split(' ') # split = string method returns a list of words with the given separator
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"] # a new list of strings

while len(stuff) != 10:
	next_one = more_stuff.pop() # default i = -1; so [-1] (last one) is selected, deleted and returned
	print "adding: ", next_one # concat works if at the end - no need for string formatters
	stuff.append(next_one) # add the popped string to the original string
	print "there are %d items now." % len(stuff)

print "\nthere we go: ", stuff # this should be + boy, girl, banana, corn

print "lets do somethings with stuff."

print stuff[1] # 2nd position
print stuff[-1] # last position
print stuff.pop() # splice and return last one
print ' '.join(stuff) # joins a list or tuple at separators
print '#'.join(stuff[3:5]) # from x-y join with "#"