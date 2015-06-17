# to make a list of dicts, make an empty list and append each dict to the list
# to print each one:
	# for item in list:
	# 	print item['key'], item['key2']

stuff = {'name' : 'kron', 'age': 28, 'height' : 45+34/2} #dicts use curly brackets

print stuff['name'] # access the values through the strings. won't print multiples tho?
print stuff['age']
print stuff['height']

stuff['city'] = "san francisco" # add key and value to dict

print stuff['city']

stuff[1] = "wow"
print stuff # if you print the dict out, it will return in alphabetical order by keys?
del stuff[1] # take stuff out
print stuff


stuff2 = [{'name' : 'kron', 'age': 28, 'height' : 45+34/2}, {'name' : 'tato', 'age': 33, 'height' : 42}] 
# this throws

for item in stuff2:
	print item # this print each whole dict in the list
	print item["name"] # this print each "name": value in the list.
	# remember when you iterate through lists - can step through index or can just step through items