from robots.robot import Robot


class AggressiveBot(Robot):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def attack(self, other):
        super().attack(other)
        self.damage += 5