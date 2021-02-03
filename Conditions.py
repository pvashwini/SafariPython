from random import random
print(random())

# import random
# print(random.random())

x = random()

print(x)
#  indentation is KING
# if x > 0.5:
#     print("It's big")
#     print("yeah, like more than half")
# else:
#     if x > 0.7:
#         print("Really Really big")
#     else:
#         print("small and insignificant")

if x > 0.7:
    print("It's big")
    print("Really Really big")
elif x > 0.5:  #  controls indentation runaway!
    print("more than half")
else:
    print("small and insignificant")

print("if is finished...")

y = "Hello" if x > 0.5 else "goodbye"
print(y)

#  not very pythonic ;) 
if x > 0.5: print("it's big"); print("yeah, I mean it")

#  python does NOT have switch/case...
#  fudges exist, often using dict
