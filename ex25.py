# more practice!! 
# run once by running the file and once by importing into python
# notice nothing is getting called here - just defining many functions!!!
# if you run this directly in the shell, you can call var = filename.function(whatever)!!
# in python in the shell, if you run help(ex25), it will read back all top comments and the function names!
#  shortcut for imports
	# from ex25 import * == import everything!!! then you don't need to filename.function - just the function!!
	# python knows .py - no need to import the file with .py

def break_words(stuff):
	""" break up break_words""" # this is called a documentation comments!
	words = stuff.split(' ') # split at a space
	return words # returns list with each word in it! returns output!!!

def sort_words(words):
	return sorted(words)
	# returns a copy of the original list!!!
	# how does sorted method work? what is the default order?
	# default is numerically ascending..what about strings? should be alphbetical and case sensitive!

def print_first_word(words):
	word = words.pop(0) # at position 0, pops off just that one, removes from list
	print word

def print_last_word(words):
	word = words.pop(-1) # at position -1 (last!!!), select/pop just that one, removes it from list!
	print word

def sort_sentence(sentence):
	words = break_words(sentence) # nesting functions in functions!
	return sort_words(words)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence) # break words at space, sort words, store in words variableq
	print_first_word(words)
	print_last_word(words)












