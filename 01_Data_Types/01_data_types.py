# Python Data Types
# 1. Numeric Types: int, float, complex
# 2. Sequence Types: list, tuple, range
# 3. Text Type: str
# 4. Mapping Type: dict
# 5. Set Types: set, frozenset
# 6. Boolean Type: bool
# 7. Binary Types: bytes, bytearray, memoryview

# Numeric Types
a = 10  # int
b = 3.14  # float
c = 2 + 3j  # complex
print(a, type(a))  # Output: <class 'int'>
print(b, type(b))  # Output: <class 'float'>
print(c, type(c))  # Output: <class 'complex'>

#Sequence Types
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# difference between list and tuple is that list is mutable (can be changed) while tuple is immutable (cannot be changed).

my_range = range(1, 6)
print(my_list, type(my_list))  # Output: <class 'list'>
print(my_tuple, type(my_tuple))  # Output: <class 'tuple'>
print(my_range, type(my_range))  # Output: <class 'range'>

# Text Type
my_string = "Hello, World!"
print(my_string, type(my_string))  # Output: <class 'str'>

# Mapping Type
my_dict = {"name": "Alice", "age": 30}
print(my_dict, type(my_dict))  # Output: <class 'dict'>

# Set Types
my_set = {1, 2, 3, 4, 5}
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_set, type(my_set))  # Output: <class 'set'>
print(my_frozenset, type(my_frozenset))  # Output: <class 'frozenset'>
# Difference between set and frozenset is that set is mutable (can be changed) while frozenset is immutable (cannot be changed).

# Boolean Type
is_true = True
is_false = False
print(is_true, type(is_true))  # Output: <class 'bool'>
print(is_false, type(is_false))  # Output: <class 'bool'>

# Binary_Types
# Binary types are used to store binary data, such as images, audio, and video files.
# They are also used to store data that is not human-readable, such as encrypted data or compressed data.
my_bytes = b"Hello, World!"
my_bytearray = bytearray(b"Hello, World!")
my_memory = memoryview(b"Hello, World!")
print(type(my_bytes))  # Output: <class 'bytes'>
print(type(my_bytearray))  # Output: <class 'bytearray'>
print(type(my_memory))  # Output: <class 'memoryview'>



