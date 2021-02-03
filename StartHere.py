print('"Hello"')
x = "Hello"
print(x)
print(type(x))

x = 3.1415926

print(x)
print(f"The value of pi is {x:5.2f}")
print(type(x))  #  float are IEEE 754 64 bin float numbers

x = 10000000
print(x)
print(type(x))
x = x * 10000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(x)

print(10 ** 2)

print("Hello" + " world")
print("x is " + str(x)) #  concatenation of string ONLY for string

x = "123"
y = 100
print(int(x) + y)

x = 123
print(x / y) #  floating point division with /
print(x // y) #  integer division with //
print(x % -y)

x += 100
print(x)

print(x := 100) # "Walrus operator" assignment but an expression with the assigned value

print(x == 100)
print(True)
print(type(True))
print(bool(x))
print(bool("Hello"))
print(bool("")) #  python has a "truthiness" concept

print(x != 100)
x = "Hello"
y = "He"
print(x == y)
y += "llo"
print(x == y)  # "content comparison" (defined by __eq__(self, other) "dunder" methods)

print(x is y) #  object identity (cannot extend/override)
y = "Hello"
print(x == y)
print(x is y) #  string literals are pooled, strings are immutable :)

# print(3 is 3)  # works but warning
print("Done")

x = 3 + 1j

print(x, type(x))
print(1j, (1j ** 2))

yes = True
no = False
print(yes and no)
print(yes or no)

#  bitwise operations!!! (work on bool, but not really the rigth thing!)
print(yes & no)
print(yes | no)
