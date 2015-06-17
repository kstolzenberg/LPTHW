# inheritance vs composition. be careful with inheritance.
# inheritance = one class will get most of its features from a parent class.
    # class foo(bar) == a new foo that inherits from bar
    # 3 ways of interaction: actions on the child imply action on the parent, actions on child override action on the parent, actions on the child alter the actions on the parent.


# implicit inheritance - handy for repetitive code
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

# make a new instance of parent called child
class Child(Parent):
    pass

# new instance of parent
dad = Parent()
# son instance inherits parent
son = Child()

# method of parent
dad.implicit()
son.implicit()

print "-" * 10

# override explicitly - sometimes you want the child to behave differently
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"
    def override(self):
        print "parent override()"

class Child(Parent):
    def override(self):
        print "child override()"

# make the objects 
dad = Parent()
son = Child ()
# call the methods
dad.override()
son.override()
son.implicit()

print "-" * 10

# alter before and after == super == will acces the parent version
class Parent(object):
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

print "-" * 10

class Parent(object):
    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()

# super is most commonly used with initializing
print "-" * 10

# composition










