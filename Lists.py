names = ["Jim", "Fred", "Sheila"]
print(names)
print(names[0])
names[0] = "Frederick"  #  Lists are mutable
print(names)
names.sort()  #  "Natural" order, defined by __gt__ etc.
print(names)
names.sort(reverse=True)
names.sort(key=lambda s: len(s))
print(names)

# slicing:
