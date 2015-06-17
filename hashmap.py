# hashmap - mapping one thing to another
# this is the amount of code you would need to do this same operation with lists!

def new(num_buckets=256):
	"""creates a map with the given number of buckets."""
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([]) # make an empty 2D list
	return aMap

def hash_key(aMap, key):
	"""given a key, create a number and make an index for the aMap buckets"""
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]

def get_slot(aMap, key, default=None):
	"""
	returns the index, key and value of a slot found in a bucket.
	returns -1, key, default when not found.
	"""
	bucket = get_bucket(aMap, key)

	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v

	return -1, key, default

def get(aMap, key, default=None):
	"""gets the value in a bucket for the given key or the default"""
	i, k, v = get_slot(aMap, key, default=default)
	return v

def set(aMap, key, value):
	"""sets the key to the value, replacing any existing value."""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)

	if i >= 0;
		# the key exists, replace it
		bucket[i] = (key, value)
	else:
		# the key does not, append to create it
		bucket.append((key, value))

def delete(aMap, key):
	"""deletes the given key from the Map."""
	bucket = get_bucket(aMap, key)

	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break

def list(aMap):
	"""prints out what is the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v













