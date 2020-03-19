class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        # A function that's part of a class is called a method.
        # The __init__() method is a special method that Python runs automatically whenever we create a new instance
        # based on the given class
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


# Making an Instance from a Class
my_dog = Dog('Willie', 6)
# Accessing Attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
# Calling Methods
my_dog.sit()
print("\n")
your_dog = Dog('Lucy', 4)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old")
your_dog.roll_over()
