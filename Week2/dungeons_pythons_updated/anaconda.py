from python import Python
from random import randint, uniform

MIN_ATTACKS = 3
MAX_ATTACKS = 10
MIN_BERSERK_FACTOR = 3
MAX_BERSERK_FACTOR = 10


class Anaconda(Python):
    def __init__(self, health):
        super().__init__(health)
        self.attacks_necessary = randint(MIN_ATTACKS, MAX_ATTACKS)
        self.berserk_factor = uniform(MIN_BERSERK_FACTOR, MAX_BERSERK_FACTOR)
        self.attack_count = 0

    def __repr__(self):
        return self.name + ' the ANACONDA'

    def attack(self):
        if self.attack_count < self.attacks_necessary:
            return self.damage
        elif self.attack_count == self.attacks_necessary:
            self.attack_count = 0
            return self.damage * self.berserk_factor
        else:
            return False
