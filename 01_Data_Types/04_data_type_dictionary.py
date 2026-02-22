# Dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed.
# Dictionaries are written with curly brackets, and they have keys and values.

values = {"name": "vinod", "age": 30, "city": "bangalore", 1: 9874563210}
print(values)
print(type(values))

#print only name
print(values["name"]) #vinod
#print(values[4]) # This will raise a KeyError because there is no key '4' in the dictionary.
print(values[1]) #9874563210

print ("************************************************************************************************")
# create a dictionary dynamically

my_dict = {}
my_dict["name"] = "vinod"
my_dict["age"] = 30
my_dict["city"] = "bangalore"
print(my_dict)