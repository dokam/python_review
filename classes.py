class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello my first name is " + self.name)


p1 = Person("Douglas", 23)

print(p1.name)
p1.age = 32
print(p1.age)

# without str
print(p1)

print(p1.myfunc())

