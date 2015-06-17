# how to read from a file without hardcoding the file name! use user input!
# slower/less efficient to only use raw_input

from sys import argv

# where do you find all the available values to access through argv?
script, filename = argv

#open file, store in txt, later read that txt
txt = open(filename)

# print a string with the username of 'filename'
print "here is your file %s" % filename
# print the info in txt
print txt.read()

#prompt for more user input
print "type the filename again: "
# store user input in 'file_again'
file_again = raw_input("> ")

# open the 'file_again' file & store in new variable
txt_again = open(file_again)

# print new variable txt after reading 
print txt_again.read()

# imp to close when you are done!!!!!!
txt_again.close()
txt.close()




