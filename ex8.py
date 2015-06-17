# create variable formatter - use %s more often
formatter = "%r %r %r %r"

# examples of ways to pass many different values through the same variables
# rather than explicitly redefining each variable or string
#integers
print formatter % (1, 2, 3, 4)
#strings
print formatter % ("one" , "two" , "three" , "four")
#booleans
print formatter % (True, False, False, True)

# what will this give us? just the original variable names!!!
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
	"i had this thing" ,
	"that you could type up right",
	"but it didn't sing.",
	"so I said goodnight."
	)
# double and single quotes with aposthropes to avoid confusion.