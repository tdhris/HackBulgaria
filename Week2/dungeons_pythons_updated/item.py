from random import randint, randrange
from weapon import Weapon


WEAPONS = [("Callandor the Sword", 40, 0.4), ("Aiglos the Spear", 35, 0.3),
           ('Axe of the Dwarvish Lords', 30, 0.3), ('Spear of Vix', 60, 0.6),
           ('Mace of Cuthbert', 50, 0.5), ('Hammer of Kharas', 55, 0.5),
           ('Dagger of Time', 70, 0.7)]


def generate_item():
    random = randint(0, 1)
    if random:
        weapon_id = randrange(len(WEAPONS))
        weapon_type = WEAPONS[weapon_id][0]
        weapon_damage = WEAPONS[weapon_id][1]
        weapon_critical_hit = WEAPONS[weapon_id][2]
        item = Weapon(weapon_type, weapon_damage, weapon_critical_hit)
    else:
        healing_points = randint(50, 100)
        item = HealingPotion(healing_points)

    return item


class HealingPotion:
    def __init__(self, healing_points):
        self.healing_points = healing_points

    def __repr__(self):
        if self.healing_points >= 50 <= 70:
            return "Healing Potion"
        if self.healing_points > 70 <= 99:
            return "Strong Healing Potion"
        else:
            return "Perfect Healing Potion"
