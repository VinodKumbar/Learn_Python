#Functions are reusable pieces of code that perform a specific task.
# They help to break down complex problems into smaller, more manageable parts, and they can be called multiple times throughout a program.



def GreetMe(name):
    print("Hello, " + name + " Welcome to Python programming!")


GreetMe("Vinod! ")  # Output: Hello, welcome to Python programming!

def AddNumbers(a, b):
    return a + b

result = AddNumbers(5, 10)
print("The sum is:", result)  # Output: The sum is: 15