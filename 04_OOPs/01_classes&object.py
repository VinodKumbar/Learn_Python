# Classes and Objects in Python
#Class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
# Object is an instance of a class. It is created from a class and has the attributes and methods defined in the class.


class calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

obj = calculator()                      # syntax to create an object of a class
obj.add(1, 2) # Output: 3
obj.subtract(5, 3) # Output: 2
obj.multiply(4, 6) # Output: 24
obj.divide(10, 2) # Output: 5.0
obj.divide(10, 0) # Output: "Cannot divide by zero"

# In the above code, we have defined a class called "calculator" with four methods: add, subtract, multiply, and divide.
# We then created an object of the class and called each method with different arguments to perform the respective operations.

#print

print(obj.add(1, 2))
print(obj.subtract(5, 3))
print(obj.multiply(4, 6))
print(obj.divide(10, 2))
print(obj.divide(10, 0))
