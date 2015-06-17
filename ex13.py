# more inputs and scripts!
# this is input when you run the script at the command line

# argv = argument variable :: variable that holds arguments to pass to script
# things that are imported are modules aka 'libraries'. modules give you features!

# when you run this script - you have also pass 3 values!!!
# == python ex13.py hotdog relish kraut >> then it correctly passes the 3 variables in the order you typed them!

from sys import argv

# 'unpacks' argv so there are 4 sep variables
script, first, second, third = argv
# here you will be prompted for input and then variable below is rewritten!
first = raw_input("which is this?")

print "the script is called: " , script
print "your first variable is " , first
print "your next variable is: " , second
print "your next variable is: " , third


