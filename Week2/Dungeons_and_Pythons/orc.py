class Orc():
	"""docstring for Orc"""
	def __init__(self, name, health):
		self.name = name
		self.health = health

		if isinstance(berserk_factor, float) == False:
			berserk_factor = 1.0
		elif berserk_factor < 1.0:
			self.berserk_factor = 1.0
		elif berserk_factor > 2.0:
			self.berserk_factor = 2.0
		else:
			self.berserk_factorberserk_factor = berserk_factor

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
		