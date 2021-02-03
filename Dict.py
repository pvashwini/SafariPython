names = {"Fred": "Jones", "Jim": "Smith"}
# print(names, type(names), sep="++++", end="That's all folks!")
# print(names, type(names), sep="++++", end="")
# print("X")
print(names)
print(names["Fred"])
# print(names["Freddy"])  #  non-existent throws exception...
print(names.values())
print(names.items())  #  key/value pairs in "tuples"
print(names.keys())
print("Fred" in names)  #  tests for does this key exist...

names = {"Fred", "Jim", "Sheila"}
print(names, type(names))
