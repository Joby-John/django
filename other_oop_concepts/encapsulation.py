# =========================
# ENCAPSULATION EXAMPLE
# =========================

class Student:
    def __init__(self, name, age):
        self.name = name            # public attribute — can be accessed directly
        self.__age = age            # private attribute — encapsulated (not accessible directly from outside)

        # Why encapsulation?
        # - Prevents direct access to sensitive data
        # - Allows validation before setting values
        # - Helps keep internal state safe and consistent

    # Getter method — used to access private attribute safely
    def get_age(self):
        return self.__age

        # Why use getter?
        # - Provides read-only access to the private attribute
        # - Can include logic (e.g., logging, formatting) before returning

    # Setter method — used to modify private attribute with control
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age! Age must be positive.")

        # Why use setter?
        # - Controls how the private attribute is updated
        # - Allows input validation to ensure data integrity

    # Public method to print all details
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.__age}")

# =========================
# USING THE CLASS
# =========================

# Creating an instance of Student
s1 = Student("Joby", 20)

# Accessing public attribute — works fine
print(s1.name)  # Output: Joby

# Trying to access private attribute directly will fail
# print(s1.__age)  # ❌ AttributeError: 'Student' object has no attribute '__age'

# Accessing private attribute via getter
print(s1.get_age())  # ✅ Output: 20

# Modifying private attribute via setter
s1.set_age(25)
print(s1.get_age())  # ✅ Output: 25

# Trying to set invalid age using setter — handled safely
s1.set_age(-10)  # ❌ Output: Invalid age! Age must be positive.

# Displaying all details using class method
s1.show_details()
