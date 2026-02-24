file = open ('testData.txt')

readFile = file.read()
print(readFile)
print("After reading the file, the file pointer is at position: ", file.seek(0))

readchar = file.read(3)
print(readchar)
print("After reading the file, the file pointer is at position: ", file.seek(0))

readline2 = file.readline()
readline3 = file.readline()

print(readline2)
print(readline3)

file.close()

#Difference between read() and readline() method is that
# read() method reads the entire file and returns it as a string,
# while readline() method reads one line at a time and returns it as a string.
# readlines() method reads the entire file and returns it as a list of strings, where each string is a line in the file.


#Print line by line using a readline() method in a loop
file = open ('testData.txt')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
print("After reading the file, the file pointer is at position: ", file.seek(0))
file.close()



#Print line by line using readlines() method , get into list and print each line using a loop
file = open ('testData.txt')
lines = file.readlines()
for line in lines:
    print(line)
file.close()