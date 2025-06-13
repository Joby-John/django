# Why Abstraction?
# - Enforces a common interface for all subclasses
# - Hides internal complexity (users only care about what to use, not how it works)
# - Improves modularity and maintainability

# Abstract class (Animal):
# - Cannot be instantiated directly
# - Defines method prototypes (abstract methods) that must be implemented by subclasses

# Concrete class (Dog, Cat):
# - Implements the abstract method
# - Can be instantiated and used normally


from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        # Abstract Method (just the prototype, no implementation)
        pass

    def breathe(self):
        print("Breathing...")  # Concrete method (fully defined)

# Concrete Class
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# animal = Animal()  # ❌ Error: Cannot instantiate abstract class
dog = Dog()
cat = Cat()

dog.make_sound()  # ✅ Output: Woof!
cat.make_sound()  # ✅ Output: Meow!
dog.breathe()     # ✅ Inherited concrete method


class Polygon(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def calcArea(self):
        pass

class Square(Polygon):
    def __init__(self, color, side1, side2):
        super().__init__(color)
        self.color = color
        self.side1 = side1
        self.side2 = side2

    def calcArea(self):
        print(self.side1 * self.side2)
        
# p1 = Polygon("Blue") cant call like this bc its an abstract class
s1 = Square("red", 4, 5)
s1.calcArea()
        