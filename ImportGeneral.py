def print_this(this_shit='the Thing'):
    print(this_shit)


def hi():
    print('hi')


wheels = 4


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print('Im driving a ' + self.model)

    def stop(self):
        print('I stop a ' + self.model)
