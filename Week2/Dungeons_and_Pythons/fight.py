import entity
import weapon
from random import randint

class Fight():
	def __init__(self, hero, orc):
		if isinstance(hero, entity.Hero) and isinstance(orc, entity.Orc):
			self.hero = hero
			self.orc = orc

	def who_is_first(self):
		dice = randint(0,100)%2
		if dice:
			return self.hero
		else:
			return self.orc

	def get_opponent(self, attacker):
		if attacker == self.hero:
			return self.orc
		else:
			return self.hero


	def simulate_fight(self):
		attacker = self.who_is_first()
		opponent = self.get_opponent(attacker)

		while attacker.health > 0:
			if attacker.weapon.critical_hit():
				damage = attacker.attack() * 2
				print("critical hit!!!!")
			else:
				damage = attacker.attack()

			opponent.take_damage(damage)
			print("%s attacks. %s takes %i damage" %(attacker.name, opponent.name, damage))
			print("%s has %i health while %s has %i health \n" % (attacker.name, attacker.health, opponent.name, opponent.health))

			attacker = self.get_opponent(attacker)
			opponent = self.get_opponent(opponent)
		else:
			print("%s died" % attacker.name)

		return True



