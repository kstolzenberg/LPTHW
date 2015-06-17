my_name = 'krobe'
my_age = 28
my_height = 64
my_weight = 130
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'
to_kilo = 0.453592
to_cent = 2.54
unit = 'centimeters'
unit2 = "kilos"

# oo %xxx are conversion types = string variable and %d = "signed integer decimal"
# % is the string format operator
# to perform operations on string variables, pass the data type and do the operation in the parentheses. line 23 is passing the examples twice.
print "let's talk about %s" % my_name
print "he's %d %s tall" % (my_height * to_cent, unit)
print "she's %d %s light" % (my_weight * to_kilo, unit2)
print "actually thats not so bad"
print "she's got %s eyes and %s hair" % (my_eyes, my_hair)
print "her teeth are usuall %s depending on the coffee" % my_teeth

print "if i add %r, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height  + my_weight)


# multiple formats in ur string go in parentheses separated by commas.