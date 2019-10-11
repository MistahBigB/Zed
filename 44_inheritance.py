#44 Inheritance

class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):    #creates child class, subclass of parent

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()    #call super with arguments Child and self, then call the function altered on whatever it returns
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()  #calls the implicit method in Parent
son.implicit()  #calls the implicit method in Parent, because Child does not  have an explicit implicit method

dad.override()  #calls the override method in Parent
son.override()  #calls the override method in Child, because Child has an explicit override method

dad.altered()   #calls the altered method in Parent
son.altered()   #calls the altered method in Child, because Child has an explicit altered function
