# Constructor is a special method in Python that is automatically called when an object of a class is created.
# It is used to initialize the attributes of the class. The constructor method is defined using the `__init__` keyword.
# Self keyword is a reference to the current instance of the class.
# It is used to access the attributes and methods of the class.
# The self parameter is always the first parameter of the constructor method and is automatically passed by Python when an object is created.
# Constructor name should always be `__init__` and it should always take at least one parameter, which is `self`.


class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"

if __name__ == "__main__":
    obj = calculator(10, 5)  # syntax to create an object of a class with constructor
    print(obj.add()) # Output: 15
    print(obj.subtract()) # Output: 5
    print(obj.multiply()) # Output: 50
    print(obj.divide()) # Output: 2.0