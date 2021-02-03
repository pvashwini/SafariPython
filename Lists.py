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
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
print(numbers[3])
print(numbers[1 : 7 : 2]) # 1st inclusive, 2nd is exclusive ("fence"), 3rd "stride"
print(numbers[::-1])
print(numbers[:5:-2])
print(numbers[:-2:])

# r = range(0, 10)
r = range(1, 10, 2)
print(r)
print(list(r))


#   pythonic -- good, expected, python style
