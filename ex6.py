# set variables with interger and string values using string formatting
x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those %s ." % (binary, do_not)

# print out string variables
print x
print y

# pass string variables again as strings
print "I said: %r." % x
print "I also said: '%s'." % y

# set more string variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# pass variables using string formatting
#this is going to pass "hilarious" thru je
print joke_evaluation % hilarious

# set more string variables
w = "this is the left side of ..."
e = "a string with a right side."

#string + string = string :)
print w + e 

# %r is good to use for debugging since it will show "raw data"

