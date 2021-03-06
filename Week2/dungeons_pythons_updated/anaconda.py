from python import Python
from random import randint, uniform

MIN_ATTACKS = 3
MAX_ATTACKS = 10
MIN_BERSERK_FACTOR = 1.0
MAX_BERSERK_FACTOR = 2.0


class Anaconda(Python):
    def __init__(self, health):
        Python.__init__(self, health)
        self.attacks_necessary = randint(MIN_ATTACKS, MAX_ATTACKS)
        self.berserk_factor = uniform(MIN_BERSERK_FACTOR, MAX_BERSERK_FACTOR)
        self.attack_count = 0

    def __repr__(self):
        return self.name + ' the ANACONDA'

    def attack(self):
        self.attack_count += 1
        if self.attack_count < self.attacks_necessary:
            return self.damage
        elif self.attack_count == self.attacks_necessary:
            self.attack_count = 0
            return self.damage * self.berserk_factor
        else:
            return False
