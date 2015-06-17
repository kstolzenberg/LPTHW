# printing exercises
# order matters! variables defined after expression can't be referenced
print "mary had a little lamb."
print "its fleece was white as %s" % "snow"
print "and everywhere that mary went."
print "." * 10 # what does this do? = make 10 . chars? yes true!

# assign char variables
end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# print strings
print end1 + end2 + end3 + end4 + end5 + end6, 
# comma creates non-breaking space! no comma = new line 
# python frowns on lines > 80 chars for readability = break it.
print end7 + end8 + end9 + end10 + end11 + end12

# can you rewrite to do in a for loop?