# Adding terminal input! and then passing it through a string!

# why the comma? = respond on same line
# %s will be a clean string vs %r will be in single quotes.

print "how old are you?",
age = raw_input()
print "how tall are you?",
height = raw_input()
print "how much do you weigh?" ,
weight = raw_input()

print "so, you are %s old , %s tall and %s heavy." % (age, height, weight)

# my own form
# dope! you can put the prompt in the function
# blue = built in function!
realtalk = raw_input('how is your day?'),
print "I guess it was %s" % realtalk
