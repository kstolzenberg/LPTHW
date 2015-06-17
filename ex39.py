# introduction to dictionaries
# also known as hashes
# uses string keys to access values - mapping or associating key values!
# this is valuable because it associates more info/more structure to the data - think of vimeo example...rather than a generic list of many types of info, dicts give structure about title, views, properties etc.
# more "computationally" efficient than array lookups...don't need to see everything, just check for key matches
# you can also assign values to numbers! and you can del certain values

# dict syntax == dict_name = {'key1':'value1', 'key2':'value2'} colons separate the key and values

# hashmap algorithms:
	# convert a key to an int using a hashing hash_key function
	# convert hash to a bucket number using %

# use a dict instead of list when:
	# data with identifiers - names, addresses, 
	# you don't need order
	# you are going to be adding and removing elements


# create a mapping of state to abbreviation
states = {
	"oregon" : 'or',
	'florida' : "fl",
	'california': "ca",
	"new york" : "ny",
	"michigan": "mi"
}

cities = {
	'ca' : "san francisco",
	'mi' : "detroit",
	"fl" : "jacksonville"
}

# add to cities these new values
cities["ny"] = "new york city"
cities["or"] = "portland"

print "-" * 10
print "ny state has: ", cities["ny"]
print "or state has: ", cities['or']

print "-" * 10
print "michigans abbreviation is : ", states["michigan"]
print "florida's abbreviation is : ", states["florida"]

print "-" * 10
print "michigan has: " , cities[states["michigan"]]
print "florida has: ", cities[states["florida"]]

print "-"* 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

print "-" * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

print "-" * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])


print "-" * 10
state = states.get('texas')

if not state:
	print "sorry no texas."

city = cities.get('tx', 'does not exist')
print "the city for the state 'tx' is: %s" % city


