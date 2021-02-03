
x = range(1, 10)

# this is a map operation :)
squares = [y ** 2 for y in x]
print(squares)

# filter like operation
squares = [y ** 2 for y in x if y % 2 == 0]
print(squares)

# flat map ish...
triangle = [ y for x in range(1, 5) for y in range(1, x) ]
print(triangle)