from python import Python
from anaconda import Anaconda
from fight import Fight
from weapon import Weapon
from item import generate_item, HealingPotion
from os import getcwd, listdir


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Dungeon:
    def __init__(self, level=1):
        self.map = self.load_map(level)
        self.player_symbol = 'H'
        self.game_ended = False

    def load_map(self, level):
        maps_dir = getcwd() + '/maps/'
        filename = 'level_' + str(level)
        if not filename in listdir(maps_dir):
            return False
        map_file = open(maps_dir + filename, "r")
        dungeon_map = []
        for row in map_file.readlines():
            line = []
            for char in row.rstrip('\n'):
                line.append(char)
            dungeon_map.append(line)
        map_file.close()
        return dungeon_map

    def print_map(self):
        for line in self.map:
            print(''.join(line))

    def spawn(self, hero):
        self.hero = hero
        position = self.get_starting_position()
        self.hero_position = position
        self.change_position(position, position)
        return True

    def get_starting_position(self):
        position = Position(0, 0)
        starting_symbol = 'S'
        is_found = False
        for line in self.map:
            position.y = 0
            for symbol in line:
                if symbol == starting_symbol:
                    is_found = True
                    break
                position.y += 1
            if is_found:
                break
            position.x += 1
        return position

    def move(self, direction):
        position = self.hero_position

        if direction == 'up' and self.is_move_valid(position, direction):
            new_position = Position(position.x - 1, position.y)

        elif direction == 'down' and self.is_move_valid(position, direction):
            new_position = Position(position.x + 1, position.y)

        elif direction == 'left' and self.is_move_valid(position, direction):
            new_position = Position(position.x, position.y - 1)

        elif direction == 'right' and self.is_move_valid(position, direction):
            new_position = Position(position.x, position.y + 1)

        else:
            return False

        if self.is_game_won(new_position):
            self.game_ended = True

        if self.map[new_position.x][new_position.y] == 'I':
            item = generate_item()
            if isinstance(item, Weapon):
                if item.damage >= self.hero.weapon.damage:
                    self.hero.equip_weapon(item)
            elif isinstance(item, HealingPotion):
                self.hero.take_healing(item.healing_points)
            else:
                return False

        if not self.should_fight(new_position):
            self.change_position(position, new_position)
            return True
        else:
            self.fight_for_territory(position, new_position)

    def change_position(self, old_position, new_position):
        self.hero_position = new_position
        self.map[old_position.x][old_position.y] = '.'
        self.map[new_position.x][new_position.y] = self.player_symbol

    def is_move_valid(self, position, direction):
        height, width = len(self.map) - 1, len(self.map[0]) - 1

        if direction == 'up' and position.x != 0 and self.map[position.x - 1][position.y] != '#':
            return True

        elif direction == 'down' and position.x != height and self.map[position.x + 1][position.y] != '#':
            return True

        elif direction == 'left' and position.y != 0 and self.map[position.x][position.y - 1] != '#':
            return True

        elif direction == 'right' and position.y < width and self.map[position.x][position.y + 1] != '#':
            return True
        return False

    def should_fight(self, position):
        if self.map[position.x][position.y] == 'P' or self.map[position.x][position.y] == 'A':
            return True
        return False

    def is_game_won(self, position):
        return self.map[position.x][position.y] == 'G'

    def fight_for_territory(self, position, new_position):
        initial_enemy_health = 100
        if self.map[new_position.x][new_position.y] == 'P':
            enemy = Python(initial_enemy_health)
        elif self.map[new_position.x][new_position.y] == 'A':
            enemy = Anaconda(initial_enemy_health)
        if not enemy:
            return False

        fight_to_the_death = Fight(self.hero, enemy)
        fight_to_the_death.simulate_fight()
        if self.hero.is_alive():
            self.change_position(position, new_position)
            return True
