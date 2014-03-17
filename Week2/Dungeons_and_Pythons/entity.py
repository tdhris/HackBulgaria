import weapon

class Entity():
	"""docstring for Entity"""

	def __init__(self, name, health):
		self.name = name
		self.health = health

		#creating default 'weapon'
		bare_hands = weapon.Weapon("bare hands", 2, 0)
		self.weapon = bare_hands

	def get_health(self):
		return self.health

	def is_alive(self):
		if self.health <= 0:
			return False
		return True

	def take_damage(self, damage):
		if damage > self.health:
			self.health = 0
			return False
		self.health -= damage
		return True

	def take_healing(self, healing_points):
		if healing_points > (100 - self.health):
			self.health = 100
			return False
		self.health += healing_points
		return True
 
	def has_weapon(self):
		return self.weapon.type != "bare hands"

	def equip_weapon(self, weapon_for_equipment):
		if not isinstance(weapon_for_equipment, weapon.Weapon):
			return False
		self.weapon = weapon_for_equipment
		return True

	def attack(self):
		if not self.has_weapon():
			return 0
		else:
			return self.weapon.damage


class Orc(Entity):
	"""docstring for Orc"""
	def __init__(self, name, health, berserk_factor):
		super().__init__(name, health)
		if isinstance(berserk_factor, float) == False:
			berserk_factor = 1.0
		elif berserk_factor < 1.0:
			self.berserk_factor = 1.0
		elif berserk_factor > 2.0:
			self.berserk_factor = 2.0
		else:
			self.berserk_factor = berserk_factor

	def attack(self):
		return self.berserk_factor * (super().attack())


class Hero(Entity):
	def __init__(self, name, health, nickname):
		super().__init__(name, health)
		self.nickname = nickname

	def known_as(self):
		return self.name + " " + self.nickname

