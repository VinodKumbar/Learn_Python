# For loop
# A for loop is used to iterate over a sequence (like a list, tuple, string, etc.) or other iterable objects.
# It allows you to execute a block of code repeatedly for each item in the sequence.
print("Example 1: Iterating over a list")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


print ("# Example 2: Iterating over a string")
for char in "Hello":
    print(char)
# Output:
# H
# e
# l
# l
# o

print ("Example 3: Iterating over a tuple")
numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5
print (" Example 4: Using range() function to iterate over a sequence of numbers")
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

obj = [1, 2, 3, 4, 5]
for i in obj:
    print(" values of object are:  " + str(i))

# print in multiple of 2
for i in range(1, 11):
  #  print(i * 2)
    print("  : " + str(i) + " multiplied by 2 is: "+ str(i * 2))


# sum of first 10 natural numbers
total = 0
for i in range(1, 11):
    #total += i
    total = total + i
print("Sum of first 10 natural numbers is:", total)

# print number from 1 to 10 with step of 2
for k in range (1,10,2):
    print(k)
print ("Number from 1 to 10 with step of 2")

for l in range (10):
    print(l)
print ("Number from 0 to 9")

