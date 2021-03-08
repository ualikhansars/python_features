class Unit:
    def __init__(self, health):
        self._health = health
        self.removable = False

    def get_health(self):
        print('health', self._health)
        return self._health

    def set_health(self, health):
        if 0 < health <= 100:
            self._health = health
            print('health is now set to', health)
        else:
            print('cannot set health')

    def del_health(self):
        if self.removable:
            del self._health
            print('health been removed')
        else:
            print('cannot remove health')

    health = property(get_health, set_health, del_health, 'health is important attribute')


class Unit2:
    def __init__(self, health):
        self._health = health
        self.removable = False

    @property
    def health(self):  # health = property(health)
        """health is important attribute"""
        print('health', self._health)
        return self._health

    @health.setter
    def health(self, health):  # health = health.setter(get_health)
        if 0 < health <= 100:
            self._health = health
            print('health is now set to', health)
        else:
            print('cannot set health')

    @health.deleter
    def health(self):  # health = health.deleter(del_health)
        if self.removable:
            del self._health
            print('health been removed')
        else:
            print('cannot remove health')


if __name__ == '__main__':
    unit = Unit(10)
    unit.health = 120
    unit.health
    unit.health = 70
    unit.health
    print(Unit.health.__doc__)

    print('Unit2')
    unit2 = Unit2(10)
    unit2.health = 120
    unit2.health
    unit2.health = 70
    unit2.health
    print(Unit2.health.__doc__)
