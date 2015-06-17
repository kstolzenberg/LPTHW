# more file handling!!

from sys import argv
# import boolean module
from os.path import exists

script, from_file, to_file = argv

# make ur test files in CLI: touch name.txt
# add text: echo "..." > name.txt
# stream it back to CLI: cat name.txt

print ("Copying from %s to %s" % (from_file, to_file))

in_file = open(from_file)
indata = in_file.read()
# could you combine like this? - no bc we call in_file elsewhere!
# indata = (open(from_file)).read() 

print "the input file is %d bytes long" % len(indata)
print "does the output file exist? %r" % exists(to_file) # boolean
print "ready, hit RETURN to contine, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "alright, all done"

out_file.close()
in_file.close()