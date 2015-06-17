# learning how to speak "object-oriented"
	# class = make a new type of thing
	# object = the most basic type of thing AND any instance of a thing
	# instance = what you get when you initialize a class
	# def = define a function inside a class ClassName(object):
	

class x(y)
	make a class named x that is-a y

class x(object): def__init__(self, j)
	class x has-a def__init__ that takes self and j parameters

class x(object): def M(self, j)
	class x has-a function M that takes self and j parameters

foo = x()
	set foo to an instance of class x

foo.m(j)
	from foo get function m and pass self, j parameters

foo.k = q
	from foo get variable k and set to q

