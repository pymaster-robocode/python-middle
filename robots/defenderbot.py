from robots.robot import Robot


class DefenderBot(Robot):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__shield = 5

    @property
    def shield(self):
        return self.__shield

    @shield.setter
    def shield(self, value):
        if value >= 0:
            self.__shield = value

    def take_damage(self, amount):
        reduced = max(0, amount - self.shield)
        print(f"{self.name} lowers incoming damage by {self.shield}")
        super().take_damage(reduced)