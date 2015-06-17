## Objects

# is-a
class Dog(Animal):
	def __init__(self, name):
		# has-a
		self.name = name

# is-a
class Cat(Animal):
	def __init__(self, name):
		#has-a
		self.name = name

# is-a
class Person(object):
	def  __init__(self, name):
		#has-a
		self.name = name
		self.pet = None

# is-a
class Employee(person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		# has-a
		self.salary = salary

# is-a
class Fish(object):
	pass

# is-a
class Salmon(Fish):
	pass

# rover is-a dog
rover = Dog("Rover")

# satan is-a cat
satan = Cat("Satan")

# mary is-a person
mary = person("mary")

# mary has-a pet named satan. satan is-a cat
mary.pet = satan

# frank is-a employee has-a 120000 salary
frank = Employee("Frank", 120000)

# frank has-a pet named rover. rover is-a dog
# has-a = composition
# is-a = inheritance
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a salmon is-a fish
croush = salmon()

# harry is-a halibut is-a fish
harry = Halibut()









