# Unlimited Positional Argument: By adding an asterisk '*' in front of a
# function parameter, all arguments passed into it will be turned into a
# tuple. By Python convention, we would name this parameter '*args'.
def add(*args):
    added = sum((arg for arg in args))
    return added


print(add(1, 2, 3))


# Unlimited Keyword Arguments: By added double asterisk '**' in front of a
# function parameter, all arguments passed into it will be turned into a
# dictionary. By Python convention, we would name this parameter either as
# '**kwargs' or '**kw'.
def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']

    return n


print(calculate(4, add=20, multiply=5))


class Car:

    def __init__(self, **kwargs):
        # dict.get() method works similarly to square brackets when
        # used to fetch values from a dictionary with keywords. The advantage
        # is that it won't raise an error if the keywords don't exist but it
        # will return a null value instead.
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')


my_car = Car(make='Nissan')
print(my_car.make, my_car.model)
