#44 Composition
#accomplishes what 44_inheritance.py does, but without inheritance
class Other(object):    #called Other because it is no longer a parent class

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):         #asserts its self
        self.other = Other()    #but gets attributes from Other

    def implicit(self):         #defines the implicit method
        self.other.implicit()   #whose attributes it gets from Other

    def override(self):         #has its own override method
        print("CHILD override()")

    def altered(self):          #has its own altered method
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

other = Other()
son = Child()

son.implicit()
other.override()
son.override()
son.altered()
