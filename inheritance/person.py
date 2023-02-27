class Person:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
