# List is a collection of items which are ordered and changeable. It allows duplicate members.

values = [1, 2, "vinod", 3.14, True]
print(values)
print(type(values))

print(values[0]) #1
print(values[2]) #vinod
print(values[-1]) #True
print(values[1:3]) #[2, 'vinod']

values.insert(3, "kumbar") # add value at index 3
print(values)
values[1] = 20  # add or update value in list
print(values)

values.append("python") # add value at end of list
print(values)

values[2] = "Vinod Kumbar" # update value at index 2

values.append("python")
del values[3] # delete value at index 3
print(values)