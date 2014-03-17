class Hero():
	
	def __init__(self, name, nickname, health):
		self.name = name
		self.nickname = nickname
		self.health = health

	def known_as(self):
		return self.name + " " + self.nickname

	def get_health(self):
		return self.health

	def is_alive(self):
		if self.health <= 0:
			return False
		else:
			return True

	def take_damage(self, damage):
		if self.health < damage:
			self.health = 0
			return False
		self.health -= damage
		return True

	def take_healing(self, healing_points):
		if not self.is_alive():
			return False
		elif healing_points > (100 - self.health):
			self.health = 100
			return False
		self.health += healing_points
		return True


	
