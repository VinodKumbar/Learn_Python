# Tuple is a collection which is ordered and unchangeable (Immutable). Allows duplicate members.
# Tuples doesnt support item assignment and methods like insert(), append(), remove() etc. It is faster than list because of immutability.

values = (1, 2, "vinod", 3.14, True)
print(values)
print(type(values))

values[2] = "VINOD" # This will raise a TypeError because tuples are immutable and do not support item assignment.
