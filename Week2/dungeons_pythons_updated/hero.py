from entity import Entity
from weapon import Weapon

DEFAULT_WEAPON = "Rusty Sword"


class Hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(health)
        self.name = name
        self.nickname = nickname
        bare_hands = Weapon(DEFAULT_WEAPON, 10, 0)
        self.weapon = bare_hands

    def __repr__(self):
        return self.name + " " + self.nickname

    def known_as(self):
        return str(self)

    def take_healing(self, healing_points):
        if healing_points > (100 - self.health):
            self.health = 100
            return False
        self.health += healing_points
        return True

    def equip_weapon(self, weapon_for_equipment):
        if not isinstance(weapon_for_equipment, Weapon):
            return False
        self.weapon = weapon_for_equipment
        return True

    def attack(self):
        if not self.weapon.critical_hit():
            return self.weapon.damage
        else:
            return self.weapon.damage * 2
