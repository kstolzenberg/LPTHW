# moar functions

# import your modules
from sys import argv

script, input_file = argv

# keep all ur functions together
# need to open files before you can read
def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

# set variables
current_file = open(input_file)

# call functions
print "first let's print the whole file:"
print_all(current_file)

# this didn't do anything? if we comment this, the lines below don't get read?
print "now let's rewind, kind of like a tape."
rewind(current_file)

print "let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

# += add assign, there is no ++ bc they don't like it.
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)



