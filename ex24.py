# more review
# check ur functions have colons! 
# check your strings are in quotes

print "let's practice everything."
print "you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

poem = """
\t the lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n \t \t where there is none. 
"""

print "------"
print poem
print "------"

five = 10 - 2 + 3 - 6
print "this should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates # these variables are temporary!!!

start_point = 10000
beans, jars, crates = secret_formula(start_point) # again order matters here and you are only here defining the names!!

print "with a starting point of: %d" % start_point
print "we'd have %d beans, %d jars and %d crates" % (beans, jars, crates)

start_point = start_point / 10

print "we can also do it this way:"
print "we'd have %d beans, %d jars, %d crates" % secret_formula(start_point)

 	













