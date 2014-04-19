from random import randint


class Weapon:
    def __init__(self, weapon_type, damage, critical_strike_percent):
        self.type = weapon_type
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

        if not isinstance(critical_strike_percent, float):
            self.critical_strike_percent = 0
        elif critical_strike_percent >= 0 and critical_strike_percent <= 1.0:
            self.critical_strike_percent = float(critical_strike_percent)
        elif critical_strike_percent < 0:
            self.critical_strike_percent = 0
        else:
            self.critical_strike_percent = 1.0

    def __repr__(self):
        return self.type + ", Damage:  " + str(self.damage)

    def __eq__(self, other):
        return self.type == other.type and\
            self.damage == other.damage and\
            self.critical_strike_percent == other.critical_strike_percent

    def get_weapon(self):
        return self.type

    def critical_hit(self):
        if self.critical_strike_percent == 1.0:
            return True
        elif self.critical_strike_percent == 0:
            return False
        else:
            dice = randint(0, 100)
            if dice <= int(self.critical_strike_percent * 100):
                return True
            else:
                return False
