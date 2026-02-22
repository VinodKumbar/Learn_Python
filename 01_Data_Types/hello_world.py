print ("Welcome Home")

# This is a comment. It is not executed by the computer. It is used to explain the code to humans.
# The print() function is used to display a message on the screen. In this case, it will display "Welcome Home".

print("Happy Learning Python")

print ("***************************************************")
# Variables are used to store data. They can be used to store numbers, text, and other types of data.
# In Python, you can create a variable by assigning a value to it using the equals sign (=).

a = 3
b = 4
c = a + b

print("Addition of {} and {} is: {}".format(a, b, c))
# In this example, we have created three variables: a, b, and c.
# We assigned the value 3 to a, the value 4 to b, and the sum of a and b to c.
# The print() function is then used to display the result of the addition.
# The format() function is used to format the string.
# It allows you to insert values into a string using placeholders.
# In this case, we have used {} as placeholders for the values of a, b, and c.
# The format() function replaces the placeholders with the actual values of a, b, and c when the string is printed.


print ("***************************************************")


Str = "Hello, World!"
print(Str)

# In Python, you can use the type() function to check the data type of a variable.
print(type(a))  # Output: <class 'int'>
print(type(Str))  # Output: <class 'str'>

print ("***************************************************")
x, y, z = 5, 3.3, "Hello"
print(x)  # Output: 5
print(y)  # Output: 3.3
print(z)  # Output: Hello

print (type(x))
print (type(y))
print (type(z))

#type() function is used to check the data type of a variable.
# In this example, we have three variables: x, y, and z. We assigned the value 5 to x, the value 3.3 to y, and the string "Hello" to z.
# The type() function is then used to check the data type of each variable.

# In Python, you can also use the input() function to get user input.
# The input() function takes a string as an argument, which is displayed as a prompt to the user.
# The user's input is then returned as a string.
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Concatenate is not supported between different data types.
# You cannot concatenate a string and an integer directly.
# You need to convert the integer to a string first using the str() function.
age = input("Enter your age: ")
print("You are " + age + " years old.")


