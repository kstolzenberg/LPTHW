# escape sequences
# \t = tabbed in 
# \n = split line
# \t* = list with bullets
# \\ helps with difficult to to type characters.
# help to separate strings types from punctuation.


#set ur variables
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\n on a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# functions
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#note triple quotes are not commnets - they are multiline strings!
'''while True :
	for i in ["/" , "-", "|", "\\", "|"]:
		print "%s\r" % i,
# ? should equal = /\/, -\-, |\|, \\\, |\|
# that crashed! no boolean to stop true?'''
	