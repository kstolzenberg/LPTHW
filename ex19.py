#more functions and variables

def cheese_and_crackers (cheese_count, boxes_of_crackers):
	print "you have %d cheeses!" % cheese_count
	print "you have %d boxes of crackers" % boxes_of_crackers
	print "man thats enough for a party!!"
	print "yo get a blanket.\n" # new line after function helps with formatting!

print "we can give the function numbers directly!"
cheese_and_crackers(20,30)

print "or we can use variables from our script "
amount_of_cheese = 10
amount_of_crackers = 35
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can even do math inside too:"
cheese_and_crackers(10+5, 3+9)

print "and we can combine the two, variables and math!"
cheese_and_crackers(amount_of_cheese +10, amount_of_crackers * 2)

response1 = int(raw_input("you tell me \n"))
response2 = int(raw_input("and what else? \n"))
cheese_and_crackers(response1/4, response2/6)