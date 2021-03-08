from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class Coordinate(Validator):
    def validate(self, value):
        if not 0 < value < 100:
            raise ValueError('invalid coordinate', value)


class Component:
    coordinate = Coordinate()

    def __init__(self, coordinate, value):
        self.coordinate = coordinate
        self.value = value


if __name__ == '__main__':
    c1 = Component(147, 200)