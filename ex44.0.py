# all about composition
# which one?? subjective to tackle reusable code
    # avoid multiple inheritance!
    # use composition to package code into modules that can be used in unrelated situations
    # use inheritance ONLY when there are clearly related pieces under a single common concept

class Other(object):
    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):
    # composition!
    def __init__(self):
        self.other = Other()

    # call composition methods
    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

# has-a
son = Child()

son.implicit()
son.override()
son.altered()
