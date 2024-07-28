class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
emp1 = Employee("Sam", 36)
emp2 = Employee("Mark", 28)
 
del emp1.name  # Deleted object's property
del emp2  # Object deleted