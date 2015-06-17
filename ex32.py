# before you can use a for-loop - you need to be able to store the result of the loop!
# best way to store is with lists. no arrays in python - just lists are more general and can be multi-dimensional too!
# you don't declare anything in python you just use it!
# use a for-loop to build and print lists
# lists are ordered first to last and represented with []

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list:
for number in the_count:
	print "this is the count: %d" % number # you want it to be each list item subbed in!

for fruit in fruits:
	print "a fruit of type: %s" % fruit

for i in change:
	print "i got %r" % i

# build a list! start with an empty one and append things to it!
elements = []

#range will let us count....but to loop through a list you can say each item in list!
for i in range(0,6):
	print "adding %d to the list!" % i
	elements.append(i)

# ^ in lieu of this - you can just set elements = range(0,6)

print "---"
print elements # what does it look like to raw print a list?
# when you print a list - it prints brackets, commas, all - good for debug only
print "---"

# this will print each list item in a tidier way - no formatting!
for item in elements:
	print "element was: %d" % item

# this makes a list from index xe, < y
new_list = range (0,10)
print new_list







