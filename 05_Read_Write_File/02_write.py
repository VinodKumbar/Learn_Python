# Read mode is used to read the contents of a file.
# Write mode is used to write new content to a file.
# If the file already exists, it will be overwritten. If the file does not exist, it will be created.
# Write mode is denoted by 'w' and read mode is denoted by 'r'.
# When we open a file in write mode, we can use the write() method to write content to the file.
# The write() method takes a string as an argument and writes it to the file.
# We can also use the writelines() method to write a list of strings to the file.
# The writelines() method takes a list of strings as an argument and writes each string in the list to the file.
# Append mode is used to add new content to the end of an existing file without overwriting the existing content.
# Append mode is denoted by 'a'.



with open('testData.txt', 'r') as reader:
    content = reader.readlines()
    reversed_content = reversed(content)
    print(reversed_content)
with open('testData.txt', 'w') as writer:
    writer.write("Flying Fish.\n")
    writer.write("Giant Squid.\n")
    writer.write("Hammerhead Shark.\n")

with open('testData.txt', 'a') as appender:
    appender.write("Angelfish.\n")
    appender.write("Beluga Whale.\n")
    appender.write("Clownfish.\n")
    appender.write("Dolphin.\n")
    appender.write("Eel\n")