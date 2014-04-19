from entity import Entity
from random import randrange

WEAK_ATTACK = 2
STRONG_ATTACK = 30
SNAKE_NAMES = ['Salazar', 'Ahktar', 'Kaa', 'Nagini',
               'Draco', 'Envy', 'Regulus']


class Python(Entity):
    def __init__(self, health):
        super().__init__(health)
        self.damage = randrange(WEAK_ATTACK, STRONG_ATTACK)
        self.name = SNAKE_NAMES[randrange(len(SNAKE_NAMES))]

    def __repr__(self):
        return '{0} the Python'.format(self.name)

    def attack(self):
        return self.damage
