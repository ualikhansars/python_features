class Health:
    def __get__(self, instance, owner):
        print('health', instance._health)
        return instance._health

    def __set__(self, instance, value):
        instance._health = value
        print('health', instance._health)

    def __delete__(self, instance):
        if instance.removable:
            del instance._health
            print('health been removed')
        else:
            print('cannot remove health')


class Unit3:
    def __init__(self, health):
        self._health = health
        self.removable = False

    health = Health()


class ReadOnly:
    def __get__(self, instance, owner):
        return instance.x

    def __set__(self, instance, value):
        raise AttributeError('cannot set')


class X:
    def __init__(self, x):
        self.x = x

    x = ReadOnly()


if __name__ == '__main__':
    print('Unit3')
    unit3 = Unit3(10)
    unit3.health = 120
    unit3.health
    unit3.health = 70
    unit3.health
