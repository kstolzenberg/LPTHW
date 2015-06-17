# else and if statements
# handling lists, objects and types are still the most difficult!
# ifs create a 'branch' - if true do it, otherwise skip it
# python expects indents after a colon : ! = a block of code
	# but! elifs and elses dedent
	# else = all other conditions
	# elif = else if some other conditions

people = 30 
cars = 40 
trucks = 15

if cars > people < trucks:
	print "we shuld take the cars"
elif cars < people:
	print "we should not** take the cars"
else:
	print "we can't decide :<"

if trucks > cars:
	print "thats toooo many trucks"
elif trucks < cars:
	print "maybe we take those trucks?"
else:
	print "we still can't decide"

if people > trucks > trucks:
	print "alright let's just take the trucks"
else:
	print "fine let's stay home them"