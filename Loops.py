
x = 0
while x < 3:
    print("x is ", x)
    # x++ NOPE, not in Python
    x += 1
    if x == 3:
        break
else:  #  execute here IFF the while test ends the loop by evaluating false
    print("What's this")

print("finished the loop")

numbers = list(range(1, 20, 2))
print(numbers)

for n in numbers:   # anything that is "iterable"
    print(f"n is {n}")

names = {"Fred": "Jones", "Jim": "Smith"}
for first in names.keys():
    print(f"firstname: {first} has lastname {names[first]}")

for last in names.values():
    print(f"lastname {last}")

for entry in names.items():
    print(f"lastname {entry}")

for v in range(1, 10, 2):
    print(v)
