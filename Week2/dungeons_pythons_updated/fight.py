from random import randint
from os import system
from time import sleep


class Fight():
    def __init__(self, hero, snake):
        self.hero = hero
        self.snake = snake

    def who_is_first(self):
        dice = randint(0, 100) % 2
        if dice:
            return self.hero
        else:
            return self.snake

    def get_opponent(self, attacker):
        if attacker == self.hero:
            return self.snake
        else:
            return self.hero

    def simulate_fight(self):
        attacker = self.who_is_first()
        opponent = self.get_opponent(attacker)

        while attacker.health > 0:
            system('clear')
            damage = attacker.attack()

            opponent.take_damage(damage)
            print("%s attacks. %s takes %i damage" % (attacker,
                                                      opponent,
                                                      damage))
            print("%s has %i health while %s has %i health \n" %
                 (attacker, attacker.get_health(),
                  opponent, opponent.get_health()))

            attacker = self.get_opponent(attacker)
            opponent = self.get_opponent(opponent)
            sleep(2)

        else:
            print("%s died" % str(attacker))
            sleep(2)

        return True
