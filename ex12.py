# more on raw input and prompts!!!
# note terminal help: pydoc "function" will give you documentation! :)
# pydoc automatically!! generates documenattion

# like last time, you can stash prompts in the () of the raw_input
# note that print is a keyword not a function? like import

#function with string "" prompt that stores the response in a variable "age"
age = raw_input("how old are you? ")
height = raw_input("how tall are you? ")
weight = raw_input("how much do you weigh? ")

#print out formatted string.
print "so you are %s old, %s tall and %s heavy." % (age, height, weight)