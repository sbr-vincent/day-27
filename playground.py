def add(*args):
    total = 0
    for num in args:
        total += num

    print(total)


add(5, 3, 5)


# **kwargs will be a dictionary
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(add=3, multiply=5)

# .get() allows us to not put in arguments when calling the class
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)

