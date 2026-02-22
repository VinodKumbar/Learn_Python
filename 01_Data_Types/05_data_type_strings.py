# Strings are a sequence of characters. They are used to represent text data.
# In Python, strings are enclosed in either single quotes (' ') or double quotes (" ").
# You can also use triple quotes (''' ''' or """ """) to create multi-line strings.
# String Examples

str = "Hello, World!"  # Using double quotes
str1 = "Welcome to Python programming."  # Using double quotes
str2 = 'Python is great!'  # Using single quotes
str3 = '''This is a multi-line string.
It can span multiple lines.'''  # Using triple quotes
str4 = "Python"


print(str)  # Output: Hello, World!

print(str[1]) # Output: e

print(str[0:5])  # if you want substring in Python Output: Hello

print(str + " " + str1)  # Output: Hello, World! Welcome to Python programming. Concatenation of strings
print ("***********************************************************************************************")
# if str4 is in str then print "Found" else print "Not Found"
if str4 in str2:
    print("Python" + " " + "present in" + " " + str2)
else:    print("Python" + " " + "does not present in" + " " + str2)
print("if else condition completed Successfully")

print (str4 in str2) # Output: True substring check

var = str.split(" , ") # Output: ['Hello', ' World!'] split string into list of substrings based on delimiter
print(var)
print(var[0]) # Output: Hello

str5 = "  Great  "
print(str5.upper()) # Output: GREAT convert string to uppercase
print(str5.lower()) # Output: great convert string to lowercase
print(str5.capitalize()) # Output: Great capitalize first letter of string
print(str5.replace("Great", "Awesome")) # Output: Awesome replace substring with another substring
print(str5.replace("Great", "Awesome"))
print(str5.strip()) # Output: Great remove leading and trailing whitespace
print(str5.lstrip())
print(str5.rstrip())


