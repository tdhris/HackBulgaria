class Entity:
    def __init__(self, health):
        self.max_health = health
        self.health = self.max_health

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
