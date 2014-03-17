import entity
import weapon
import fight

class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Dungeon:
	def __init__(self, filename):
		self.file = open(filename, "r")
		self.map = []
		for row in self.file.readlines():
			line = []
			for char in row.rstrip('\n'):
				line.append(char)
			self.map.append(line)
		self.file.close()
		self.player_symbols = {}


	def print_map(self):
		for line in self.map:
			print(''.join(line))


	def set_player_symbol(self, player_name, entity_to_place):
		if isinstance(entity_to_place, entity.Hero):
			self.player_symbols[player_name] = 'H'
		else:
			self.player_symbols[player_name] = 'O'


	def get_player_position(self, player_symbol):
		position = Position(0, 0)
		is_found = False
		for line in self.map:
			position.y = 0
			for symbol in line:
				if symbol == player_symbol:
					is_found = True
					break
				position.y += 1
			if is_found:
				break
			position.x += 1
		return position


	def change_position(self, player_symbol, old_position, new_position):
		self.map[old_position.x][old_position.y] = '.'
		self.map[new_position.x][new_position.y] = player_symbol
	

	def spawn(self, player_name, entity_to_spawn):
		starting_position = self.get_player_position('S')

		if isinstance(entity_to_spawn, entity.Hero):
			setattr(self, "hero" , entity_to_spawn)
			self.hero.position = starting_position

		elif isinstance(entity_to_spawn, entity.Orc):
			setattr(self, "orc", entity_to_spawn)
			self.orc.position = starting_position
		
		else:
			return False

		self.set_player_symbol(player_name, entity_to_spawn)
		self.change_position(self.player_symbols[player_name], starting_position, starting_position)
		return True


	def is_move_valid(self, position, direction):
		height, width = len(self.map)-1, len(self.map[0])-1

		if direction == 'up' and position.x != 0 and self.map[position.x-1][position.y] != '#':
			return True

		elif direction == 'down' and position.x != height and self.map[position.x+1][position.y] != '#':
			return True

		elif direction == 'left' and position.y != 0 and self.map[position.x][position.y-1] != '#':
			return True

		elif direction == 'right' and position.y < width and self.map[position.x][position.y+1] != '#':
			return True
		return False


	def should_fight(self, position):
		if self.map[position.x][position.y] != '.' and self.map[position.x][position.y] != '#':
			return True
		return False

	def fight_for_territory(self, position, new_position):
		fight_to_the_death = fight.Fight(self.hero, self.orc)
		fight_to_the_death.simulate_fight()
		if self.hero.is_alive():
			self.change_position('H', position, new_position)
			return True
		else:
			self.change_position('O', position, new_position)
			return True


	def move(self, player_name, direction):
		player_symbol = self.player_symbols[player_name]
		position = self.get_player_position(player_symbol)

		if direction == 'up' and self.is_move_valid(position, direction):
			new_position = Position(position.x-1, position.y)

		elif direction == 'down' and self.is_move_valid(position, direction):
			new_position = Position(position.x+1, position.y)

		elif direction == 'left' and self.is_move_valid(position, direction):
			new_position = Position(position.x, position.y-1)

		elif direction == 'right' and self.is_move_valid(position, direction):
			new_position = Position(position.x, position.y+1)

		else:
			return False

		if not self.should_fight(new_position):
			self.change_position(player_symbol, position, new_position)
			return True
		else:
			self.fight_for_territory(position, new_position)
