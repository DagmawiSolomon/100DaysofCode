def add(*args):
    print(sum(args))


add(1,8,84,776,44)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')


my_car = Car(make="BMW", model="GWAGON")

