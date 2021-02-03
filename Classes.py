class Date:
    @staticmethod
    def isLeap(year):
        return year % 4 == 0  # plus more logic

    #  self is "this" in many other languages
    #  explicit in argument list, not optional!!!
    def __init__(self, d, m, y):
        #  no "class field declaration" just add fields
        # self prefix is NOT OPTIONAL (c.f. javascript)
        self.day = d
        self.month = m
        self.year = y
        # a = 99 # kinda static variable

    def __str__(self):
        return f"Date with day = {self.day}"

    def __repr__(self):
        return self.__str__()

    def show_me(self):
        # write an instance method using self!
        print(f"hello, from an instance of date with day = {self.day}")

class Holiday(Date):  # subclass
    def __init__(self, d, m, y, n):
        super().__init__(d, m, y)
        self.name = n

    def __str__(self):
        return f"Holiday {super().__str__()} a holiday named {self.name}"

print(f"1984 is leap? {Date.isLeap(1984)}")

today = Date(3, 2, 2021)
print(today, type(today))
print(today.day)

today.bad_value = "hahaha"
print(today.bad_value)
# no real "private" and can usually force items into an objec, like any map\

days =[today, today]
print(days)

today.show_me()

# print(today.a)

today = Holiday(1, 1, 2021, "New year's day")
print(today)
