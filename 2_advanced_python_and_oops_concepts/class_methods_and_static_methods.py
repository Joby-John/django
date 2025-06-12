# =========================
# CLASS METHOD EXAMPLE
# =========================
# Class methods are used to modify or access class-level attributes.
# Defined using @classmethod and take 'cls' (the class) as the first parameter.

class Employee:
    # Class attribute shared by all instances
    compName = "Google"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    @classmethod
    def changeCompName(cls, newName):
        # Modifies the class attribute for all instances
        cls.compName = newName

    def printDetails(self):
        # Prints instance and class attributes
        print(f"Company Name: {self.compName}")  # or Employee.compName
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Creating an instance
e1 = Employee("Joby", 28)

# Printing original details (Company = Google)
e1.printDetails()

# Changing company name using class method
Employee.changeCompName("Amazon")

# Printing updated details (Company = Amazon)
e1.printDetails()


# =========================
# STATIC METHOD EXAMPLE
# =========================
# Static methods are utility functions within a class.
# Defined using @staticmethod and do not take 'self' or 'cls'.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def isAdult(age):
        # Utility function that checks if age is above 17
        print(age > 17)

# Creating a Person instance (not required to use static method)
p1 = Person("Joby", 27)

# Using static method via class
Person.isAdult(17)  # Output: False

# Optional: Using static method via instance
p1.isAdult(20)      # Output: True
