# reading and writing to a file
# make a simple text editor
#file.close, file.read, file.readline, file.truncate, file.write()

# note!! when you use ARGV you need to pass the variable when you run the command or else error!

# import our modules
from sys import argv

# set variables attached to argv
script, filename = argv

# pass user value to user question
print "we are going to erase %s" % filename
print "if you don't want that, hit CTRL-C (^C)."
print "if you do want that, hit RETURN"

# get user input 
raw_input("?")

# open the user-specified file, set open mode and store in a variable
print "opening the file..."
target = open(filename, 'w') 
# 'w' mode is writing, there is also r-reading (default) and a-appending - which only adds!!

# hmm it ran without this? what does this do? reduces file size
#this is actually redundant - not clear why this would be used
print "truncating the file! goodbai!"
target.truncate

print "now I am going to ask you for three lines"

#get user input to add file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write these to the file"

# write lines to file and separate each line with a newline
# string formatting inside a function needs to totally go inside the function!
target.write("%s \n %s \n %s" % (line1, line2, line3)) 

# close the file - why? docs say to free system resources. good practice to avoid open data.
print "and finally we close the file"
target.close()














