
# def add(a, b):
#     print(a + b)
#     # return None

## extensions can parse / verify type correctness if specified
## underlying language ignores these "annotations" / type-hints
# def add(a : int, b : int) -> int:
def add(a, b):
    return a + b

x = 10
y = 20
# print(add(x, y))  # None is "undefined", null
print(add(x, y))
print(add("Hello", " world"))

def dayOfWeek(day, month, year):
    # Right hand side are "tuples" parens are optional...
    # left hand side is "destructuring assignment" (other destructurings exist...)
    m, y = (month, year) if month > 2 else (month + 12, year - 1)
    ##  oops, function isn't working, not going to bother to fix
    ## check out "Zeller's congruence"
    return (day + (13 * (m + 1) // 5) + y + y // 4 - y // 100 + y // 400) % 7
    # my mistake was dividing by "y"... should be divided by 5. Finger trouble :(
    # return (day + (13 * (m + 1) // y) + y + y // 4 - y // 100 + y // 400) % 7

def showCount(c = 100):
    print(f"count is {c}")

print(f"day of Jan 1, 2000 was {dayOfWeek(1, 1, 2000)}")
print(f"day of Feb 11, 2021 is {dayOfWeek(month=2, day=11, year=2021)}")

showCount(99)
showCount()

def show_allsorts(a, b, *args, **kwargs):
    print(f"a is {a}, b is {b}")
    for arg in args:
        print(f"arg is {arg}")
    for k,v in kwargs.items():
        print(f"{k} has value {v}")


show_allsorts(1, 3, "hello", "banana", 99.9, name="Fred", origin="Planet Earth")

names = [1, 2, "Fred", "Jim", "Sheila"]
show_allsorts(*names)

day_names = ["Saturday", "Sunday", "Monday"]
def day_name(d):
    if (d < 0 or d > 7):
        raise IndexError(f"{d} is not a valid day number")
    return day_names[d]

print(f"The name of day zero is {day_name(0)}")
try:
    print("calculating day number")
    from random import random
    if random() > 0.5:
        raise RuntimeError("Bad random value")
    day_num = int(random() * 8)
    print(f"The name of day number is {day_name(day_num)}")
    print("wasn't that clever")
except IndexError as ie:
    print(f"oops that broke with {ie}")
except:
    print("somethign else (potentially really bad!) broke")
finally:
    print("all done")

