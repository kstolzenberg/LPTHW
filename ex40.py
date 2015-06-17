# python supports object-oriented programming
# modules, classes and objects
# python style: key = value/style/container ; be able to access info via the key

# working with modules
	# import example
	# example.method() -- access a method/function from the external module
	# example.variable -- access a variable from the external module
# a class is a way to group functions and data 
# when you create/instantiate a class = an object = building a copy of a thing
# getting things from things: list style, dict style, module-import stye, class style

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

# create variable to hold new song instance & pass lists as objects
# why wouldn't you pass the lyrics through the sing method variable?
happy_bday = Song([ "happy birday to you" , "i don't want to get sued" , "so ill stop right ther"])

bulls_on_parade = Song(["they rally around tha family", "with pockets full of shells"])

suzysong = ["wake up girl", "today is awake", "are u dreaming?"]
suzyq = Song(suzysong)

#call sing_me_a_song method on these objects (variables all passed)
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
suzyq.sing_me_a_song()


