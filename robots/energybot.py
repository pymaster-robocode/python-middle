from robots.robot import Robot


class EnergyBot(Robot):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def attack(self, other):
        super().attack(other)
        self.energy += 5